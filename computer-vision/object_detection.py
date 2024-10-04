import cv2
import os
import numpy as np

# Caffe (Convolutional Architecture for Fast Feature Embedding) is a deep learning framework for 
# creating image classification and image segmentation models.
# Initially, users can create and save their models as plain text PROTOTXT files.
# After the model is trained and refined using Caffe, the program saves the trained model as a CAFFEMODEL file.

# Load the MobileNet SSD model
current_dir = os.path.dirname(__file__)
prototxt_path = os.path.join(current_dir, 'deploy.prototxt')
model_path = os.path.join(current_dir, 'mobilenet_iter_73000.caffemodel')
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# Classes that MobileNet SSD can detect, translated into Spanish
CLASSES = ['fondo', 'avion', 'bicicleta', 'pajaro', 'barco', 
 'botella', 'autobus', 'coche', 'gato', 'silla', 
 'vaca', 'mesa de comedor', 'perro', 'caballo', 
 'motocicleta', 'persona', 'planta en maceta', 
 'oveja', 'sofa', 'tren', 'televisor/monitor']


# Initialize the webcam using DirectShow
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Set desired resolution (adjust according to your webcam capabilities)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: no se puede abrir la cámara.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: No fue posible leer un cuadro de la cámara web.")
        break

    # Check if the frame is correctly captured
    if frame is None or frame.size == 0:
        print("Error: Cuadro vacío capturado")
        continue

    # Get the frame dimensions
    (h, w) = frame.shape[:2]

    # Prepare the frame to be fed to the model
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # Loop over the detections
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Filter out weak detections
        if confidence > 0.2:
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]

            # Extract the bounding box coordinates
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Draw the prediction on the frame
            label_text = f"{label}: {confidence:.2f}"
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label_text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Detección de Objetos en Vivo.', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Finalizando la detección de objetos...")
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
