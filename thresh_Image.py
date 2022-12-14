import cv2
import imutils
from utills import four_point_transform


def local_threah(image):

    img_path = image
    big_img = cv2.imread(img_path)


    ratio = big_img.shape[0] / 500.0
    org = big_img.copy()
    img = imutils.resize(big_img, height = 500)



    gray_img = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img,(5,5),0)
    edged_img = cv2.Canny(blur_img,75,200)


    cnts,_ = cv2.findContours(edged_img.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts,key=cv2.contourArea,reverse=True)[:5]
    for c in cnts:
        peri = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.02*peri,True)
        if len(approx)==4:
            doc = approx
            break
            
            
    p=[]
    for d in doc:
        tuple_point = tuple(d[0])
        cv2.circle(img,tuple_point,3,(0,0,255),4)
        p.append(tuple_point)



    warped = four_point_transform(org, doc.reshape(4, 2) * ratio)
    
    #warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)



    # T = threshold_local(warped, 11, offset = 10, method = "gaussian")
    # warped = (warped > T).astype("uint8") * 255

    cv2.imwrite('final.jpg',warped)
