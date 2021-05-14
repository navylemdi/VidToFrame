#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:40:00 2021

@author: yvan
"""

import cv2
import numpy as np
import os

#Chemin jusqu'a la video choisie
video_path = '/Users/yvan/Desktop/ETS_montreal/Cours/E21/MTR892/Cam_0/MVI_3986.MOV'
video_name = video_path.split("/")[-1]
video_name = video_name.split(".")[0]

suffix = 0
if video_path.split("/")[-2] == 'Cam_0':
    suffix = '_0'
else:
    suffix = '_1'

vidcap = cv2.VideoCapture(video_path)
success, image = vidcap.read()

# Recuperation des propriete de la video
fps = vidcap.get(cv2.CAP_PROP_FPS) # Frame rate
frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) # Nombre de frame
duration = frame_count/fps # Duree totale video (seconde)

print('Video: '+ video_name)
print('FPS = ' + str(fps))
print('Number of frames = ' + str(frame_count))
print('Duration (s) = ' + str(duration))

# Choix Calibration ou Essai
calibration = True #vrai si video de calibration, Faux si video de test traction
if calibration:
    #Time code des changements de position de la plaque de calibration
    #A modifier a chaque video
    liste_timecode = np.array([0, 2, 3, 4, 6, 7, 9, 10, 12, 13, 14, 16, 18, 19,
                               21, 22, 24, 25, 27, 30, 32, 34, 36, 37, 39, 41,
                               42, 43]) #(s)
else:
    #Pour les video d'essai, trouver le time code du debut de l'essai (Top)
    #et de la fin de l'essai (End) et modifier ci-dessous
    TOP_time_code = 4 #(s)
    time_step = 1 #(s)
    END_time_code = 60*2+35 #Ex: la fin est à min:sec alors 60*min+sec #Time code en seconde(s)
    liste_timecode = np.arange(TOP_time_code, END_time_code, time_step)

liste_nbframe = liste_timecode*fps

FrameName = "Calframe" #prefixe nom des images
i = 0
Save_path='/Users/yvan/Desktop/ETS_montreal/Cours/E21/MTR892/Cam_0'
for nbframe in liste_nbframe:
    vidcap.set(1, nbframe)
    ret, frame = vidcap.read()
    cv2.imwrite(os.path.join(Save_path , FrameName + str(i).zfill(4) + suffix + ".png"), frame)
    cv2.waitKey(1)
    i += 1
vidcap.release()
