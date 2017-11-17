# -*- coding: utf-8 -*-
"""
Created on Thu May  4 13:55:03 2017

@author: p
"""

import cv2 as cv
#import numpy as np

cap = cv.VideoCapture(0)
fgbg = cv.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    
#    cv.imshow('Original', frame)
#    cv.imshow('After', fgmask)
    res = cv.bitwise_and(frame, frame, mask = fgmask)
    cv.imshow('masked', res)
    
    k = cv.waitKey(5) & 0xFF
    if k ==27:
        break
    
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)    
cap.release()