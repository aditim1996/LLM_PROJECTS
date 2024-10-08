# -*- coding: utf-8 -*-
"""Blog Generation LLM APP using LLAMA 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AZsCvKGiPJjaMTUzixCMByj1_inzlymA
"""

#Importing libs

# !pip install sentence-transformers
# !pip install uvicorn
# !pip install ctransformers
# !pip install fastapi
# !pip install ipykernel
# !pip install langchain
# !pip install python-box
# !pip install streamlit
# !pip install langchain-community

# !pip install -q -U bitsandbytes
# !pip install -q -U git+https://github.com/huggingface/transformers.git
# !pip install -q -U git+https://github.com/huggingface/peft.git
# !pip install -q -U git+https://github.com/huggingface/accelerate.git
# !pip install sentencpiece

# import sentence-transformers
# import uvicorn

from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import streamlit as st

# !pip install -q streamlit

# !huggingface-cli login

# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# model_id = "meta-llama/Llama-2-7b-chat-hf"

# model = AutoModelForCausalLM.from_pretrained(model_id, load_in_4bit=True, device_map="auto")
# tokenizer = AutoTokenizer.from_pretrained(model_id)



from tempfile import template
## Function to get response from my LLAMA2 model
from ctransformers import AutoModelForCausalLM
import textwrap
from huggingface_hub import hf_hub_download
# from llama_cpp import Llama


def getLLamaresponse(input_text,no_words,blog_style):

  ### LLAMA 2 model


    # llm = CTransformers(model='brockportgpt-7b-q8_0.gguf',model_type = 'llama',
    #                   config={'max_new_token':256,

    #                           'temperature':0.01 })



# Load the model
    llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7b-Chat-GGUF",
                                              model_file="llama-2-7b-chat.Q8_0.gguf",
                                              model_type="llama",
                                              )
  ## Promt Template

    template = """
      Write a blog for 
      {blog_style} 
      job profile for a topic 
      {input_text}
      within 
      {no_words} words.
          """
    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                          template=template)

  ##Generate the response from LLAMA 2 model
    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

# UI for app

st.set_page_config(page_title="Generate Blog",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")
input_text = st.text_input('Enter the Blog Topic')


## Creating two more columns for additional 2 fields

col1,col2 = st.columns([5,5]) #size of columns

with col1:
  no_words = st.text_input('Number of words')

with col2:
  blog_style = st.selectbox('Writing the blog for',
   ('Researcher','Data Scientist','Common People'),index=0)

submit = st.button("Generate")

## Final Response

if submit:
  st.write(getLLamaresponse(input_text,no_words,blog_style))

# !npm install localtunnel

# !streamlit run app.py &>/content/logs.txt & curl ipv4.icanhazip.com

# !npx localtunnel --port 8501

