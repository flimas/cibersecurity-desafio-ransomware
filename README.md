# Secure File Manager

**Secure File Manager** é uma ferramenta em Python desenvolvida para proteger arquivos e diretórios por meio de criptografia AES. A aplicação permite criptografar e descriptografar arquivos e diretórios com uma interface amigável, além de registrar logs de operações realizadas.

---

## Funcionalidades

1. **Criptografia de Arquivos:** Proteja arquivos individuais com uma chave de criptografia segura.
2. **Criptografia de Diretórios:** Aplique proteção a todos os arquivos em um diretório.
3. **Descriptografia de Arquivos:** Restaure arquivos previamente criptografados.
4. **Descriptografia de Diretórios:** Restaure múltiplos arquivos criptografados em um diretório.
5. **Registro de Logs:** Todas as operações são registradas em um arquivo de log para auditoria.
6. **Interface Amigável:** Mensagens claras para o usuário sobre sucesso ou falha de operações.

---

## Requisitos

- Python 3.8 ou superior
- Pacotes Python:
  - `pyaes`
  - `os`
  - `logging`

---

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/cibersecurity-desafio-ransomware.git
   cd cibersecurity-desafio-ransomware

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

3. Instalar as dependências:
    ```bash
    pip install pyaes

***
# USO

1.	Execute o programa principal:
    ```bash
    python3 main.py
2.	Escolha uma das opções no menu:
  * Criptografar Arquivo: Insira o caminho do arquivo que deseja proteger.
  * Criptografar Diretório: Insira o caminho do diretório para criptografar todos os arquivos.
  * Descriptografar Arquivo: Insira o caminho do arquivo criptografado.
  * Descriptografar Diretório: Insira o caminho do diretório para restaurar todos os arquivos.

## Configuração
No arquivo config.py pode ser alterado a chave de criptografia e o local dos logs:
* Chave de Criptografia: Altere as constante KEY para uma chave de sua preferência. Lembrando que por se tratar de AES a chave deve ter 16 bytes (128 bits), 24 bytes (192 bits) ou 32 bytes (256 bits)
* Local do Log: Ajuste o caminho do arquivo de log na variável LOG_FILE

***
# Contribuição
Contribuições são bem-vindas!
