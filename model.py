from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

chat = ChatOpenAI(
    model="tiiuae/falcon-180B",
    api_key=os.getenv("AI71_API_KEY"),
    base_url=os.getenv("AI71_BASE_URL"),
    streaming=False,
)


system_prompt = ("You are a health consultant assistant. Your job is to come up with a number of possible causes of symptoms based on the user's description and then provide practical and useful suggestions to relieve the symptoms and effective exercises based on the user's description. Answer as detailed as possible.")

def get_response(user_input):

    response = chat.invoke(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input)
        ]

    )
    return response.content