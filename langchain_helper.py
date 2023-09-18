from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_name(letter):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['letter'],
        template="I need a name starts from this {letter}. Suggest me some fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="name")

    # # Chain 2: Menu Items
    # prompt_template_items = PromptTemplate(
    #     input_variables=['restaurant_name'],
    #     template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated string"""
    # )

    # food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain],
        input_variables=['letter'],
        output_variables=['name']
    )

    response = chain({'letter': letter})

    return response

if __name__ == "__main__":
    print(generate_name("A"))
