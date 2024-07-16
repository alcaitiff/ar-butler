from lib.mic import Mic
from lib.rag import Rag
from lib.configloader import ConfigLoader
from lib.transcriptor import Transcriptor
from lib.actionparser import Parser

def main():
  cfg = ConfigLoader().get_config()
  transcriptor = Transcriptor(cfg.transcriptor)
  mic = Mic(cfg.mic)
  parser = Parser(cfg)
  rag = Rag(cfg)
  try:
    while True:
      mic.detect_and_record()
      msg=transcriptor.transcribe(cfg.mic.audio_file)
      parser.parse_action(msg,mic,transcriptor,rag)
  except KeyboardInterrupt:
    print('Keyboard Interruption')
  except ValueError:  
    print('Command Interruption')
  print('bye')

main()
