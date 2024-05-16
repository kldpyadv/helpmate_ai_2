from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
import os
import openai
from dotenv import load_dotenv
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core import VectorStoreIndex
from IPython.display import display, HTML
from llama_index.core import SimpleDirectoryReader

load_dotenv()
openai.api_key = os.getenv('OPEN_AI_KEY')

def process_document(pdf_path):
    #Create object of SimpleDirectoryReader
    reader = SimpleDirectoryReader(input_dir=pdf_path)
    documents = reader.load_data()
    return create_queryengine(documents)


def create_queryengine(documents):
    parser = SimpleNodeParser.from_defaults()
    nodes = parser.get_nodes_from_documents(documents)
    index = VectorStoreIndex(nodes)
    query_engine = index.as_query_engine()
    return query_engine

#Query Reponse Function
def query_response(user_input, query_engine):
    response = query_engine.query(user_input)
    file_name = response.source_nodes[0].node.metadata['file_name'] + "page no" + response.source_nodes[0].node.metadata['page_label']
    final_reponse = response.response + '\n <br>Check further at ' + file_name
    return final_reponse

#dir(response)
#reponse.source_nodes[0].score for score or percentage of correctness
#response.source_nodes[0].node.text for the text where information was found




