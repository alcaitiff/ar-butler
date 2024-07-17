from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
from TTS.utils.generic_utils import get_user_data_dir
import torch
import numpy as np
import torchaudio

class XTTS:
  speaker = {}
  model_object= {}
  config = {}

  def __init__(self, **kwargs):
    self.model_object = None
    self.speaker = None
    device = "cuda"
    model_path = "assets/xtts/"
    self.config = XttsConfig()
    self.config.load_json("assets/xtts/config.json")
    self.model_object = Xtts.init_from_config(self.config)
    self.model_object.load_checkpoint(self.config, checkpoint_dir=model_path, eval=True)
    self.model_object.to(device)
    self.model_object.cuda()

  def predict(self, text):
    lang = "en"
    out = self.model_object.synthesize(
        text,
        config=self.config,
        language=lang,
        speaker_wav="assets/speakers/Emma.wav"
    )
    torchaudio.save("xtts.wav", torch.tensor(out["wav"]).unsqueeze(0), 24000)

