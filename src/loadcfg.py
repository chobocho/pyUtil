import json

class LoadCfg():
    def __init__(self, filename):
         self.filename = filename

    def load(self):
         with open(self.filename) as cfg_file:
             cfg_data = json.load(cfg_file)
         #print (cfg_data)
         return cfg_data["buttons"]