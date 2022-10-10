import cv2
import os
import uuid
import time

if __name__ == "__main__":
    labels = ["mug_front", "mug_back", "mug_left", "mug_right"]
    number_imgs = 5

    images_path = os.path.join("data", "collectedImages")

    if not os.path.exists(images_path):
        if os.name == "posix":
            os.system(f'mkdir -p {images_path}')
        if os.name == "nt":
            os.system(f'mkdir {images_path}')
    for label in labels:
        path = os.path.join(images_path, label)
        if not os.path.exists(path):
            os.system(f'mkdir {path}')

    #Capturing Images
    for label in labels:
        cap = cv2.VideoCapture(0)
        print('collecting Images for {}'.format(label))
        time.sleep(5)
        for img_num in range(number_imgs):
            print("Collecting image {}".format(img_num))
            ret, frame = cap.read()
            img_name = os.path.join(images_path, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(img_name, frame)
            cv2.imshow('frame', frame)
            time.sleep(2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
