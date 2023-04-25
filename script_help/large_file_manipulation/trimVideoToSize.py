import os.path as path
from moviepy.video.io.VideoFileClip import VideoFileClip

# This is the STOCK image 
stockFile = "12k HDR 60fps Dolby Vision _ Peak Black.mp4"

# Load the video file
video = VideoFileClip(stockFile)

# Trim the video from x[0] to x[1]
testsize = [255, 600]

hundredsixtyonemb = [155, 600]
hundredthirtyonemb = [255, 600]
hundredthreemb = [10, 380]
ninetytwomb = [10, 350]
ninetyfivemb = [10, 360]
ninetyninemb = [70, 400]
ninetyeightnmb = [75, 400]
ninetysevenmb = [77, 400]

tgtSteven = testsize
trimmed_video = video.subclip(tgtSteven[0], tgtSteven[1])


# Calculate the estimated size of the output clip 
duration = trimmed_video.duration
bitrate = 1000 #in kbps
approx_var_processing = 2.78
output_size_est = int(bitrate * duration / approx_var_processing) #in kb

input("Est. Size: {} kb".format(output_size_est))

# Save the trimmed video to a file
trimmed_video.write_videofile("trimmed_example.mp4")