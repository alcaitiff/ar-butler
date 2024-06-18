import whisperx

class Transcriptor:
  cfg = {}
  model = {}

  def __init__(self, config):
    self.cfg = config
    self.model = whisperx.load_model(self.cfg.model_name, self.cfg.device, compute_type=self.cfg.compute_type,language=self.cfg.language)

  # Function for transcribe
  def transcribe(self,file_path):
    print("Transcribing...")
    audio = whisperx.load_audio(file_path)
    result = self.model.transcribe(audio, batch_size=self.cfg.batch_size)
    msg = ''
    for segment in result["segments"]:
      msg +=segment["text"]
    return msg.strip()