from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text:str):
    if not text or not text.strip():
        return [0.0] * 384
    
    embedding = model.encode(text)

    return embedding.tolist()