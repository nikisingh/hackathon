"# hackathon driver drowsiness detection" 

Algorithm :
Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the eye.
It checks 20 consecutive frames and if the Eye Aspect ratio is less than 0.25, Alert and BeepSound gets generated.
