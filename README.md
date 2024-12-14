# Real-time Face Recognition System

A Python-based real-time face recognition system that uses your webcam to detect and identify faces. The system can recognize known faces from a pre-defined set of images and mark unknown faces accordingly.

## Features

- Real-time face detection and recognition using webcam
- Support for multiple known faces
- Recognition results displayed on video feed
- Video output saving capability
- Easy-to-use interface

## Requirements

- Python 3.x
- OpenCV (cv2)
- face_recognition

## Installation

1. Clone this repository or download the source code
2. download the dlib installation file that is compatabile with you python version from [here](https://github.com/z-mahmud22/Dlib_Windows_Python3.x) 
3. Install the required dependencies:
```bash
python -m pip install "dlib_file_you_downloaded"
pip install face_recognition
pip install opencv-python
pip install numpy
```

## Project Structure

```
face_recognition/
│
├── images/
│   └── known/         # Directory for known face images
│
├── webcam.py          # Main script for face recognition
├── face_reco.ipynb    # Jupyter notebook with face recognition examples
├── output.avi         # Output video file (generated during execution)
└── README.md
```

## Usage

1. Add known face images to the `images/known` directory
   - Each image should contain one clear face
   - Name the image files with the person's name (e.g., `john.jpg`, `jane.png`)
   - Supported formats: .png, .jpg, .jpeg, .bmp

2. Run the face recognition system:
```bash
python webcam.py
```

3. The system will:
   - Load known faces from the images directory
   - Open your webcam
   - Display the video feed with face recognition results
   - Save the output to 'output.avi'

4. Press 'q' to quit the application

## How it Works

1. The system loads and encodes known faces from the `images/known` directory
2. For each frame from the webcam:
   - Detects face locations
   - Encodes detected faces
   - Compares with known face encodings
   - Draws rectangles around detected faces
   - Labels faces as known names or "Unknown"
   - Saves the frame to output video

## Customization

You can customize the following parameters in the `FaceRecognition` class:
- `known_faces_dir`: Directory containing known face images
- `output_video_path`: Path for saving the output video
- `camera_index`: Index of the webcam to use (default: 0)

## Troubleshooting

- Ensure proper lighting conditions for better face detection
- Keep faces clearly visible to the camera
- Check if the webcam is properly connected and accessible
- Verify that known face images are clear and contain only one face

## License

This project is open-source and available under the MIT License.