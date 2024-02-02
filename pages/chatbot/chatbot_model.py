from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = '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'
chat = OpenAI(temperature=0)
#
conversation = ConversationChain(
    llm=chat, 
    verbose=True,
    memory=ConversationBufferMemory()
)
