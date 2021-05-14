# VidToFrame
This code reads a .MOV video and saves frames from this video.  
Change *video_path* to select the video you are working on.  
Change *Save_path* to select the directory you want to save the frames.  
If you are working on a calibration video, put *calibration* boolean at True and write the time code of the frames you want to extract in the list *liste_timecode*.  
If you are working on a test video, write the begining (*TOP_time_code*) and ending (*END_time_code*) time code of the video. Choose a time step (*time_step*) to extract frames.

## Requirements
Make sure you have installed cv2, numpy and os librairies
