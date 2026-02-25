import cv2
import numpy as np
import sys

# Get filepath from command line arguments
if len(sys.argv) != 3:
    print("Usage: python image-to-curves.py <image_path> <epsilon_factor>")
    sys.exit(1)

image_path = sys.argv[1]
epsilon_factor = float(sys.argv[2])
output_filename = image_path.replace(".jpg", "_curves.jpg")

def simplify_hollow_mask(mask_image, epsilon_factor):
    # 1. Find contours with Hierarchy
    # RETR_CCOMP retrieves all contours and organizes them into a 2-level hierarchy
    contours, hierarchy = cv2.findContours(mask_image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    simplified_curves = []

    for i in range(len(contours)):
        # 2. Douglas-Peucker Simplification
        # epsilon is the maximum distance between the original curve and its approximation
        epsilon = epsilon_factor * cv2.arcLength(contours[i], True)
        approx = cv2.approxPolyDP(contours[i], epsilon, True)
        simplified_curves.append({
            "points": approx,
        })

    return simplified_curves

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
curves = simplify_hollow_mask(image, epsilon_factor)

# Draw curves onto a black image
output_image = np.zeros_like(image)
for curve in curves:
    # Only draw contours of a certain area size
    if cv2.contourArea(curve["points"]) > 100:
        cv2.drawContours(output_image, [curve["points"]], -1, 255, 1)

# Flood fill between the shell and hole
point = [100, 1000]
cv2.floodFill(output_image, None, point, 255, 255)
cv2.imwrite(output_filename, output_image)

# Convert points to mesh

