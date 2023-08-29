# QR-code-extraction
Extraction of QR codes from images using Yolov8. This project uses a pre-trained machine learning model to detect QR codes from images.

The base model used is an instance of Yolov8 finetuned using 410 images with qr codes. For more information about the training open the jupyter notebook train.ipynb inside the Training folder.

## Getting Started

To get started with running the QR code detection program locally, follow the steps below:

### Prerequisites

- Python 3.7 or higher installed
- Git installed (for cloning the repository)
- Docker (optional, for running the app in a Docker container)

## Installation

1. Clone this repository to your local machine

2. Open a terminal and navigate to the cloned repository

3. Install the required packages using the following command:
```bash
pip install -r requirements.txt
```

## Usage
1. Place the image in the repository's root directory
2. Run the FastAPI using the following command:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
This will start the app and make it accessible at http://localhost:8000.

3. Open your web browser and visit http://localhost:8000 to access the FastAPI interface.

4. Upload an image containing QR codes using the provided UI and see the QR codes extracted and displayed.
