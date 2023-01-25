import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
import sys
import os
import pytesseract

if __name__ == "__main__":
    # img = cv2.imread('./car1.jpg',cv2.IMREAD_COLOR)
    # img = cv2.resize(img, (620,480) )
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
    # gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
    # edged = cv2.Canny(gray, 1, 300) #Perform Edge detection
    # cv2.imshow('',edged)
    # cv2.waitKey()

    car_number = 1

    if car_number == 1:
        # img = cv2.imread('./LAB7_OPENCV/car1.jpg',cv2.IMREAD_COLOR)
        img = cv2.imread('./car1.jpg', cv2.IMREAD_COLOR)
    elif car_number == 2:
        # img = cv2.imread('./LAB7_OPENCV/car2.jpg',cv2.IMREAD_COLOR)
        img = cv2.imread('./car2.jpg', cv2.IMREAD_COLOR)
    elif car_number == 3:
        # img = cv2.imread('./LAB7_OPENCV/car3.jpg',cv2.IMREAD_COLOR)
        img = cv2.imread('./car3.jpg', cv2.IMREAD_COLOR)
    else:
        # img = cv2.imread('./LAB7_OPENCV/car4.jpg',cv2.IMREAD_COLOR)
        img = cv2.imread('./car4.jpg', cv2.IMREAD_COLOR)
    # cv2.imshow('',img)
    # cv2.waitKey()

    img = cv2.resize(img, (620, 480))
    # cv2.imshow('',img)
    # cv2.waitKey()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grey scale
    # cv2.imshow('',gray)
    # cv2.waitKey()

    blur_factor = 0
    if car_number == 1:
        blur_factor = 17
    elif car_number == 2:
        blur_factor = 30
    elif car_number == 3:
        blur_factor = 17
    elif car_number == 4:
        blur_factor = 35
    else:
        pass
    gray = cv2.bilateralFilter(
        gray, 11, blur_factor, blur_factor)  # Blur to reduce noise
    # cv2.imshow('',gray)
    # cv2.waitKey()

    canny_a = 0
    canny_b = 0
    if car_number == 1:
        canny_a = 100
        canny_b = 300
    elif car_number == 2:
        canny_a = 200
        canny_b = 300
    elif car_number == 3:
        canny_a = 50
        canny_b = 150
    else:
        canny_a = 150
        canny_b = 120
    edged = cv2.Canny(gray, canny_a, canny_b)  # Perform Edge detection
    cv2.imshow('', edged)
    cv2.waitKey()

    if car_number == 1:
        shapes = [4, 5, 6, 7]
    elif car_number == 2:
        shapes = [4, 5, 6, 7]
    elif car_number == 3:
        canny_a = 50
        canny_b = 150
    else:
        shapes = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # shapes = [11,12 ,13 ,14 ,15 ,16]

    # find contours in the edged image, keep only the largest
    # ones, and initialize our screen contour
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    all_edges = cv2.drawContours(img.copy(), cnts, -1, (0, 255, 0), 2)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    screenCnt = None

    # for ind, each in enumerate(cnts):
    #     print("------------")
    #     print(f"index = {ind}")
    #     print(f"len(each) = {len(each)}")
    #     print(f"cv2.contourArea(each) = {cv2.contourArea(each)}")
    #     all_edges = cv2.drawContours(img.copy(), each , -1, (0, 255, 0), 2)
    #     cv2.imshow('',all_edges)
    #     cv2.waitKey()

    # loop over our contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.009 * peri, True)
        # if our approximated contour has four points, then
        # we can assume that we have found our screen
        if len(approx) in shapes:
            screenCnt = approx
            break

    if screenCnt is None:
        detected = 0
        print("No contour detected")
    else:
        detected = 1

    if car_number == 2:
        screenCnt = cnts[22]

    if detected == 1:
        cv2.drawContours(img, screenCnt, -1, (0, 255, 0), 3)
        # cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

    # Masking the part other than the number plate
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1,)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    # Now crop
    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = gray[topx:bottomx+1, topy:bottomy+1]

    cv2.imshow('image', img)
    cv2.imshow('Cropped', Cropped)

    predicted_result = pytesseract.image_to_string(Cropped, lang='eng',
                                                   config='--oem 3 --psm 6')
    predicted_result = pytesseract.image_to_string(Cropped, config='--psm 6')

    filter_new_predicted_result_GWT2180 = "".join(
        predicted_result.split()).replace(":", "").replace("-", "")
    print(filter_new_predicted_result_GWT2180)

    print(f"predicted_result = {predicted_result}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
