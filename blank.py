import cv2
import numpy as np

img = np.zeros((400,400,3),dtype='uint8')
cv2.imshow("blank",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

