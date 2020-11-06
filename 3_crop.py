import cv2

img = cv2.imread('first.png', cv2.IMREAD_COLOR)

# get the dimensions of the image 
x, y, z = img.shape

print("The dimensions of the image are %d * %d * %d" %(x, y, z))

# Now lets try to take out a part of the image 
# Apparently, this is known as Region of interest (ROI)
# Always good to know the different terminologies 
# Are you having fun upto now ?

roi = img[100:150, 100:150, 1]

# Did you notice that the image object can also be 
# accesed as an array. This seems to be more than just 
# a mere object

cv2.imshow("My region of interest", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
