import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY");

while(True):
    text = input("Tú: ")
    
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Trolete is a chatbot in spanish that reluctantly answers questions with sarcastic responses:\nYou: " + text,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    
    print(response.choices[0].text);