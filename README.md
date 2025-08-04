# Rag



## 🦙 Instalação do Ollama com o modelo LLaMA 3 no Windows 

### 📥 1. Baixar e instalar o Ollama

👉 [https://ollama.com/download](https://ollama.com/download)

1. Faça o download do instalador `.exe`
2. Execute e conclua a instalação normalmente
3. Ou via termnial
>> winget install Ollama.Ollama
---

### ⚙️ 2. Adicionar o Ollama ao PATH do Windows
>> [System.Environment]::SetEnvironmentVariable('Path', [System.Environment]::GetEnvironmentVariable('Path', 'Machine') + ';C:\Program Files\Ollama', 'Machine')


### ⚙️ 3. Utilizar o modelo

#### Modelo mais pesado
>> ollama pull llama3:8b

#### Modelo mais leve
>> ollama pull llama3:instruct

#### Script de teste
from langchain_ollama import ChatOllama  # e não mais langchain_community

llm = ChatOllama(model="llama3:instruct")
resposta = llm.invoke("Qual é a capital da Alemanha?")
print(resposta.content)


## 🦙 Instalação do Ollama com o modelo LLaMA 3 no Linux/Mac
### 📥 1. Baixar e instalar o Ollama

👉 [https://ollama.com/download](https://ollama.com/download)
/ no linux
>> curl -fsSL https://ollama.com/install.sh | sh

## Conectar com o Hugging Face
1. Add o comando no terminal
>> huggingface-cli login

2. Inserir o token do hugging face que pode ser obtido no endereço
[https://huggingface.co/settings/tokens]
