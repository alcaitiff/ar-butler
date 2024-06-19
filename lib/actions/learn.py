class Learn:
  cfg = {}

  def __init__(self, config):
    self.cfg = config

  # Function for detect action
  def do_action(self,msg):
    data=msg.split(' ',1)[1]
    print("LEARNING: "+'\033[33m'+data+'\033[0m')
    with open(self.cfg.memory.text_file_path, "a") as myfile:
      myfile.write(data+"\n")