import cv2
import numpy as np
from scipy.stats import itemfreq



cameraCapture = cv2.VideoCapture(0)  
cv2.namedWindow('camera')
success, frame = cameraCapture.read()

while success:
    cv2.waitKey(1)
    success, frame = cameraCapture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 37)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1, 50, param1=160, param2=40)
    if not circles is None:
        circles = np.uint16(np.around(circles))
        max_r, max_i = 0, 0
        for i in range(len(circles[:, :, 2][0])):
            if circles[:, :, 2][0][i] > 50 and circles[:, :, 2][0][i] > max_r:
                max_i = i
                max_r = circles[:, :, 2][0][i]
        x, y, r = circles[:, :, :][0][max_i]
        if y > r and x > r:
            square = frame[y-r:y+r, x-r:x+r]
            zone_0 = square[square.shape[0]*2//8:square.shape[0]
                                * 6//8, square.shape[1]*3//8:square.shape[1]*4//8]
            gray_0 = cv2.cvtColor(zone_0, cv2.COLOR_BGR2GRAY)
            img_0 = cv2.medianBlur(gray_0, 37)

            zone_1 = square[square.shape[0]*2//8:square.shape[0]
                                * 6//8, square.shape[1]*4//8:square.shape[1]*5//8]
            gray_1 = cv2.cvtColor(zone_1, cv2.COLOR_BGR2GRAY)
            img_1 = cv2.medianBlur(gray_1, 37)
            
            """ret,thresh = cv2.threshold(zone_0,127,255,1)
            contours,h = cv2.findContours(thresh,1,2)
            for cnt in contours:
                approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
                print (len(approx))
                if len(approx)==4:
                    print ("right")"""
                
    cv2.imshow('camera', frame)
    try:
        cv2.imshow('camera2', square)
        cv2.imshow('camera_z0', img_0)
        cv2.imshow('camera_z2', img_1)
        image_data_0 = np.asarray(img_0)
        value_0 = 0
        for i in range(len(image_data_0)):
            for j in range(len(image_data_0[0])):
                value_0 = value_0 + image_data_0[i][j]
        image_data_1 = np.asarray(img_1)
        value_1 = 0
        for i in range(len(image_data_1)):
            for j in range(len(image_data_1[0])):
                value_1 = value_1 + image_data_1[i][j]
        if value_1 > value_0:
            print('LEFT')
        else:
            print('RIGHT')
        
           
        
        
    except:
        continue
    
        
