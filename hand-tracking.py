import cv2
import mediapipe as mp
hand_tracking = mp.solutions.hands
hands = hand_tracking.Hands()

Hand_shape = mp.solutions.drawing_utils
model = cv2.VideoCapture(0)

while model.isOpened():
    ret, frame = model.read()
    if not ret:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            Hand_shape.draw_landmarks(frame, landmarks, hand_tracking.HAND_CONNECTIONS)

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
model.release()
cv2.destroyAllWindows()


