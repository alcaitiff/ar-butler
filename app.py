from mic import Mic
from configloader import ConfigLoader
from transcriptor import Transcriptor
from actionparser import Parser

def main():
  cfg = ConfigLoader().get_config()
  transcriptor = Transcriptor(cfg.transcriptor)
  mic = Mic(cfg.mic)
  parser = Parser(cfg.actions)
  try:
    while True:
      mic.detect_and_record()
      msg=transcriptor.transcribe(cfg.mic.audio_file)
      action = parser.parse_action(msg)
      match action:
        case cfg.actions.exit.id:
          break
        case cfg.actions.learn.id:
          print("LEARNING: "+'\033[33m'+msg.split(' ',1)[1]+'\033[0m')
        case _:
          print("User input: "+'\033[32m'+msg+'\033[0m')
  except KeyboardInterrupt:
    print('Keyboard Interruption')
  print('bye')

main()
