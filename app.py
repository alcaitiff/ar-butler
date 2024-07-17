if __name__ == '__main__':
  import logging
  import time
  from lib.mic import Mic
  from lib.rag import Rag
  from lib.configloader import ConfigLoader
  from lib.transcriptor import Transcriptor
  from lib.actionparser import Parser
  from lib.xtts import XTTS
  from lib.player import Player

  def main():
    cfg = ConfigLoader().get_config()
    mic = Mic(cfg.mic)
    logging.basicConfig(level=logging.INFO)
    rag = Rag(cfg)
    parser = Parser(cfg)
    transcriptor = Transcriptor(cfg.transcriptor)
    xtts = XTTS()
    player = Player()

    try:
      while True:
        mic.detect_and_record()
        msg=transcriptor.transcribe(cfg.mic.audio_file)
        parser.parse_action(msg,mic,transcriptor,rag,xtts,player)
    except KeyboardInterrupt:
      print('Keyboard Interruption')
    except ValueError:  
      print('Command Interruption')
    print('bye')

  main()
