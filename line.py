import cv2
import numpy as np

img = np.zeros((400,400,3),dtype='uint8')

cv2.line(img,(20,160),(100,160),(255,0,0),20)

cv2.imshow("blank",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

