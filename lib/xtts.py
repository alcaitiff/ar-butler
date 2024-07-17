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
  gpt_cond_latent = {}
  speaker_embedding = {}
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
    self.gpt_cond_latent, self.speaker_embedding = self.model_object.get_conditioning_latents(audio_path=[self.cfg.tts.speaker_wav])

  def predict(self, text):
    lang = self.cfg.transcriptor.language
    text = " \n".join(text.split('. '))
    out = self.model_object.inference(
        text=text,
        language=lang,
        gpt_cond_latent=self.gpt_cond_latent, 
        speaker_embedding=self.speaker_embedding,
        temperature=0.7,
        enable_text_splitting=True,
        speed=1.5
    )
    torchaudio.save(self.cfg.tts.audio_file, torch.tensor(out["wav"]).unsqueeze(0), 24000)
