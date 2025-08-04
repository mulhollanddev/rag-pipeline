from langchain_ollama import ChatOllama  # e não mais langchain_community

llm = ChatOllama(model="llama3:instruct")
resposta = llm.invoke("Qual é a capital da Alemanha?")
print(resposta.content)
