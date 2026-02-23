import cv2
import numpy as np

FILE_PATH = "/photos/5x7.jpg"

image = cv2.imread(FILE_PATH)

NW_point = (360, 481)
NE_point = (2728, 385)
SE_point = (2864, 2903)
SW_point = (172, 2861)

image_points = np.float32([NW_point, NE_point, SE_point, SW_point])

# Calculate the min width and height of the points
w = min(NE_point[0] - NW_point[0], SE_point[0] - SW_point[0])
h = min(SE_point[1] - NE_point[1], SW_point[1] - NW_point[1])
transform_points = np.float32([[0, 0], [w, 0], [w, h], [0, h]])

# Calculate the transformation matrix
M = cv2.getPerspectiveTransform(image_points, transform_points)

# Apply the transformation
transformed_image = cv2.warpPerspective(image, M, (int(w), int(h)))

# Save the transformed image
cv2.imwrite("/photos/5x7_transformed.jpg", transformed_image)

# # Save the edge detected image
# cv2.imwrite("/photos/4x4_edges.jpg", edges)

# Find contours in transformed_image
grayscale = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2GRAY)

# Find edges
edges = cv2.Canny(grayscale, 55, 55)

# Save the edge detected image
cv2.imwrite("/photos/5x7_edges.jpg", edges)
