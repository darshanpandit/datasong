import numpy as np
import json
import pygame
import os
from time import sleep

class Controller:
  def __init__(self, sample_rate, control_mat, sound_dir):
      self.sample_rate = sample_rate #bps or ups
      self.control_mat = control_mat
      self.media = Audio_media(sound_dir)

  def initiate_playback(self):
    #for each sample
    print(self.control_mat.shape[0])
    for i in range(0,self.control_mat.shape[1]):

        chn_vec = self.control_mat[0:7,i] #gets the ith column
        self.media.play(chn_vec)
        #more media output here
        sleep((60)/self.sample_rate)

  def terminate():
    self.media.close()


class Audio_media:
  """ We assign each sound/note a unique channel, this way multiple samples can be played at the same instance """
  def __init__(self, sound_dir):

    pygame.mixer.pre_init(22050, -16,8, 256)
    pygame.mixer.init()
    self.sound_dir = sound_dir
    #initiate channel vectors
    self.channel_map = {}
    for i in range(8):
      self.channel_map[i] = pygame.mixer.Channel(i)




  def play(self, chn_vec):
    for i in range(0, (len(chn_vec))):
      channel = self.channel_map[i]
      if not channel.get_busy():
        channel.play(self.soundify( i, chn_vec[i]) )

  def soundify(self,channelno, value):
    path = os.path.join(self.sound_dir, (str((8*channelno)%64+1+value)+'.aif'))
    return pygame.mixer.Sound(path)

  def close(self):
    pygame.quit()

#lets create a random matrix for now
row, col = 10, 120
c_mat = np.random.randint(8, size=(row,col))
#print(c_mat[0:8,0] )
#print (c_mat)

sound_dir = "D:\Work\datasong\darshan\Sounds2"
controller = Controller(  60,c_mat, sound_dir)
controller.initiate_playback()






