# setup.ps1
# Instala o Ollama
winget install Ollama.Ollama

# Espera um pouco
Start-Sleep -Seconds 5

# Inicia o servidor Ollama
Start-Process -NoNewWindow -FilePath "ollama" -ArgumentList "serve"

# Espera o servidor iniciar
Start-Sleep -Seconds 5

# Puxa o modelo necessário
ollama pull llama3
