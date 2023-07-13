import os
import streamlit as st

from Data_train import My_own_gpt  # import the My_own_gpt function from the Data_train module

models = [  # create a list of available GPT models
    "gpt-3.5-turbo-16k-0613",
    "gpt-3.5-turbo",
    "text-davinci-003",
    "davinci",
    "babbage",
    "ada",
    "curie",
    "text-davinci-001",
    "ZeyadAhmed/AraElectra-Arabic-SQuADv2-QA",
]

# set the API key and other parameters for accessing the OpenAI API
API = ""
api_key = ""
env = ""
index_name = ""

def main():
    # set the page title and display a header
    st.set_page_config(page_title="تدريب بياناتك  📝📗")
    st.header("ادخل البيانات  📝📗")
    
    # allow users to upload PDF documents
    pdf_docs = st.file_uploader(
        "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
    
    # when the "Process" button is pressed, train the GPT model on the uploaded PDFs
    if st.button("Process"):
        with st.spinner("Processing"):
            My_own_gpt(pdf_docs, models[0], API, api_key, env, index_name)
            st.text(" 🎩🏆تم التدريب بنجاح")

if __name__ == "__main__":
    main()  # call the main function when the script is executed
