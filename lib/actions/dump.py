class Dump:
  cfg = {}

  def __init__(self, config):
    self.cfg = config

  # Function for detect action
  def do_action(self,msg):
    print("DUMPING MEMORY: ("+msg+")")
    with open(self.cfg.memory.text_file_path, "r") as myfile:
      print(myfile.read())