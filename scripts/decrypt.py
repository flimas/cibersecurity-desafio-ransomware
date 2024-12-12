import os
import pyaes
import logger
import config

def decrypt_file(file_path):
    # Buscar o conteúdo criptografado e armazenar em encrypted_data para descriptografar
    if not file_path.endswith(".encrypted"):
        return
    with open(file_path, "rb") as enc_file:
        encrypted_data = enc_file.read()
    aes = pyaes.AESModeOfOperationCTR(config.KEY)
    decrypted_data = aes.decrypt(encrypted_data)

    # Salvar o arquivo com o conteúdo descriptografado e sem a extensão encrypted
    original_file = file_path[:-10] # Remove a extensão .encrypted
    with open(original_file, "wb") as dec_file:
        dec_file.write(decrypted_data)
    os.remove(file_path)
    logger.log_action("Decrypt", f"File decrypted: {file_path}")

def decrypt_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            decrypt_file(os.path.join(root, file))
    logger.log_action("Decrypt", f"Directory decrypted: {directory_path}")