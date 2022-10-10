import cv2

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()

        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)

        # Wait keys
        c = cv2.waitKey(1)

        if cv2.waitKey(1) & 0xFF == ord('y'):
            cv2.imwrite('images/c1.png', frame)
            cv2.destroyAllWindows()

        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


