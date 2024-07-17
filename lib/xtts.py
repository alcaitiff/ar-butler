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
  cfg = {}
  def __init__(self, cfg):
    self.model_object = None
    self.speaker = None
    self.cfg=cfg
    device = cfg.transcriptor.device
    model_path = cfg.tts.model_path
    self.config = XttsConfig()
    self.config.load_json(cfg.tts.config_file_path)
    self.model_object = Xtts.init_from_config(self.config)
    self.model_object.load_checkpoint(self.config, checkpoint_dir=model_path, eval=True)
    self.model_object.to(torch.device(device))

  def predict(self, text):
    lang = self.cfg.transcriptor.language
    out = self.model_object.synthesize(
        text.rstrip('.'),
        config=self.config,
        language=lang,
        speaker_wav=self.cfg.tts.speaker_wav
    )
    torchaudio.save(self.cfg.tts.audio_file, torch.tensor(out["wav"]).unsqueeze(0), 24000)

