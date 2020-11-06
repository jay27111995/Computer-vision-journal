import cv2

img = cv2.imread('first.png', cv2.IMREAD_GRAYSCALE)

# get the dimensions of the image 
x, y = img.shape

# Did you notice that now img is an object ?
# what does imread return ? In what format ?

print("The dimensions of the image are %d and %d" %(x, y))

# Now lets resize our image 

img2 = cv2.resize(img, (int(x/2), int(y/2))) 

"""
Note:
    File "2_resize_and_save.py", line 15, in <module>
    img2 = cv2.resize(img, (x/2, y/2))
TypeError: integer argument expected, got float

Well, Apparently we can define types which I am 
not used to in python. But, I got this error so 
I am typecasting using Int()
"""

# Now lets save our image 
cv2.imwrite('my_resized_image.png', img2)

cv2.imshow('My first image', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
