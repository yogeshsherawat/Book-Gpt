import openai

openai.api_key = 'sk-....'


class ChatManager(object):
    @staticmethod
    def get_reply_to_query_with_content(query, content):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": content
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['message']['content']