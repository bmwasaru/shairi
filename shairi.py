import os
from datetime import datetime
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('OPEN_API_KEY'))

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant."},
    {"role": "user", "content": "Compose a poem in Kiswahili."}
  ]
)

with open(f'mashairi/{datetime.today().strftime("%d-%m-%y")}.txt', 'w+', encoding="utf-8") as file:
    file.write(completion.choices[0].message.content)
