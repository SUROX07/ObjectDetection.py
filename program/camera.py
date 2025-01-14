import cv2
from gui_buttons import Buttons

class VideoCamera(object):
    net=cv2.dnn.readNet("dnn_model\yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
    model= cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1/255)

    classes=[]
    with open("dnn_model/classes.txt", "r") as file_object:
        for class_name in file_object.readlines():
            class_name= class_name.replace("\n","")
            classes.append(class_name)


    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cv2.namedWindow("Frame")
    cv2.setWindowProperty('Frame', cv2.WND_PROP_TOPMOST, cv2.WINDOW_NORMAL)

    while True:
        ret, frame=cap.read()
        
        (class_ids, scores, bboxes) = model.detect(frame)
        for class_ids, scores, bbox in zip(class_ids, scores, bboxes):
            (x, y, w, h)= bbox
            class_name=classes[class_ids]
            if class_name == "person" :
                cv2.putText(frame, class_name, (x, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (200, 0, 50), 2)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 0, 50), 3)
                cv2.putText(frame, "Person Detected...", (5, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 1)
            else:
                cv2.putText(frame, "Nothing Detected...", (5, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 1)




    
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) 
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()