import cv2, time

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

first_frame=None
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21,21),0)
    
    if first_frame is None:
        first_frame=gray
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray)    
    thresh_delta=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]    
    thresh_delta=cv2.dilate(thresh_delta, None, iterations=2)
    
    (cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 500:
            continue
        
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0,255,0),3)
        
    out.write(frame)
    
    #cv2.imshow("Gray Frame", gray)
    #cv2.imshow("Delta Frame",delta_frame)
    #cv2.imshow("Threshhold Frame",thresh_delta)
    cv2.imshow("Color Frame", frame)
    
    key=cv2.waitKey(1)
    print(gray)
    
    
    
    if key==ord('q'):
        break

video.release()

cv2.destroyAllWindows