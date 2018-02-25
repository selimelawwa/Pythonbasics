# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:19:59 2018

@author: selem
"""

import os


directory  = r"C:\Users\selem\Desktop\test"
ourfiles  = os.listdir(directory)
#here we change current working directory of prgoram to be folder which has the photos to be renamed
os.chdir(directory)

#print all files in directory 
print(ourfiles)

#for loop over all files in our directory and renaming them 
for file in ourfiles:
    print('oldfilename is : ',file)
    newfilename = ''.join([i for i in file if not i.isdigit()])
    #to handle if 2 or more files have same name will add 'x' at end of file 
    while os.path.exists(newfilename):
         newfilename = newfilename[:len(newfilename)-4] + 'x.txt'
    os.rename(file,newfilename)
    print('new file name is : ',newfilename)

