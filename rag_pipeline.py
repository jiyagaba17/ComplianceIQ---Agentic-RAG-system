from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from llm.llm_handler import get_llm_response


def run_pipeline():
    # Load PDF
    loader = PyPDFLoader("sample-local-pdf.pdf")
    documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    # Create embeddings
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Store in vector DB
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    # Create retriever
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    # Query
    query = "What are compliance risks?"

    docs = retriever.invoke(query)

    # Combine retrieved content
    context = " ".join([doc.page_content for doc in docs])

    # Get LLM response
    response = get_llm_response(context)

    print("\n🔹 Final Answer:\n")
    print(response)


if __name__ == "__main__":
    run_pipeline()
