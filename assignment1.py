import cv2
import numpy as np

cap= cv2.VideoCapture(0)
image1 = cv2.imread('F:\\assignement\\''pubg 1.jpg')
image2 = cv2.imread('F:\\assignement\\''pubg2.jpg')
image3 = cv2.imread('F:\\assignement\\''pubg3.jpg')
image4 = cv2.imread('F:\\assignement\\''pubg4.jpg')
image5 = cv2.imread('F:\\assignement\\''pubg5.jpg')
image6 = cv2.imread('F:\\assignement\\''pubg6.jpg')

choice = input("Enter your choice:")
while True:
    flag, frame=cap.read()
    if not flag:
        print("con not acess")
        break

    elif flag:
        if choice == '1':
            image1= cv2.resize(image1,(frame.shape[1], frame.shape[0]))
            blended_frame1 = cv2.addWeighted(frame, 0.8, image1, 0.5, gamma=0.1 )
            cv2.imshow("Blend",blended_frame1)
                
        elif choice == '2':
            image2= cv2.resize(image2,(frame.shape[1], frame.shape[0]))
            blended_frame2 = cv2.addWeighted(frame, 0.8, image2, 0.5, gamma=0.1)
            cv2.imshow("Blend", blended_frame2)

        elif choice == '3':
            image3= cv2.resize(image3,(frame.shape[1], frame.shape[0]))
            blended_frame3 = cv2.addWeighted(frame, 0.8, image3, 0.5, gamma=0.1)
            cv2.imshow("Blend", blended_frame3)

        elif choice == '4':
            image4= cv2.resize(image4,(frame.shape[1], frame.shape[0]))
            blended_frame4 = cv2.addWeighted(frame, 0.8, image4, 0.5, gamma=0.1)
            cv2.imshow("Blend", blended_frame4)

        elif choice == '5':
            image5= cv2.resize(image5,(frame.shape[1], frame.shape[0]))
            blended_frame5 = cv2.addWeighted(frame, 0.8, image5, 0.5, gamma=0.1)
            cv2.imshow("Blend", blended_frame5)

        elif choice == '6':
            image6= cv2.resize(image6,(frame.shape[1], frame.shape[0]))
            blended_frame6 = cv2.addWeighted(frame, 0.8, image6, 0.5, gamma=0.1)
            cv2.imshow("Blend", blended_frame6)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()                    