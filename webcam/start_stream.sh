#!/bin/sh
echo "Start stream."
VIDEO_DEVICE="/dev/video1"
echo "Starting stream with device: $VIDEO_DEVICE"

/opt/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer \
  -i "input_uvc.so -d $VIDEO_DEVICE -r 640x480 -f 30" \
  -o "output_http.so -w ./www -p 8082"
