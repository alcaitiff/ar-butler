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
    if clean_msg in self.cfg.exit.keywords:
      return self.cfg.exit.id
    first_word=self.first_word(clean_msg)
    if first_word in self.cfg.learn.keywords and len(clean_msg.split())>1:
      return self.cfg.learn.id
    return False