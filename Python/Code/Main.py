import cv2
import matplotlib.pyplot as plt


cv2_img = cv2.imread('../Images/Natural Images/Saint.jpg')
cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
hsv_cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2HSV)

white = (0,0, 17)
black = (360, 59, 96)

mask = cv2.inRange(hsv_cv2_img, white, black)

result = cv2.bitwise_and(cv2_img, cv2_img, mask=mask)

plt.imshow(mask, cmap="gray")
# plt.imshow(result)
plt.show()
