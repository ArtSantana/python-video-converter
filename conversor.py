import ffmpeg
from os import remove, listdir

class Conversor:
  def __init__(self):
    pass

  def convertVideos(self, files, format):
    index = 1
    self.clearFolder()
    # Now converting the videos with ffmpeg properly
    for i in files:
      (
        ffmpeg
        .input('./videos/'+i)
        .output('./converted-videos/'+str(index)+format, ar=48000, **{'qscale:v': 0})
        .run()
      )
      index += 1

  def clearFolder(self):
    # Removing the files from folder
    for i in listdir('./converted-videos/'):
      remove('./converted-videos/'+str(i))