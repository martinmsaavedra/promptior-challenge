# from dotenv import load_dotenv
import json, os
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# import sys

# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.join(current_dir, '..')
# sys.path.append(parent_dir)

# load_dotenv()

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# if not os.path.exists('chat-flask/data/services_data.json') or not os.path.exists('chat-flask/data/about_data.json'):
#     from web_scrapper.web_scrapping import extraer_datos_servicios, extraer_datos_sobre_nosotros
#     extraer_datos_servicios()
#     extraer_datos_sobre_nosotros()
    

services_data = load_data('data/services_data.json')
about_data = load_data('data/about_data.json')
openai_key =os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(api_key=openai_key,temperature=0, model_name='gpt-3.5-turbo')

def process_question_with_langchain(question):
    prompt_text = generate_summary_prompt(services_data, about_data) + f" Question: {question}."
    prompt_template = PromptTemplate(input_variables=["question"], template=prompt_text)
    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.invoke({"question": question})
    return response['text'] if 'text' in response else "Lo siento, no pude generar una respuesta adecuada."

def generate_summary_prompt(services_data, about_data):
    services_info = " ".join(services_data)
    about_info = " ".join(about_data)
    prompt_text = f"Services: {services_info} About: {about_info}"
    return prompt_text


if __name__ == '__main__':
    question = "¿En qué año se fundó Promptior?"
    print(process_question_with_langchain(question))
