# rag-tutorial-v2

You may need to set the flag below before installing `langchain-chroma`.

```
export HNSWLIB_NO_NATIVE=1 
```

You may need to run this 

```
python -m venv langchain-env
source langchain-env/bin/activate

 ollama pull llama3
 ollama run llama3
 ollama pull nomic-embed-text
 ollama pull mistral

```