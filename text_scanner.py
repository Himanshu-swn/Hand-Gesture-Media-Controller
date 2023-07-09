import cv2

img3_path = "./images/book_page.jpg"
img3 = cv2.imread(img3_path)
cv2.imshow("image 3",img3)
img3_grey = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
thresh_val, img3_thresh = cv2.threshold(img3_grey, 200, 255, cv2.THRESH_OTSU)  ## _, because it return 2 values :)
print(thresh_val)
cv2.imshow("text enhanced B/W image",img3_thresh)

cv2.waitKey(0)