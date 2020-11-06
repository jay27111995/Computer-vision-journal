import cv2

# cv2 is the python package/class
# You are accessing the function imread of class cv2
# Second parameter to get the image in either grayscale or color  
img = cv2.imread('first.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('My first image', img)

# The waitkey with input parameter 0 tells the program to wait until
# the user gives a keyboard input
# This way, we can preview the image and exit the program when we give a 
# keystroke 
cv2.waitKey(0)
cv2.destroyAllWindows()

