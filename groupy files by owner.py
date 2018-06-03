# -*- coding: utf-8 -*-
"""
Created on Mon May 21 00:53:59 2018

@author: selem
"""

class FileOwners:

    @staticmethod
    def group_by_owners(files):
        new_list = {}
        for filename,user in files.items():
            if(user in new_list):
                new_list.setdefault(user, []).append(filename)
               # new_list[user] =[new_list[user],filename]
            else:
                #new_list[user] =  filename
                new_list.setdefault(user, []).append(filename)
        return new_list

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))