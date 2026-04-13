import os

model = None

def get_model():
    global model
    if model is None:
        print("Loading embedding model (local)")
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


def generate_embedding(text):
    if os.getenv("RENDER") == "true":
        print("Using OpenAI embedding (cloud mode)")

        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )

        return response.data[0].embedding


    model = get_model()
    return model.encode(text).tolist()