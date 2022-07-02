from cgitb import grey
from email.mime import image
import cv2
import dlib


#đọc ảnh
img = cv2.imread("E:\python\code\project_AI\qh.png")

#chuyen doi anh sang mau Grey : 3D-2D
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

#dlib
face_detector = dlib.get_frontal_face_detector()

#load predictor : tạo điểm nhận diện trên khuôn mặt
predictor = dlib.shape_predictor('E:\python\code\project_AI\shape_predictor_68_face_landmarks.dat')
#nhap anh vao
faces = face_detector(gray) # là array gồm các khuôn mặt trong ảnh 

for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    
    #ve duong vien khuon mat
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=2)
    face_features = predictor(image=gray, box = face)
    
    #chạy vòng lặp hiển thị ra 68 điểm trên khuôn mặt
    for n in range(0, 68):
        x = face_features.part(n).x
        y = face_features.part(n).y
        
        #vẽ điểm chấm 
        cv2.circle(img=img, center=(x,y), radius=2, color=(0,0,255), thickness=1)
    
    


#hiển thị ảnh
cv2.imshow(winname="Face Recognition App", mat=img)

#wait for a key press to exit
cv2.waitKey(delay=0)

#close all windows
cv2.destroyAllWindows()
