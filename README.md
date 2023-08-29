# QR-code-extraction
Extraction of QR codes from images using Yolov8. This project uses a pre-trained machine learning model to detect QR codes from images.

The base model used is an instance of Yolov8 finetuned using 410 images with qr codes. For more information about the training open the jupyter notebook train.ipynb inside the Training folder.

## Getting Started

To get started with running the QR code detection program locally, follow the steps below:

### Prerequisites

- Python 3.7 or higher installed
- Git installed (for cloning the repository)

## Installation

1. Clone this repository to your local machine

2. Open a terminal and navigate to the cloned repository

3. Install the required packages using the following command:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the FastAPI using the following command:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
This will start the app and make it accessible at http://localhost:8000.

2. Open a new terminal and navigate to the repository where you have your image
3. Use the 'curl' command to send a POST request to the endpoint
```bash
curl -X POST -F "file=@path_to_your_image.jpg" http://localhost:8000/detect_qr/ --output output.jpg
```
Replace 'path_to_your_image.jpg' with the name of your image and 'output.jpg' with the name you want the final image with the QR code to have.

For example, if the image is named 'image-to-detect.jpg' and we want to save the image of the qr code in 'extracted-QR-code.jpg' you should use the following command 
```bash
curl -X POST -F "file=@image-to-detect.jpg" http://localhost:8000/detect_qr/ --output extracted-QR-code.jpg
```
