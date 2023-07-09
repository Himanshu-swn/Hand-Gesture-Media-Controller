# images are combination of matrix
# greyscale images are simplest type of images
# black has 0 intesity and white has max
# intesity ranges from 0-255
# RGB images: images formed by addition of different intesities of red, blue and green components at every pixel.
# 1080p = 1080px height and 1920px width
# 8 bit images has 255px
# images are stored as BGR not RGB in opencv


import cv2
import numpy as np
# from multiprocessing.connection import wait
# from sre_constants import SUCCESS
# from tkinter import Frame

img_path = "./images/sherlock_kid.png"
img = cv2.imread(img_path)
# print(img)
# print(img.shape)
# h, v, c = img.shape
# print(h,v,c)                  # height width channels(RGB i.e 3 channels)
# cv2.imshow("image", img)

# ###### CROPPED IMAGE #####
# img_cropped = img[:, 300:-1]
# # cv2.imshow("cropped_image",img_cropped)

# ###### DRAWING ON IMAGE #####
# img[0:50, 50:100] = (0, 0, 225)
# cv2.rectangle(img, (0, 0), (100, 100), (0, 0, 255), thickness=2)
# cv2.circle(img, (100, 100), 50, (0, 0, 255), 2)
# cv2.putText(img, "Hi Happy !!!", (0, 200), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)
# cv2.imshow("image2", img)


###### BGR_TO_GREY #####
# img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_grey.shape)
# cv2.imshow("grey_image",img_grey)

# BGR_TO_HSV #####                              # Hue, saturation, Lightness
# img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("hsv_image",img_hsv)

# ###### SAVING MODIFIED IMAGE #####
# # cv2.imwrite("./images/modified_images/sherlock_kid_grey.png",img_grey)

# ###### RESIZED IMAGE #####
# img_resized = cv2.resize(img, (int(img.shape[1]*0.5), int(img.shape[0]*0.5)))    # first width then height
# cv2.imshow("resized_image", img_resized)

# ###### WHITE IMAGE GENERATION #####
# white_img = np.full(img.shape, 255, dtype=np.uint8)
# # cv2.imshow("white_img",white_img)

# ###### NEGATIVE IMAGE #####
# img_negative = np.subtract(white_img, img)
# # cv2.imshow("negative_image",img_negative)

# ###### SUBTRACTING 50_RED FROM IMAGE #####
# img_red_50 = np.full(img.shape, [0, 0, 50], dtype=np.uint8)
# img_red_added = np.add(img, img_red_50)
# # cv2.imshow("red added image",img_red_added)

# ###### BLUR #####
# blur=cv2.GaussianBlur(img,(9,9),cv2.BORDER_DEFAULT)  # ksize should be of odd numbers, tuple of size 2
# cv2.imshow("blur",blur)

# ###### EDGE CASCADING #####
# canny=cv2.Canny(img,120,200)
# cv2.imshow("canny",canny)

# ###### DILATING IMAGE #####
# dilated=cv2.dilate(canny,(7,7),iterations=1)
# cv2.imshow("dilated",dilated)

# # ###### FLIPPING IMAGE #####
# flipped = cv2.flip(img, -1)   # 0 means vertical, 1 means horizontal, -1 means both
# cv2.imshow("flipped", flipped)

# wait for infinite time. specify values in ms if you want to end program after specific time
# cv2.waitKey(0)


# ##################################### VIDEO_READING #####################################

# video_reader = cv2.VideoCapture(0)  # 0 for reading from webcam

# while 1:
#     SUCCESS, frame = video_reader.read()
#     if not SUCCESS:
#         break

#     cv2.imshow("My webcam", frame)
#     key=cv2.waitKey(10)
#     if key==ord('q'):
#         break

# video_reader.release()
# cv2.destroyAllWindows()


# ################################ IMAGE THRESHOLDING ########################################

# # ---> it is a way to create binary image from greyscale or colored image

# img2_path = "./images/gray_scale.png"
# img2 = cv2.imread(img2_path)
# cv2.imshow("image 2",img2)

# ###### THRESHOLD FUNCTION #####
# # image converted to grayscale
# img2_grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# _, img2_thresh = cv2.threshold(img2_grey, 127, 255, cv2.THRESH_BINARY)  ## _, because it return 2 values :)
# # cv2.imshow("threshold image",img2_thresh)

# # ##### SELF THRESHOLD FUNCTION #####
# # def thresh(img):
# #     (h, w) = img.shape
# #     for i in range(h):
# #         for j in range(w):
# #             if (img[i, j] > 127):
# #                 img[i, j] = 255
# #             else:
# #                 img[i, j] = 0
# #     return img

# # cv2.imshow("self_threshold image", thresh(img2_grey))
