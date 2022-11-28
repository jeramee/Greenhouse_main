# Path: greenhouse_main\base\write_JSON_dictionary.py
# -*- coding: utf-8 -*-
'''read JSON into a dictionary'''
import json
import sys
from pathlib import Path

'''create Read_JSON_Dictionary class'''
class Read_JSON_Dictionary:

    file_name = ""
    dictionary = {}

    def __init__(self, file_name, dictionary):
        self.file_name = file_name
        self.dictionary = dictionary

    '''write JSON from a dictionary'''
    def write_JSON_dictionary (self):      
        try:
            file_object = open(self.file_name, 'w')
            json.dump(self.dictionary, file_object)
            '''close file_object'''
            file_object.close()            
        except FileNotFoundError:
            print('File not found: ' + self.file_name)
            sys.exit()

    '''read JSON into a dictionary'''
    '''Commenting this out because I would have to pass a file object
    to the function and I know how to do that but I did not want to
    deal with the crashes from not closing the file.
    this is easy to do in main or another function.'''
    '''def read_json_n_dictionary (self):
        try:
            file_object = open(self.file_name, 'r')
            self.dictionary = json.load(file_object.read())            
            file_object.close()
        except FileNotFoundError:
            print('File not found: ' + self.file_name)
            sys.exit()
    '''

