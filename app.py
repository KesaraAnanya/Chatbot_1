from langchain_openai import ChatOpenAI 
from langchain_core.messages import HumanMessage, SystemMessage 
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model_name = "gpt-3.5-turbo",
                  temperature=0.7)

messages =[
    SystemMessage(content="You are a good helpful assistant.")
]

while True:
    user_input = input("User:")
    
    if user_input.lower() == "bye":
        print("AI Response: Bye! I will be here need any more help.")
        break

    messages.append(HumanMessage(content=user_input))

    response = chat.invoke(messages)

    print("AI Response:",response.content)

messages.append(response)