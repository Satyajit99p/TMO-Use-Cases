import cv2

hdrDebevec=cv2.imread('hdrDebevec.hdr',cv2.IMREAD_ANYDEPTH)
tonemapReinhard = cv2.createTonemapReinhard(1.5, 0,0,0)
ldrReinhard = tonemapReinhard.process(hdrDebevec)
cv2.imwrite("ldr-Reinhard.jpg", ldrReinhard * 255)