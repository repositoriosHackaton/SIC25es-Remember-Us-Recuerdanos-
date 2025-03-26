from ultralytics import YOLO
import cv2
import math 
from funciones.msg import send_smg

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# model
model = YOLO("bestYolo8s100e.pt")

# object classes
classNames = ['cigarro', 'fumador', 'persona']
colors = [(255, 50, 50), (50, 255, 50), (50, 250, 255)]

while True:
    success, img = cap.read()
    results = model(img, stream=True, verbose=False)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values



            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            if confidence >= 0.65:
                print("Confidence --->",confidence)

                # class name
                cls = int(box.cls[0])
                print("Class name -->", classNames[cls])
                if classNames[cls] == 'cigarro': send_smg()
                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), colors[cls], 2)

                # object details
                org = [x1, y1-5]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 0.7
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(img, classNames[cls], org, font, fontScale, colors[cls], thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()