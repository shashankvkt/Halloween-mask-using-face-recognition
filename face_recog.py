import numpy as np
import cv2

mask = cv2.imread('spook.jpg')

BLUE = [0,0,0]

background = cv2.imread('scary.jpg')

cap = cv2.VideoCapture(0)

while True:
    ret,image = cap.read()
    height, width = image.shape[:2]
    background = cv2.resize(background,(width,height))

    add = cv2.addWeighted(image,0.5,background,0.5,0)
    
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    faces = face_cascade.detectMultiScale(gray,1.2,5)

    for (x,y,w,h) in faces:    
        masks = cv2.resize(mask,(h,w))
        
        break    
    
   
    ball = masks[0:h,0:w]
    add[y:y+w,x:x+h] = ball
    a,b,c =  masks.shape
   

    constant= cv2.copyMakeBorder(mask,y,height-(y+w),x,width-(x+h),cv2.BORDER_CONSTANT,value=BLUE)
    constant = cv2.resize(constant,(width,height))
    halo_effect = cv2.addWeighted(add,0.05,constant,0.95,0)
    halo_effect = cv2.addWeighted(image,0.45,constant,0.55,0)
    halo_effect = cv2.addWeighted(halo_effect,0.6,background,0.4,0)
    print constant.shape
   
    cv2.imshow('x',halo_effect)
    
    if cv2.waitKey(1) & 0xFF == ord('0'):
        break



  
cap.release()
cv2.destroyAllWindows()

