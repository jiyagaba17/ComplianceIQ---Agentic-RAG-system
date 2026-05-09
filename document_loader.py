from pypdf import PdfReader


def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:  # avoid None
            text += extracted

    return text


def load_document(file_path):
    if file_path.endswith(".txt"):
        return load_text(file_path)
    elif file_path.endswith(".pdf"):
        return load_pdf(file_path)
    else:
        raise ValueError("Unsupported file type")
