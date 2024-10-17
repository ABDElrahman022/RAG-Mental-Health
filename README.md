# RAG Mental Health ChatBot

This project is a **Retrieval-Augmented Generation (RAG)**-based chatbot designed to assist in mental health-related conversations. The chatbot interacts with users, collects information about their mental health, and generates helpful responses. Once enough symptoms are collected, the chatbot provides a summary that could aid doctors in diagnosis. It is built using **LangChain**, **Pinecone**, **HuggingFace embeddings**, and the **Streamlit** framework for the frontend interface.

## Project Structure

- **main.py**: Contains the backend logic for loading documents, embedding them using HuggingFace, and initializing the Pinecone vector store.
- **frontend.py**: Implements the frontend interface using Streamlit, allowing users to interact with the chatbot.
- **requirements.txt**: Lists the dependencies required for this project.

## Features

- **Mental Health Focused**: The chatbot restricts conversations to mental health topics, collecting symptoms and generating responses accordingly.
- **Symptom Collection**: Once the chatbot has collected sufficient symptoms, it presents them for review.
- **RAG Pipeline**: Uses document retrieval and generation to provide contextually relevant responses.

## Requirements

To run this project, you'll need the following dependencies:

```bash
pinecone-client==2.2.4
streamlit==1.29.0
langchain==0.1.6
langchain-community==0.0.19
langchain-core==0.1.23
python-dotenv==1.0.1
sentence-transformers==3.2.0
```
## Installation


1. **Clone the repository**:

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/ABDElrahman022/rag-mental-health-chatbot.git
   cd rag-mental-health-chatbot
   ```
2. **Install dependencies**:

    Ensure you have Python installed. Then, install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:

    Create a `.env` file in the root directory and add your `Pinecone` and `HuggingFace API keys`:
   ```bash
    PINECONE_API_KEY = your-pinecone-api-key
    HF_KEY_API = your-huggingface-api-key
    ```
4. **Prepare the document for retrieval**:

    Make sure the document the chatbot will use for retrieval is available at the path specified in `main.py`. By default, this path is set to:

    ```bash
    r"C:\Users\RAG real state\real-estate-chatbot-modified.txt"
    ```
    Update this path to point to your own document, if needed.

## Usage
1. **Run the backend**:

    The backend logic is located in `main.py`. It handles document loading, embedding, and setting up Pinecone for document retrieval.

    You can modify the chatbot’s behavior by adjusting the `PromptTemplate` and other parameters in `main.py`.

2. **Run the frontend**:

    Start the Streamlit app by running:

    ```bash
    streamlit run frontend.py
    ```
3. **Chat with the bot**:


    Once the Streamlit app is up and running, you'll be able to interact with the chatbot. It will guide you through a conversation focused on mental health, collecting symptoms and generating responses. After collecting enough data, the bot will present a summary of symptoms.

## Customization
- **Document Loading**: Modify the `TextLoader` in `main.py` to change the document source.
- **Model Customization**: You can switch models by modifying the `repo_id` in `main.py` under the `HuggingFaceHub` initialization.
- **Prompt Adjustments**: Customize the conversation flow by altering the `PromptTemplate` as needed.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
