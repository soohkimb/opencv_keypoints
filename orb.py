import cv2
img = cv2.imread('image.png', 0)

orb = cv2.ORB_create()

keypoints, descriptor = orb.detectAndCompute(img, None)

img_draw = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('ORB', img_draw)
cv2.waitKey()
cv2.destroyAllWindows()
