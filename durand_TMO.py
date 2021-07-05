import cv2

hdrDebevec=cv2.imread('hdrDebevec.hdr',cv2.IMREAD_ANYDEPTH)
tonemapDurand = cv2.createTonemapDurand(1.5,4,1.0,1,1)
ldrDurand = tonemapDurand.process(hdrDebevec)
ldrDurand = 3 * ldrDurand
cv2.imwrite("ldr-Durand.jpg", ldrDurand * 255)
