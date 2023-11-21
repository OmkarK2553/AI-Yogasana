import cv2
import numpy as np

image = cv2.imread(r'D:\OpenCV Practice\Comparative_Study\comp_study\output_frames\Front\1_sit_0000.jpg')  

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

selected_contour = None
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 200:
        selected_contour = contour
        break

if selected_contour is not None:
    coordinates = selected_contour.reshape(-1, 2)
    print(coordinates)
else:
    print("Hand-band not found in the image.")

cv2.drawContours(image, [selected_contour], -1, (0, 255, 0), 2)

cv2.imshow('Image with Contour', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
