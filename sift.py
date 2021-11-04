import cv2
img = cv2.imread('image.png', 0)
sift = cv2.SIFT_create()
# kp1, des1 = sift.detectAndCompute(img, None) #keypoint and descriptors

keypoints, descriptor = sift.detectAndCompute(img, None)
print('keypoint:',len(keypoints), 'descriptor:', descriptor.shape)
print(descriptor)

img_draw = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT', img_draw)
cv2.waitKey()
cv2.destroyAllWindows()
