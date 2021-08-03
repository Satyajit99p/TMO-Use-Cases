import cv2
import numpy as np

gamma = 2.0
invgamma = 1/gamma
lookup = np.array([((i/255.0)**invgamma)*255 for i in np.arange(0,256)]).astype('uint8')

original = cv2.imread('hdrDebevec.png')
corrected = cv2.LUT(original,lookup)
cv2.imwrite('ldr_gamma.jpg',corrected)

#corrected=cv2.resize(corrected,(512,384))
#cv2.imshow('ldr_gamma.jpg',corrected)
#cv2.waitKey(0)

