import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(name="invoices")


def store_embedding_data(text, embedding, doc_id):
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[doc_id]
    )


def search_similar_data(query_embedding):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    return results.get("documents", [])