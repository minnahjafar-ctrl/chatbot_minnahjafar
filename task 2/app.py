import streamlit as st
from rag import ask_rag
import os
import shutil

st.set_page_config(
    page_title="QueryPDF AI",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0E1117;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161B22;
    border-right: 1px solid #30363D;
}

/* Title */
h1 {
    color: white;
    font-weight: 700;
}

/* Input box */
.stTextInput input {

    background-color: #1E1E1E;

    color: white;

    border-radius: 12px;

    border: 1px solid #444;

    padding: 12px;
}

/* Buttons */
.stButton button {

    background-color: #7C4DFF;

    color: white;

    border-radius: 12px;

    border: none;

    padding: 10px 20px;

    font-weight: 600;
}

.stButton button:hover {

    background-color: #9B6DFF;
}

[data-testid="stSidebar"] {
    background-color: #0f172a;
}

[data-testid="stSidebar"] * {
    color: white;
}
/* User message */
.user-message {

    background-color: #7C4DFF;

    color: white;

    padding: 14px;

    border-radius: 18px;

    margin-bottom: 12px;

    margin-left: 30%;

    text-align: right;

    box-shadow: 0px 2px 10px rgba(0,0,0,0.2);
}

/* AI message */
.assistant-message {

    background-color: #1C1F26;

    color: white;

    padding: 16px;

    border-radius: 18px;

    margin-bottom: 15px;

    margin-right: 30%;

    border: 1px solid #30363D;

    box-shadow: 0px 2px 10px rgba(0,0,0,0.15);

    line-height: 1.7;
}

/* Source chunk boxes */
.source-box {

    background-color: #161B22;

    padding: 15px;

    border-radius: 14px;

    border-left: 4px solid #7C4DFF;

    margin-bottom: 12px;

    color: white;
}

</style>
""", unsafe_allow_html=True)

st.title(" 🤖 QueryPDF AI",text_alignment="center")

# st.sidebar.title("📄 Upload PDF")

# uploaded_files = st.sidebar.file_uploader(
#     "Upload PDF files",
#     type=["pdf"],
#     accept_multiple_files=True
# )

# if uploaded_files:

#     st.sidebar.subheader("Uploaded Files")

#     for file in uploaded_files:

#         st.sidebar.write(file.name)



# os.makedirs("pdfs", exist_ok=True)

# if uploaded_files:

#     for file in uploaded_files:

#         save_path = os.path.join(
#             "pdfs",
#             file.name
#         )

#         with open(save_path, "wb") as f:

#             f.write(file.read())


# if uploaded_files and not os.path.exists("chroma_db"):

#     # create db here

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []


# SHOW CHAT HISTORY FIRST
for message in st.session_state.chat_history:

    if message["role"] == "user":

        st.markdown(
            f'''
            <div class="user-message">
                {message["content"]}
            </div>
            ''',
            unsafe_allow_html=True
        )

    elif message["role"] == "assistant":

        st.markdown(
            f'''
            <div class="assistant-message">
                {message["content"]}
            </div>
            ''',
            unsafe_allow_html=True
        )
    else:

        with st.expander("View Source Chunks"):

            for doc in message["content"]:

                st.markdown(
                    f'<div class="source-box">{doc.page_content}</div>',
                    unsafe_allow_html=True
                )


# INPUT BOX BELOW CHAT
query = st.text_input("Ask a question")


# BUTTON
if st.button("Submit"):

    answer, retrieved_docs = ask_rag(
        query,
        st.session_state.chat_history
    )

    st.session_state.chat_history.append({
        "role": "user",
        "content": query
    })

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": answer
    })

    st.session_state.chat_history.append({
        "role": "retrieved_docs",
        "content": retrieved_docs
    })

    # DISPLAY NEWEST USER MESSAGE
    st.markdown(
        f'''
        <div class="user-message">
            {query}
        </div>
        ''',
        unsafe_allow_html=True
    )

    # DISPLAY NEWEST AI MESSAGE
    st.markdown(
        f'''
        <div class="assistant-message">
            {answer}
        </div>
        ''',
        unsafe_allow_html=True
    )

    
    st.rerun()