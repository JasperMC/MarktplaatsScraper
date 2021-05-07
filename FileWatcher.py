import time
import os
from os import path
import json

class FileWatcher:

    def __init__(self):
        self.query_folder = "Queries"
        self.listing_folder = "Listings"

    def getFiles(self):
        files = {}
        for filename in os.listdir(self.query_folder):
            filepath = self.query_folder + '/' + filename
            filename2, extension = os.path.splitext(filepath)
            if extension == ".json":
                with open(self.query_folder + '/' + filename) as json_file:
                    json_data = json.load(json_file)
                    file = {}
                    file['query'] = json_data['query']
                    #print(file['query'])
                    file['query_filepath'] = self.query_folder + '/' + filename
                    file['listing_filepath'] = self.listing_folder + '/' + filename
                    if not path.exists(file['listing_filepath']):
                        with open(file['listing_filepath'],'w+') as new_file:
                            json.dump({},new_file)
                            new_file.close()

                    files[filename] = file
                    json_file.close()
        return files
