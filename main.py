# Import Libraries
from ultralytics import YOLO
import os
import cv2
import matplotlib.pyplot as plt
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from starlette.responses import Response

# Create FastAPI instance
app = FastAPI()

# Set the threshold for detection confidence
threshold = 0.7

# Load pre-trained YOLO model
MODEL_PATH = r".\last.pt"
model = YOLO(MODEL_PATH)


@app.post("/detect_qr/")
async def detect_qr_codes(file: UploadFile = File(...)):
    # Save the uploaded image temporarily
    with open("temp_image.jpg", "wb") as f:
        f.write(file.file.read())
    
    # Load the image and apply the YOLO model
    image = cv2.imread("temp_image.jpg")
    results = model.predict("temp_image.jpg")[0]
    cropped_images =[]

    # Iterate through detected objects
    for result in results.boxes.data.tolist():
        x1,y1,x2,y2,score,class_id = result

        # Draw box if confidence is above threshold
        if score > threshold:
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            # Crop object in bounding box
            cropped_image = image[int(y1):int(y2), int(x1):int(x2)]
            cropped_images.append(cropped_image)

    # Convert the image to bytes
    img_bytes_list = [cv2.imencode(".jpg", img)[1].tobytes() for img in cropped_images]

    def generate():
        for img_bytes in img_bytes_list:
            yield img_bytes

    # Return the cropped images as a streaming response with appropriate content type
    return StreamingResponse(generate(), media_type="image/jpeg")
