FROM python:3.14-slim-bookworm

WORKDIR /app

RUN apt update
RUN apt upgrade -y

# Helper tool for querying installed libraries.
RUN apt install -y pkg-config

# Install python libraries
RUN pip install numpy
RUN pip install pillow
# RUN pip install torch torchvision
RUN pip install tqdm
# RUN pip install scikit-image
RUN pip install numpy-stl

# OpenCV dependencies
RUN apt install -y cmake g++ wget zip unzip
RUN apt install -y ffmpeg libavcodec-dev libavformat-dev libavutil-dev libswscale-dev libx264-dev

# Download OpenCV code
RUN mkdir /root/opencv
RUN wget -O /root/opencv/opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
RUN wget -O /root/opencv/opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip
RUN unzip /root/opencv/opencv.zip -d /root/opencv/
RUN unzip /root/opencv/opencv_contrib.zip -d /root/opencv/
RUN mkdir /root/opencv/build

# Configure OpenCV
RUN cd /root/opencv/build && cmake -DWITH_FFMPEG=1 -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x

# Build and install OpenCV
RUN cd /root/opencv/build && make -j$(nproc)
RUN cd /root/opencv/build && make install

# RUN pip install open3d
RUN pip install matplotlib

ENTRYPOINT sleep infinity
