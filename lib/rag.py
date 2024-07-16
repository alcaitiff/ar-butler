from sentence_transformers import SentenceTransformer
import torch
import os
# Retrieval-Augmented Generation
class Rag:
  cfg = {}
  embedder = {}
  embeddings = {}

  def __init__(self, config):
    self.cfg = config
    self.embedder = SentenceTransformer(config.rag.embedder_name)
    if os.path.isfile(self.cfg.rag.embeddings_file_path) and os.access(self.cfg.rag.embeddings_file_path,os.R_OK):
      self.embeddings = torch.load(self.cfg.rag.embeddings_file_path)
    else:
      self.encode(self.cfg.memory.text_file_path)      

  def encode(self,file_name):
    with open(file_name, "r") as data_file:
      data = data_file.readlines()
      self.embeddings_size = len(data)
    self.embeddings = self.embedder.encode(data, convert_to_tensor=True)
    torch.save(self.embeddings,self.cfg.rag.embeddings_file_path)

  def retrieve(self,query):
    result = []
    query_embedding = self.embedder.encode(query, convert_to_tensor=True)
    with open(self.cfg.memory.text_file_path, "r") as data_file:
      data = data_file.readlines()
      top_k = min(5,len(data))
      # We use cosine-similarity and torch.topk to find the highest 5 scores
      similarity_scores = self.embedder.similarity(query_embedding, self.embeddings)[0]
      scores, indices = torch.topk(similarity_scores, k=top_k)

      #print("\nQuery:", query)
      #print("Top "+str(top_k)+" most similar sentences in corpus:")
      for score, idx in zip(scores, indices):
        #print(data[idx], f"(Score: {score:.4f})")
        result.append(data[idx])
      return result  