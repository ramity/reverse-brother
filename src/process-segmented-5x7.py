import cv2
import numpy as np
import math

# Load the image
image = cv2.imread("/photos/5x7_segmented.jpg")

# Convert to grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find contours
contours, hierarchy = cv2.findContours(grayscale, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
cv2.drawContours(image, contours, -1, (0, 0, 255), 2)

# Process outer contour
outer_contour = sorted(contours, key=cv2.contourArea)[-1]
outer_bounding_box = cv2.boundingRect(outer_contour)
cv2.rectangle(image, outer_bounding_box, (255, 0, 0), 2)

# Get the N,E,S,W points of the outer bounding box
outer_bounding_box_N_point = (outer_bounding_box[0] + outer_bounding_box[2] // 2, outer_bounding_box[1])
outer_bounding_box_E_point = (outer_bounding_box[0] + outer_bounding_box[2], outer_bounding_box[1] + outer_bounding_box[3] // 2)
outer_bounding_box_S_point = (outer_bounding_box[0] + outer_bounding_box[2] // 2, outer_bounding_box[1] + outer_bounding_box[3])
outer_bounding_box_W_point = (outer_bounding_box[0], outer_bounding_box[1] + outer_bounding_box[3] // 2)

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def centriod(contour):
    M = cv2.moments(contour)
    if M["m00"] == 0:
        return (contour[0][0][0], contour[0][0][1])
    return (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

# Closest contour
outer_N_contour = sorted(contours, key=lambda c: distance(centriod(c), outer_bounding_box_N_point))[0]
outer_E_contour = sorted(contours, key=lambda c: distance(centriod(c), outer_bounding_box_E_point))[0]
outer_S_contour = sorted(contours, key=lambda c: distance(centriod(c), outer_bounding_box_S_point))[0]
outer_W_contour = sorted(contours, key=lambda c: distance(centriod(c), outer_bounding_box_W_point))[0]

# Draw the N,E,S,W points of the outer bounding box
cv2.circle(image, centriod(outer_N_contour), 10, (255, 100, 100), -1)
cv2.circle(image, centriod(outer_E_contour), 10, (255, 100, 100), -1)
cv2.circle(image, centriod(outer_S_contour), 10, (255, 100, 100), -1)
cv2.circle(image, centriod(outer_W_contour), 10, (255, 100, 100), -1)

# Process inner contour
inner_contour = sorted(contours, key=cv2.contourArea)[-2]
inner_bounding_box = cv2.boundingRect(inner_contour)
cv2.rectangle(image, inner_bounding_box, (0, 255, 0), 2)

# Get the N,E,S,W points of the inner bounding box
inner_bounding_box_N_point = (inner_bounding_box[0] + inner_bounding_box[2] // 2, inner_bounding_box[1])
inner_bounding_box_E_point = (inner_bounding_box[0] + inner_bounding_box[2], inner_bounding_box[1] + inner_bounding_box[3] // 2)
inner_bounding_box_S_point = (inner_bounding_box[0] + inner_bounding_box[2] // 2, inner_bounding_box[1] + inner_bounding_box[3])
inner_bounding_box_W_point = (inner_bounding_box[0], inner_bounding_box[1] + inner_bounding_box[3] // 2)

# Closest contour
inner_N_contour = sorted(contours, key=lambda c: distance(centriod(c), inner_bounding_box_N_point))[0]
inner_E_contour = sorted(contours, key=lambda c: distance(centriod(c), inner_bounding_box_E_point))[0]
inner_S_contour = sorted(contours, key=lambda c: distance(centriod(c), inner_bounding_box_S_point))[0]
inner_W_contour = sorted(contours, key=lambda c: distance(centriod(c), inner_bounding_box_W_point))[0]

# Draw the N,E,S,W points of the inner bounding box
cv2.circle(image, centriod(inner_N_contour), 10, (100, 255, 100), -1)
cv2.circle(image, centriod(inner_E_contour), 10, (100, 255, 100), -1)
cv2.circle(image, centriod(inner_S_contour), 10, (100, 255, 100), -1)
cv2.circle(image, centriod(inner_W_contour), 10, (100, 255, 100), -1)

# Draw outer lines
cv2.line(image, centriod(outer_E_contour), centriod(outer_W_contour), (255, 100, 100), 2)
cv2.line(image, centriod(outer_N_contour), centriod(outer_S_contour), (255, 100, 100), 2)
cv2.line(image, centriod(outer_E_contour), centriod(outer_W_contour), (255, 100, 100), 2)
cv2.line(image, centriod(outer_N_contour), centriod(outer_S_contour), (255, 100, 100), 2)

# Draw inner lines
cv2.line(image, centriod(inner_E_contour), centriod(inner_W_contour), (100, 255, 100), 2)
cv2.line(image, centriod(inner_N_contour), centriod(inner_S_contour), (100, 255, 100), 2)
cv2.line(image, centriod(inner_E_contour), centriod(inner_W_contour), (100, 255, 100), 2)
cv2.line(image, centriod(inner_N_contour), centriod(inner_S_contour), (100, 255, 100), 2)

# Draw outer lines
cv2.line(image, outer_bounding_box_E_point, outer_bounding_box_W_point, (255, 0, 0), 2)
cv2.line(image, outer_bounding_box_N_point, outer_bounding_box_S_point, (255, 0, 0), 2)
cv2.line(image, outer_bounding_box_E_point, outer_bounding_box_W_point, (255, 0, 0), 2)
cv2.line(image, outer_bounding_box_N_point, outer_bounding_box_S_point, (255, 0, 0), 2)

# Draw inner lines
cv2.line(image, inner_bounding_box_E_point, inner_bounding_box_W_point, (0, 255, 0), 2)
cv2.line(image, inner_bounding_box_N_point, inner_bounding_box_S_point, (0, 255, 0), 2)
cv2.line(image, inner_bounding_box_E_point, inner_bounding_box_W_point, (0, 255, 0), 2)
cv2.line(image, inner_bounding_box_N_point, inner_bounding_box_S_point, (0, 255, 0), 2)

# Save the edge detected image
cv2.imwrite("/photos/5x7_final.jpg", image)

# Calculate the outer values
outer_w = distance(outer_bounding_box_E_point, outer_bounding_box_W_point)
outer_w = max(outer_w, distance(outer_bounding_box_E_point, outer_bounding_box_W_point))
outer_h = distance(outer_bounding_box_N_point, outer_bounding_box_S_point)
outer_h = max(outer_h, distance(outer_bounding_box_N_point, outer_bounding_box_S_point))

# Calculate the inner values
inner_w = distance(inner_bounding_box_E_point, inner_bounding_box_W_point)
inner_w = max(inner_w, distance(inner_bounding_box_E_point, inner_bounding_box_W_point))
inner_h = distance(inner_bounding_box_N_point, inner_bounding_box_S_point)
inner_h = max(inner_h, distance(inner_bounding_box_N_point, inner_bounding_box_S_point))

print(f"outer_w: {int(outer_w)} px")
print(f"outer_h: {int(outer_h)} px")
print(f"inner_w: {int(inner_w)} px")
print(f"inner_h: {int(inner_h)} px")

width, height, _ = image.shape
px_per_inch_x = width / 8
px_per_inch_y = height / 8

print(f"outer_w: {outer_w / px_per_inch_x:.2f} in")
print(f"outer_h: {outer_h / px_per_inch_y:.2f} in")
print(f"inner_w: {inner_w / px_per_inch_x:.2f} in")
print(f"inner_h: {inner_h / px_per_inch_y:.2f} in")
