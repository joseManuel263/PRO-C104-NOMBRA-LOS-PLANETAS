import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img,
            "Sol   (UwU)",
            (100,80),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 2,
            color = (0,0,255))

cv2.imshow ("PRO-C104: NOMBRA LOS PLANETAS", img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)