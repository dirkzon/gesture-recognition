import cv2
import time
import numpy as np
from joblib import load
from mediapipe.python.solutions import drawing_utils, hands

print('GESTURE RECOGNITION')
print("Press 'q' to quit")
print("Press 'd' for debug")

gesture_model = load('./model/gesture_model.pkl')

hand_model = hands.Hands(static_image_mode=True, 
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7, max_num_hands=4)

debug = False
t = 0
txt_offset = (-60, 30)

vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)
resolution = (vc.get(3), vc.get(4))

while vc.isOpened():
    ret, frame = vc.read()

    results = hand_model.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            if debug:
                drawing_utils.draw_landmarks(frame, handLandmarks, 
                    hands.HAND_CONNECTIONS)

            x, y = [], []
            for lm in handLandmarks.landmark:
                x.append(lm.x)
                y.append(lm.y)
            
            txt_pos = np.add(np.multiply(resolution, (x[0], y[0])), txt_offset)
            
            points = np.asarray([x,y])
            min = points.min(axis=1, keepdims=True)
            max = points.max(axis=1, keepdims=True)
            normalized = np.stack((points-min)/(max-min), axis=1).flatten()
            pred = gesture_model.predict_proba([normalized])

            gesture = pred.argmax(axis=1)[0]
            confidence = pred.max()

            cv2.putText(frame, "'{}',{:.1%}".format(gesture, confidence), 
                txt_pos.astype(int), cv2.FONT_HERSHEY_DUPLEX,  1, 
                (0, 255, 255), 1, cv2.LINE_AA)

    fps = 1/(time.time()-t)
    t = time.time()

    if debug:
        cv2.putText(frame, "{}x{}; {}fps".format(*resolution, int(fps)), 
            (0,15), cv2.FONT_HERSHEY_DUPLEX,  0.6, (0, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        vc.release()
    if key == ord('d'):
        debug = not debug

cv2.destroyAllWindows()
