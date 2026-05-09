def clean_text(text):
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    return text.strip()


def split_text(text, chunk_size=100, overlap=20):
    words = text.split
    chunks = []

    i = 0
    while i < len(words):
        chunk = words[i:i+chunk_size]
        chunks.append(" ".join(chunk))
        i = i+chunk_size-overlap

    # for i in range(0, len(text), chunk_size):
    #     chunks.append(text[i:i+chunk_size])

    return chunks
