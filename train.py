import cv2 as cv
import os



# importing libraries
import cv2
import numpy as np

# Create a VideoCapture object and read from input file
os.listdir('labeled')
vf_path = 'labeled/0.hevc'
cap = cv2.VideoCapture(vf_path)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video  file")

# Read until video is completed
while cap.isOpened():

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
# ##%
# import cv2
# import numpy as np
# import subprocess as sp
# import shlex
#
# width, height, n_frames, fps = 1344, 756, 50, 25  # 50 frames, resolution 1344x756, and 25 fps
#
# output_filename = 'output.mp4'
#
# # Open ffmpeg application as sub-process
# # FFmpeg input PIPE: RAW images in BGR color format
# # FFmpeg output MP4 file encoded with HEVC codec.
# # Arguments list:
# # -y                   Overwrite output file without asking
# # -s {width}x{height}  Input resolution width x height (1344x756)
# # -pixel_format bgr24  Input frame color format is BGR with 8 bits per color component
# # -f rawvideo          Input format: raw video
# # -r {fps}             Frame rate: fps (25fps)
# # -i pipe:             ffmpeg input is a PIPE
# # -vcodec libx265      Video codec: H.265 (HEVC)
# # -pix_fmt yuv420p     Output video color space YUV420 (saving space compared to YUV444)
# # -crf 24              Constant quality encoding (lower value for higher quality and larger output file).
# # {output_filename}    Output file name: output_filename (output.mp4)
# process = sp.Popen(shlex.split(f'ffmpeg -y -s {width}x{height} -pixel_format bgr24 -f rawvideo -r {fps} -i pipe: -vcodec libx265 -pix_fmt yuv420p -crf 24 {output_filename}'), stdin=sp.PIPE)
#
# # Build synthetic video frames and write them to ffmpeg input stream.
# for i in range(n_frames):
#     # Build synthetic image for testing ("render" a video frame).
#     img = np.full((height, width, 3), 60, np.uint8)
#     cv2.putText(img, str(i+1), (width//2-100*len(str(i+1)), height//2+100), cv2.FONT_HERSHEY_DUPLEX, 10, (255, 30, 30), 20)  # Blue number
#
#     # Write raw video frame to input stream of ffmpeg sub-process.
#     process.stdin.write(img.tobytes())