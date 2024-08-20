
# import the opencv library 
import cv2 
import numpy as np

def region_of_interest(img, vertices):
    #initializes image to be black. Starting withi a blank mask
    mask = np.zeros_like(img)
    #fills polygon within vertices with white color
    cv2.fillPoly(mask, vertices, 255)
    # Returning the image only where mask pixels are non-zero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

vid = cv2.VideoCapture("/Users/brycekan/Downloads/LaneVideo.mp4")

if (vid.isOpened() == False):
  print("Error opening the video file")
else:
  fps = vid.get(cv2.CAP_PROP_FPS)
  print('Frames per second : ', fps,'FPS')
  frame_count = vid.get(cv2.CAP_PROP_FRAME_COUNT) 
  print('Frames in video ', frame_count,'frames')

frame_skip = 5

#Get height of video
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
#get width of video
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
roi_vertices = [(0, height), (width // 2, height // 2), (width, height)]

while(vid.isOpened()):
    ret, frame = vid.read() 
    if vid.get(cv2.CAP_PROP_POS_FRAMES) % frame_skip != 0:
        continue
    grayimage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Apply gaussian blur
    Gausblur = cv2.GaussianBlur(grayimage, (5, 5), 0)
    #Apply Canny function to obtain edges with a threshold
    edges = cv2.Canny(Gausblur, 50, 150) 
    #get roi edges
    roi_edges = region_of_interest(edges, np.array([roi_vertices], np.int32))
    #Determines what is a line segment
    #adjusted threshold, minlinelength, maxlinegap to video
    lines = cv2.HoughLinesP(roi_edges, rho=1, theta=np.pi/180,threshold= 150, minLineLength=100, maxLineGap=10)
    #draws each line onto each frame
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
    if ret == True:
        cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
      break

vid.release()
cv2.destroyAllWindows()

