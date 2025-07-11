from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

AZURE_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

llm = AzureChatOpenAI(
    openai_api_key=AZURE_API_KEY,
    deployment_name=AZURE_DEPLOYMENT,
    azure_endpoint=AZURE_ENDPOINT,
    openai_api_version=AZURE_API_VERSION
)

template = """
You are a helpful college assistant. Answer student queries like admission, fees, faculty, timetable, etc. dont give answer everything else quetions give only collage related quetion answers

Question: {question}
Answer:"""

prompt = PromptTemplate(input_variables=["question"], template=template)

# ✅ Updated LangChain 0.1.17+ style
chain = prompt | llm

def get_response(question: str):
    result = chain.invoke({"question": question})
    return result.content  # ✅ FIX: get only the text!
