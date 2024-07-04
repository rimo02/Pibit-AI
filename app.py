import streamlit as st
from main import process


def main():

    with st.sidebar:
        file = st.file_uploader('Upload Your resume Here')
        if st.button("Submit and Process"):
            if file is not None:
                file_content = file.read().decode("utf-8")
                json_answer = process(file_content)
                st.write(json_answer)


if __name__ == "__main__":
    main()
