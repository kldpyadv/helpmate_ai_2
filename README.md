AI Mr Helpmate 2.0 - Insurance Document Chatbot

Kindly put OPENAI key in .env file or directly in functions.py file

AI Mr Helpmate 2.0 is an AI-powered chatbot designed to assist users in querying insurance documents. By leveraging LlamaIndex for document indexing and a GPT model for natural language understanding, this chatbot provides accurate answers drawn directly from indexed insurance documentation.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
python
llama-index
docx2txt
pypdf
openai
flask

File Descriptions

app.py
This Flask application handles routing and server-side logic:

default_func(): Initializes document processing in a background thread and renders the main chat interface.
process_documents_background(pdf_path): Background thread function that processes documents located at the specified path.
check_processing(): API endpoint to check the status of document processing.
getresponse(): Processes user input, queries the indexed documents, and returns the response.
end_conv(): Redirects to the default function to restart the conversation.

functions.py
Contains functions for processing insurance documents and querying them:

process_document(pdf_path): Reads and processes documents from the specified directory.
create_queryengine(documents): Creates a query engine from the processed documents.
query_response(user_input, query_engine): Retrieves responses based on the user's query using the LlamaIndex query engine.

JavaScript Functions
The JavaScript code manages client-side interactions and asynchronous requests.

checkProcessingStatus: Periodically checks if the server has processed the input and updates the chat interface accordingly.
appendUserMessage: Inserts the user's message into the chat area.
appendBotMessage: Inserts the bot's response into the chat area.
clearChatHistory: Clears the chat history and resets the chat interface.


Deployment
To deploy this on a live system, consider using platforms like Heroku, AWS, or GCP depending on your requirements.