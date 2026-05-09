from document_loader import load_document
from utils import clean_text, split_text
from vector_store import store_chunks, retrieve
from llm.llm_handler import get_llm_response


def main():

    # DOCUMENT PARSING
    raw_text = load_document("sample.pdf")

    # Clean text
    clean = clean_text(raw_text)

    # Split into chunks
    chunks = split_text(clean)

    # CHUNKING, EMBEDDINGS

    store_chunks(chunks)
    query = "What are compliance risks?"
    relevant_chunks = retrieve(query)

    context = "".join(relevant_chunks)
    response = get_llm_response(context)

    print("Answer:")
    print(response)


if __name__ == "__main__":
    main()
