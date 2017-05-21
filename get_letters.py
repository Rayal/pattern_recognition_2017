import cv2
import numpy as np
#from sys import argv

img = cv2.imread(argv[1])

img_gray = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 100, 255, cv2.THRESH_BINARY_INV)[1]

#cv2.imshow("gray", img_gray)
#cv2.waitKey(1)

kernel = np.ones((3, 3))

#kernel[1][:] = 1
#kernel.T[1][:] = 1

#print (kernel)

dil = cv2.dilate(img_gray, kernel) 
er = cv2.erode(img_gray, kernel)
res = dil - er

#res = img_gray - er

img2, contours, heirarchy = cv2.findContours(img_gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)

#cv2.imshow("img2", img2)
#cv2.waitKey(1)

contours = [c for c in contours if len(c) > 2]

#print(np.mean([len(c) for c in cont[1]]))
#print(np.std([len(c) for c in cont[1]]))

#cv2.imshow("res",cv2.drawContours(img.copy(), contours, -1, (0, 0, 255)))
#cv2.imshow("ermmm...", res)
#cv2.waitKey()
#cv2.destroyAllWindows()

contours = [c/c.max(axis = 0) for c in contours]


