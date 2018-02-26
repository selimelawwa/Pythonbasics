# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:57:48 2018

@author: selem
"""
import urllib

def read_text(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content
    
#check if text contain insults
def check_profanity(text_file):
    text_content = read_text(text_file)
    encoded_text = urllib.parse.quote(text_content, 'utf-8')
    link = "http://www.wdylike.appspot.com/?q=" + encoded_text
    connection = urllib.request.urlopen(link)
    answer = connection.read()
    #decode utf-8 to remove the 'b' that comes with connection data
    if answer.decode("utf-8", "ignore") == 'true':
        print("WARNING! There are unappropriate words")
    else:
        print("Text is fine")
    connection.close()
    
check_profanity('text_to_check.txt')

