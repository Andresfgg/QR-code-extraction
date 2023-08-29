# QR-code-extraction
Extraction of QR codes from images using Yolov8. This project uses a pre-trained machine learning model to detect QR codes from images.

The base model used is an instance of Yolov8 finetuned using 410 images with qr codes. For more information about the training open the jupyter notebook train.ipynb inside the Training folder.

## Getting Started

To get started with running the QR code detection program locally, follow the steps below:

### Prerequisites

- Python 3.7 or higher installed
- Git installed (for cloning the repository)
- Docker (optional, for running the app in a Docker container)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd qr-code-detection