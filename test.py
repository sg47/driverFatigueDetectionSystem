import cv
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth = cv2.CascadeClassifier('Mouth.xml')
right_eye = cv2.CascadeClassifier('rightEye.xml')

## Enable if driver wears specs. Specialised classifier
# eye_specs = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
##

# Counter for saving frames of the eye
count = 1

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        ## Eye tracking
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
	
	# detecting eye in only the face frame after isolating it
        eyes = right_eye.detectMultiScale(
		roi_gray,
		minSize=(40,40)
	)
	
	# Draw rectangle around eyes
        for (ex,ey,ew,eh) in eyes:
	    roi_color_eye = roi_color[ey:ey+eh, ex:ex+ew]
	    roi_color_eye = cv.fromarray(roi_color_eye)
 	    cv.SaveImage((str(count) + ".jpg"), roi_color_eye)
	    count += 1	    
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

	# mouth tracking
	mouthArea = mouth.detectMultiScale(roi_gray,minSize=(40,40),maxSize=(400,400))
        
	# Draw rectangle around mouth
        for (mx,my,mw,mh) in mouthArea:
	    if(mx in range(115,135) and my in range(225,300)):
            	cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(255,0,255),2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
