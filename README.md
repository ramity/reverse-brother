# Reverse Brother

![Brother 4x4 Hoop Pixel Measurements](docs/4x4_Pixel_Measurements.jpg)

A reverse engineering project for my mom.

# Table of Contents

- [Introduction](#introduction)
- [Process](#process)
  - [4x4 Inner/Outer Pixel Results](#4x4-innerouter-pixel-results)
  - [5x7 Inner/Outer Pixel Results](#5x7-innerouter-pixel-results)

# Introduction

My mom asked for custom inserts for her embroidery machine. This project documents my process of reverse engineering the insert by applying pixel math and computer vision.

# Process

I asked her for a photo of the hoop with a coin for scale. She suggested using her fiskars cutting mat for scale.

![Fiskars Cutting Mat](docs/4x4.jpg)
> 4x4 hoop

![Fiskars Cutting Mat](docs/5x7.jpg)
> 5x7 hoop

I used paint.net to get some pixel measurements and then applied a perspective transformation to the image.

![4x4 Transformed](docs/4x4_transformed.jpg)
> 4x4 perspective transformed

![5x7 Transformed](docs/5x7_transformed.jpg)
> 5x7 perspective transformed

I'd then convert the image to grayscale and applied a canny edge detection.

![4x4 Edges](docs/4x4_edges.jpg)
> 4x4 canny edge detection

![5x7 Edges](docs/5x7_edges.jpg)
> 5x7 canny edge detection

I manaually edited the image to highlight the insert.

![4x4 Segmented](docs/4x4_segmented.jpg)
> 4x4 segmented

![5x7 Segmented](docs/5x7_segmented.jpg)
> 5x7 segmented

Then I computed the outer and inner contours and bounding boxes.

![4x4 Final](docs/4x4_final.jpg)
> 4x4 final

![5x7 Final](docs/5x7_final.jpg)
> 5x7 final

From there I computed the outer and inner width and height.

## 4x4 Inner/Outer Pixel Results

| Name | px | in |
| --- | --- | --- |
| outer_w | 2118 | 6.76 |
| outer_h | 1792 | 5.79 |
| inner_w | 1920 | 6.12 |
| inner_h | 1588 | 5.13 |

## 5x7 Inner/Outer Pixel Results

| Name | px | in |
| --- | --- | --- |
| outer_w | 2107 | 7.08 |
| outer_h | 1754 | 5.93 |
| inner_w | 1857 | 6.24 |
| inner_h | 1501 | 5.07 |
