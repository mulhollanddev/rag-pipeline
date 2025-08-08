
# 🧠 RAG com LLaMA 3 e Ollama

## ⚙️ Instalação de dependências do projeto

```bash
pip install -r requirements.txt
```

---

## 🦙 Instalação do Ollama com o modelo **LLaMA 3** no **Windows**

### 📥 1. Baixar e instalar o Ollama

- Acesse: 👉 [https://ollama.com/download](https://ollama.com/download)
- Baixe o instalador `.exe` e conclua a instalação.
- **Ou instale via terminal**:

```powershell
winget install Ollama.Ollama
```

---

### 🛠️ 2. Adicionar o Ollama ao `PATH` do Windows

Execute no PowerShell (como administrador):

```powershell
[System.Environment]::SetEnvironmentVariable('Path', [System.Environment]::GetEnvironmentVariable('Path', 'Machine') + ';C:\Program Files\Ollama', 'Machine')
```

---

### 🧪 3. Baixar e testar o modelo

#### 📦 Baixar o modelo:

Modelo completo (mais pesado):

```bash
ollama pull llama3:8b
```

Modelo otimizado (mais leve):

```bash
ollama pull llama3:instruct
```

#### ✅ Exemplo de uso com LangChain:

```python
from langchain_ollama import ChatOllama  # Atualizado! Não use langchain_community

llm = ChatOllama(model="llama3:instruct")
resposta = llm.invoke("Qual é a capital da Alemanha?")
print(resposta.content)
```

---

## 🐧 Instalação do Ollama com o modelo **LLaMA 3** no **Linux/macOS**

### 📥 1. Baixar e instalar o Ollama

- Acesse: 👉 [https://ollama.com/download](https://ollama.com/download)
- Ou, via terminal (Linux/macOS):

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## 🤝 Integração com Hugging Face (opcional)

1. Faça login via terminal:

```bash
huggingface-cli login
```

2. Insira seu token de acesso, obtido em:

👉 [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## 🛠️ Comando rápido para baixar o modelo LLaMA 3

```bash
ollama pull llama3:instruct
```
