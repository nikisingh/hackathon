# import the opencv library 
import cv2 

# define a video capture object 
vid = cv2.VideoCapture(0) 

while(True): 
	# Capture the video frame 
	ret, frame = vid.read() 

	# Display the resulting frame 
	cv2.imshow('driver-drowsiness', frame) 
	
	# the 'x' button is set as the quitting button 
	if cv2.waitKey(1) & 0xFF == ord('x'): 
		break

# After the above while loop release the a video capture object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 