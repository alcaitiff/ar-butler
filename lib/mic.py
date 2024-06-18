import wave
import struct
from array import array
from pvrecorder import PvRecorder

class Mic:
  cfg = {}
  recorder = {}

  def __init__(self, config):
    self.cfg = config
    self.recorder = PvRecorder(frame_length=self.cfg.frame_length, device_index=self.cfg.device_index)

  # Function to list mics
  def list_mics(self):
    for index, device in enumerate(self.recorder.get_available_devices()):
      print(f"[{index}] {device}")

  def is_silence(self, frame):
    snd_data=array('h',frame)
    return max(snd_data) < self.cfg.volume_threshold

  # Function for recording an audio fragment
  def record_chunk(self, frames):
      silence = 0
      try:
        print('\033[91m'+self.cfg.messages.RECORDING+'\033[0m')
        while True:
          frame = self.recorder.read()
          frames.extend(frame)
          silence = silence + 1 if self.is_silence(frame) else 0
          if silence > self.cfg.silence_frames:
            self.recorder.stop()
            break
      finally:
        with wave.open(self.cfg.audio_file, 'w') as f:
          f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
          f.writeframes(struct.pack("h" * len(frames), *frames))

  # Function for detect audio
  def detect_and_record(self):
    frames = []
    print(self.cfg.messages.IDLE)
    self.recorder.start()
    while True:
      frame = self.recorder.read()
      if not self.is_silence(frame):
        break
    frames.extend(frame)
    self.record_chunk(frames)
