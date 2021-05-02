import cv2
cap= cv2.VideoCapture(0)
name = 'name'
while(True):
    ret, frame= cap.read()
    #hit space to capture image
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord(' ') :
        cv2.imwrite("people/"+str(name)+".jpg", frame)
        break


cap.release()
cv2.destroyAllWindows()