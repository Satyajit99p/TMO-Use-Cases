import cv2
import numpy as np


# List of exposure times
times = np.array([ 1/30.0, 0.25, 2.5, 15.0 ], dtype=np.float32)
#times = np.array([ 4.5,7.0,0.08,0.1,0.05,2.5 ], dtype=np.float32)
#list of image files
filenames = ["StLouisArchMultExpEV-4.72.jpg","StLouisArchMultExpEV-1.82.jpg",
             "StLouisArchMultExpEV+1.51.jpg","StLouisArchMultExpEV+4.09.jpg"]
#filenames=['0.83.jpg','2.33.jpg','-0.83.jpg','-2.33.jpg','-0.33.jpg','0.33.jpg']
images = []
for filename in filenames:
    im = cv2.imread(filename)
    images.append(im)

# Align input images
alignMTB = cv2.createAlignMTB()
alignMTB.process(images, images)

# Obtain Camera Response Function (CRF)
calibrateDebevec = cv2.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(images, times)

# Merge images into an HDR linear image
mergeDebevec = cv2.createMergeDebevec()
hdrDebevec = mergeDebevec.process(images, times, responseDebevec)
# Save HDR image.
cv2.imwrite("hdrDebevec.hdr", hdrDebevec)
