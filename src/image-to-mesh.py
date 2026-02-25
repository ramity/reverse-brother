import cv2
import numpy as np
from stl import mesh
import sys

# Get filepath from command line arguments
if len(sys.argv) != 2:
    print("Usage: python image-to-mesh.py <image_path>")
    sys.exit(1)

image_path = sys.argv[1]
output_filename = image_path.replace(".jpg", ".stl")
extrusion_height = 7.938 # 5/16ths in freedom units

def create_stl_from_mask(image_path, output_filename, extrusion_height):
    # 1. Load the image and convert to binary mask
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Could not load image.")
        return

    # Smooth edges without adding extra pixels
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # Flip image because image coordinates (y down) differ from Cartesian (y up)
    mask = np.flipud(img)
    height, width = mask.shape

    faces = []
    vertices = []

    # 2. Generate vertices for top and bottom surfaces
    # We only create vertices for the "white" parts of the mask
    for y in range(height):
        for x in range(width):

            if mask[y, x] == 255:
                # Top vertex (Z = extrusion_height)
                v_top = [x, y, extrusion_height]
                # Bottom vertex (Z = 0)
                v_bottom = [x, y, 0]

                # In a real optimized script, we'd use a Delaunay triangulation
                # For simplicity, we'll treat each pixel as a small cube/cell

                # Define the 8 corners of the "pixel box"
                # Bottom face
                p1 = [x, y, 0]
                p2 = [x+1, y, 0]
                p3 = [x+1, y+1, 0]
                p4 = [x, y+1, 0]
                # Top face
                p5 = [x, y, extrusion_height]
                p6 = [x+1, y, extrusion_height]
                p7 = [x+1, y+1, extrusion_height]
                p8 = [x, y+1, extrusion_height]

                # Create the 12 triangles (2 per side) for this pixel's volume
                pixel_faces = [
                    [p1, p2, p3], [p1, p3, p4], # Bottom
                    [p5, p6, p7], [p5, p7, p8], # Top
                    [p1, p2, p6], [p1, p6, p5], # Side 1
                    [p2, p3, p7], [p2, p7, p6], # Side 2
                    [p3, p4, p8], [p3, p8, p7], # Side 3
                    [p4, p1, p5], [p4, p5, p8]  # Side 4
                ]
                faces.extend(pixel_faces)

    # 3. Create the mesh
    faces_np = np.array(faces)
    surface_mesh = mesh.Mesh(np.zeros(faces_np.shape[0], dtype=mesh.Mesh.dtype))

    for i, f in enumerate(faces):
        for j in range(3):
            surface_mesh.vectors[i][j] = faces_np[i][j]

    # 4. Export
    surface_mesh.save(output_filename)
    print(f"Successfully saved {output_filename}")

# Usage
create_stl_from_mask(image_path, output_filename, extrusion_height)
