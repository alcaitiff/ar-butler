class Dump:
  cfg = {}

  def __init__(self, config):
    self.cfg = config

  def do_action(self):
    print("DUMPING MEMORY:")
    with open(self.cfg.memory.text_file_path, "r") as file:
      for i, line in enumerate(file):
        print('\033[92m '+str(i)+'\033[0m: '+line.strip())