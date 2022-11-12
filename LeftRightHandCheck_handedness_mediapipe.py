# import the opencv library
import cv2
import mediapipe

# define a video capture object
vid = cv2.VideoCapture(0)
with mediapipe.solutions.hands.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=1) as hands:
        while vid.isOpened():
            ret, frame = vid.read()
            if ret == False:
                continue
            
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
            if cv2.waitKey(1) & 0xFF == ord('q'):
             break    
            frame = cv2.flip(frame, 1)
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            cv2.imshow('frame', frame)
            try:
                print(results.multi_handedness)
            except:
                print("not")
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
