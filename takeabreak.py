# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:16:16 2018

@author: selem
"""
import webbrowser    
import time
import datetime 
import ctypes  # An included library with Python install.   



while datetime.datetime.now().hour < 17:
    time.sleep(60*60) #sleep for 60sec * 60min = 1 hour
    ctypes.windll.user32.MessageBoxW(0, "Please take a break NOW", "Notice", 1) #popup message to tell me to stop working
    webbrowser.open('https://www.youtube.com/watch?v=hM5lO2PWnGk',new=2)

