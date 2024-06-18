import json
from types import SimpleNamespace


class ConfigLoader:
  cfg = {}

  def __init__(self, config_file_path="config.json"):
    self.cfg = self.load_config(config_file_path)

  # Function to load config
  def load_config(self, config_file_path):
    with open (config_file_path) as json_data:
      cfg = json.loads(json_data.read(),object_hook=lambda d: SimpleNamespace(**d))
    return cfg    
  
  def get_config(self):
    return self.cfg