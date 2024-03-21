import cv2

# Affiche la version d'OpenCV installée
print("Version d'OpenCV :", cv2.__version__)

# Initialisation d'OpenCV
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", cv2.imread("rectangle.png"))
cv2.waitKey(0)
cv2.destroyAllWindows()
