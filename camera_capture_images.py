import cv2
import numpy as np

  
capture = cv2.VideoCapture(0)

path='C:/Users/srina/Desktop/python_opencv/sam/'
i=0
while(True):
      
    retur, frame = capture.read()
    cv2.imshow('video camera', frame)
    
    color_image = np.asanyarray(frame)
    
    key = cv2.waitKey(1)
    
     #to save the date
    if key & 0xFF == ord('s') or key & 0xFF == ord('s'):
         i +=1
         cv2.imwrite(path+str(i)+'.png',color_image)
         print("The user pressed s to save image: ",i)

    # Press esc or 'q' to close the image window
    if key & 0xFF == ord('q') or key == 27 or key & 0xFF == ord('Q'):
            #capture.release()
            cv2.destroyAllWindows()
            break