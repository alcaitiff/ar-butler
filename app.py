if __name__ == '__main__':
  from lib.mic import Mic
  from lib.rag import Rag
  from lib.configloader import ConfigLoader
  from lib.transcriptor import Transcriptor
  from lib.actionparser import Parser
  from lib.xtts import XTTS
  from lib.player import Player
  from lib.llm import LLM
  def main():
    cfg = ConfigLoader().get_config()
    mic = Mic(cfg.mic)
    rag = Rag(cfg)
    parser = Parser(cfg)
    transcriptor = Transcriptor(cfg.transcriptor)
    llm = LLM(cfg)
    xtts = XTTS(cfg)
    player = Player()

    try:
      while True:
        mic.detect_and_record()
        msg=transcriptor.transcribe(cfg.mic.audio_file)
        if len(msg) > 0:
          parser.parse_action(msg,mic,transcriptor,rag,xtts,player,llm)
    except KeyboardInterrupt:
      print('Keyboard Interruption')
    except ValueError:  
      print('Command Interruption')
    print('bye')

  main()
