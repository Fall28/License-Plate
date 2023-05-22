from easyocr import Reader
import cv2

car=cv2.imread('car1.jpg')
car=cv2.resize(car,(800,600))
gray=cv2.cvtColor(car,cv2.COLORBGR2GRAY)
