import cv2
import numpy as np

hdrDebevec=cv2.imread('hdrDebevec.hdr',cv2.IMREAD_ANYDEPTH)
tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
ldrDrago = tonemapDrago.process(hdrDebevec)
ldrDrago =  3 * ldrDrago
cv2.imwrite("ldr-Drago.jpg", ldrDrago * 255)


