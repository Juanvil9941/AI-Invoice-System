import os

model = None  

def get_model():
    global model
    if model is None:
        print("Loading embedding model")
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


def generate_embedding(text):
    if os.getenv("RENDER") == "true":
        print("Using dummy embedding(cloud mode)")
        return [0.0] * 384

    model = get_model()
    return model.encode(text).tolist()