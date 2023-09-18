import os
import openai
openai.api_key = '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'


def get_embedding(input):
  response = openai.Embedding.create(
  model="text-embedding-ada-002",
  input=f"{input}"
)
  return response

sentence_with_embeddings = []
for sentence in sentences:
  embedding = get_embedding(sentence)['data'][0]['embedding']
  sentence_with_embeddings.append((sentence, embedding))

