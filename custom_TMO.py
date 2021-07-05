import cv2
import numpy as np 

hdr = cv2.imread('hdrDebevec.hdr',cv2.IMREAD_ANYDEPTH)
custom=cv2.createTonemap(2.5)
image=custom.process(hdr)
image = 3 * image
cv2.imwrite("ldr-custom.jpg", image*255)

