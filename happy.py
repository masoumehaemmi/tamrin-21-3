import cv2

angri = cv2.imread("angri.jpg" , 0)


happi = cv2.imread("angri.jpg"  , 0)


for i in range(angri.shape[0]):

    for j in range(angri.shape[1]):

        happi[angri.shape[0] - 1 - i, angri.shape[1] - 1 - j] = angri[i, j]
        
cv2.imwrite("happy1.jpg", happi)


cv2.waitKey()



