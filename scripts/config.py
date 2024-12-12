import os
# Configuracoes basicas LOGs e chave
LOG_FILE = "logs/operations.log"
KEY = b"_mysecretencrypt"

# Funcao para inicializar os diretorios e arquivos necessarios
def setup_environment():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()

