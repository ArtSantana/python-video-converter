# In this file we have the handle
# for all menu actions that the user
# can have

import os
from os import listdir
from conversor import Conversor
from video import Video

VIDEOS_LIST = listdir('./videos')
FORMATS = ['.avi', '.mp4', '.MXF', '.mov', '.mkv', '.wmv']
arrayVideos = []
Converter = Conversor()

def clearScreen():
  os.system('cls' if os.name == 'nt' else 'clear')

def menu():
  while True:
    indexVideos = 1
    clearScreen()
    print('Selected videos: ', arrayVideos)
    print('Videos available for conversion')
    for i in VIDEOS_LIST:
      print(str(indexVideos) + ' -', i)
      indexVideos += 1
    print('\nFor close the program digit \'exit\'\n')
    print('Enter 0 to edit your videos')
    print('Enter \'all\' to add all videos at once')
    print('Enter the index of each video that you want work with: ', end='')
    handleInput(input())
    

def handleInput(keyInput):
  if keyInput == 'exit':
    clearScreen()
    print('Bye, see you next time')
    exit()
  elif keyInput == '0':
    optionsFfmpeg()
  elif keyInput == 'all':
    convertAll()
    del VIDEOS_LIST[:]
  else:
    try:
      # Here we will append the video in the array and
      # after that removing him from the available list
      arrayVideos.append(VIDEOS_LIST[int(keyInput) - 1])
      VIDEOS_LIST.remove(VIDEOS_LIST[int(keyInput) - 1])
    except ValueError:
      pass
    except IndexError:
      print('This index is not available')
      print('Press enter to continue...')
      input()
      pass

def optionsFfmpeg():
  clearScreen()
  print('1- Convert videos')
  options = input()
  if options == '1':
    print('Formats:\n1- .avi\t\t2- .mp4\t\t3- .mxf')
    print('4- .mov\t\t5- .mkv\t\t6- .wmv')
    format = int(input())
    Videos = Video(arrayVideos)
    Converter.convertVideos(Videos.getFiles(), FORMATS[format-1])

def convertAll():
  for i in VIDEOS_LIST:
    print(i)
    arrayVideos.append(i)