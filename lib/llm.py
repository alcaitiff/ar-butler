from langchain_community.llms import LlamaCpp
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class LLM:
  llm_cpp = {}
  cfg = {}
  prompt = {}
  llm_chain = {}
  def __init__(self, config):
    self.cfg=config
    self.llm_cpp = LlamaCpp(
      model_path=self.cfg.llm.model_path,
      n_gpu_layers=self.cfg.llm.n_gpu_layers,
      n_batch=self.cfg.llm.n_batch,
      n_ctx=self.cfg.llm.n_ctx,
      f16_kv=True,
      verbose=False,
      max_tokens=300,
      cache=False
    )
  def invoke(self, query, context):
    return self.llm_cpp.invoke(self.cfg.llm.search_prompt.format(question=query,context=context))