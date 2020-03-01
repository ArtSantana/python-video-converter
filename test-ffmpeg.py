import ffmpeg
import os
from os import listdir

index = 1
for i in listdir('./videos'):
  print(str(index)+'.avi')
  (
   ffmpeg
   .input('./videos/'+i)
   .output('./'+str(index)+'.avi')
   .run()
  )
  index += 1