from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_chunk_pdf(pdf_path: str, chunk_size: int = 1000, overlap: int = 200):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    chunks = splitter.split_documents(docs)

    # Simplify format for storage
    return [{"text": c.page_content, "metadata": {"source": pdf_path}} for c in chunks]
