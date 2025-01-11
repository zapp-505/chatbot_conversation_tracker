
from groq import Groq

client = Groq(
    api_key="your-api-key",
)

conversation_history = []
def talk(query):
    conversation_history.append({
        "role": "user", 
        "content": query
    })
    
    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        model="llama-3.1-8b-instant",
    )
    bot_response = chat_completion.choices[0].message.content
    
    conversation_history.append({
        "role": "assistant", 
        "content": bot_response
    })

    print("Bot: ", chat_completion.choices[0].message.content)


while True:
    query = input("USER_: ")
    if query == "exit":
        break
    else:
        talk(query)