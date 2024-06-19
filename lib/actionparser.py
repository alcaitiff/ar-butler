from lib.actions.learn import Learn
from lib.actions.dump import Dump
class Parser:
  cfg = {}

  def __init__(self, config):
    self.cfg = config

  def first_word(self,str):
    try:
      return str.split()[0]
    except IndexError:
      return ''

  # Function for detect action
  def parse_action(self,msg):
    clean_msg = msg.upper().strip().replace('.', '').replace('!','').replace(',','')
    actions = self.cfg.actions
    if clean_msg in actions.exit.keywords:
      raise ValueError("EXIT")
    if clean_msg in actions.dump.keywords:
      return Dump(self.cfg).do_action(msg)
    first_word=self.first_word(clean_msg)
    if first_word in actions.learn.keywords and len(clean_msg.split())>1:
      return Learn(self.cfg).do_action(msg)
   
    print("User input: "+'\033[32m'+msg+'\033[0m')
