import face_recognition
import cv2
import os

class FaceRecognition:
    def __init__(self, known_faces_dir='images/known', output_video_path='output.avi'):
        """
        Initialize the face recognition system

        :param known_faces_dir: Directory containing known face images
        :param output_video_path: Path to save the output video
        """
        self.known_encodings = []
        self.known_names = []
        self.known_faces_dir = known_faces_dir
        self.output_video_path = output_video_path
        self.load_known_faces()

    def load_known_faces(self):
        """
        Load known faces from the specified directory
        """
        try:
            # Get all image files from the known faces directory
            known_face_paths = [
                os.path.join(self.known_faces_dir, f) 
                for f in os.listdir(self.known_faces_dir) 
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))
            ]

            # Process each known face image
            for path in known_face_paths:
                try:
                    # Load image and get face encoding
                    image = face_recognition.load_image_file(path)
                    encoding = face_recognition.face_encodings(image)[0]

                    # Store encoding and name
                    self.known_encodings.append(encoding)
                    # Use filename (without extension) as name
                    name = os.path.splitext(os.path.basename(path))[0]
                    self.known_names.append(name)

                except Exception as e:
                    print(f"Error processing {path}: {e}")

            print(f"Loaded {len(self.known_names)} known faces")

        except Exception as e:
            print(f"Error loading known faces: {e}")

    def recognize_faces_in_video(self, camera_index=0):
        """
        Perform real-time face recognition using webcam

        :param camera_index: Index of the camera to use (default: 0)
        """
        # Initialize video capture
        video_capture = cv2.VideoCapture(camera_index)

        # Get video properties for saving output
        frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(video_capture.get(cv2.CAP_PROP_FPS)) or 20  # Default to 20 if FPS is unavailable

        # Initialize VideoWriter
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.output_video_path, fourcc, fps, (frame_width, frame_height))

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            if not ret:
                print("Failed to grab frame")
                break

            # Convert the image from BGR color to RGB
            rgb_frame = frame[:, :, ::-1]

            # Find all face locations and face encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            # Loop through each face found in the frame
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # Compare faces
                matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
                name = "Unknown"

                # If a match is found
                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.known_names[first_match_index]

                # Draw rectangle around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                # Draw name label
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Write the frame to the output video
            out.write(frame)

            # Display the resulting frame
            cv2.imshow('Face Recognition', frame)

            # Hit 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the capture and close windows
        video_capture.release()
        out.release()
        cv2.destroyAllWindows()

    def run(self, camera_index=0):
        """
        Run the face recognition system

        :param camera_index: Index of the camera to use (default: 0)
        """
        if not self.known_encodings:
            print("No known faces loaded. Please check the known faces directory.")
            return

        self.recognize_faces_in_video(camera_index)

# Example usage
def main():
    try:
        # Create an instance of FaceRecognition
        face_rec = FaceRecognition(output_video_path='output.avi')

        # Run the face recognition
        face_rec.run()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
