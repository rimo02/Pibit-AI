from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import os
import json

os.environ["OPENAI_API_KEY"] = "YOUR-OPENAI-KEY"
model_name = "gpt-3.5-turbo"
llm = ChatOpenAI(model_name=model_name)


def process(text):
    template = """
        You are an AI assistant. Your task is to parse the given resume below and parse it into a JSON structure.
        The JSON format should contain the following :
        1. Personal Information - Include Name, Email, LinkedIn, 
        2. Educational Information - Include university name, gpa, courses studied, graduation date and any other curricular activies associated with it
        3. Professional Information - Include Job Title, Company Name, Years of Experience, Starting and Ending Date , and the projects you worked on. 
        4. Skills : Highlight out the important technical skills and soft skills (if any) [should be a list ] 
        5. Projects : Project Title, Description, Link (if any available)

        Format the json properly ensuring proper readability. 
        Here's the resume : {resume}
        """
    prompt = PromptTemplate(template=template, input_variables=["resume"])
    chain = LLMChain(llm=llm, prompt=prompt)

    inputs = {
        "resume": text,
    }
    result = chain.run(inputs)
    if result:
        return json.dumps(result, indent=2)
    else:
        return "We are unable to process your request"
