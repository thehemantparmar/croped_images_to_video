import os
os.system("ffmpeg -f image2 -r 1/2 -i crop/flower%01d.png -i audio1.mp3 -c:a aac -vcodec mpeg4 -y videos/flowers.mp4")