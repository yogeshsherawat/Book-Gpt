import openai

openai.api_key = 'sk-....'


class EmbeddingManager(object):
    @staticmethod
    def generage_emedding_for_text(text):
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=f"{text}"
        )
        return response['data'][0]['embedding']
