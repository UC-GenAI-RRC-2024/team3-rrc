from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = 'your_openAI_API'
chat = OpenAI(temperature=0)
#
conversation = ConversationChain(
    llm=chat, 
    verbose=True,
    memory=ConversationBufferMemory()
)
