import cv2

source = cv2.imread("/Users/brycekan/Downloads/Lanes.jpg")
window_name = "image"
#Need to convert to grayscale for gaussian blur
cropped_image = source[300:2080, 150:1030]
#cv2.imshow("cropped", cropped_image)

image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

#GaussianBlurring: reduces image noise and elimiates bright pixels
blurred = cv2.GaussianBlur(src=image, ksize=(3, 5), sigmaX=0.5) 

#Using Canny, Take input of blurred and apply thresholds for 100<edges<400
edges = cv2.Canny(blurred, 100, 400) 

cv2.imshow(window_name, edges) 

cv2.waitKey(0)

cv2.destroyAllWindows()