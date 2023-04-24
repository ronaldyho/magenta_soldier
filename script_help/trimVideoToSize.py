import os.path as path
from moviepy.video.io.VideoFileClip import VideoFileClip

# This is the STOCK image 
stockFile = "12k HDR 60fps Dolby Vision _ Peak Black.mp4"

# Load the video file
video = VideoFileClip(stockFile)

# Trim the video from x[0] to x[1]
hundredthreemb = [10, 380]
ninetytwomb = [10, 350]
ninetyfivemb = [10, 360]
ninetyninemb = [70, 400]
ninetyeightnmb = [75, 400]
ninetysevenmb = [77, 400]

tgtSteven = ninetysevenmb
trimmed_video = video.subclip(tgtSteven[0], tgtSteven[1])

# Save the trimmed video to a file
trimmed_video.write_videofile("trimmed_example.mp4")