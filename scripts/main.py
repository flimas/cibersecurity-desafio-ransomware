import sys
import os
import encrypt
import decrypt
import config
import logger

def main():
    config.setup_environment()
    print("|˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜|")
    print("|            Secure File Manager           |")
    print("|__________________________________________|")
    print("| 1. Encrypt File  |  2. Encrypt Directory |")
    print("|__________________|_______________________|")
    print("| 3. Decrypt File  |  4. Decrypt Directory |")
    print("|__________________|_______________________|")
    choice = input("Choose an option: ")


    try:
        if choice == "1":
            file_path = input("Enter the file path: ").strip()
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            encrypt.encrypt_file(file_path)
            print(f"File {dir_path} encrypted successfully!")
        
        elif choice == "2":
            dir_path = input("Enter the directory path: ").strip()
            if not os.path.isdir(dir_path):
                raise FileNotFoundError(f"Directory not found: {dir_path}")
            encrypt.encrypt_directory(dir_path)
            print(f"Directory {dir_path} encrypted successfully!")

        elif choice == "3":
            file_path = input("Enter the encrypted file path: ").strip()
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            decrypt.decrypt_file(file_path)
            print(f"File {file_path} decrypted successfully!")
            
        
        elif choice == "4":
            dir_path = input("Enter the encrypted directory path: ").strip()
            if not os.path.isdir(dir_path):
                raise FileNotFoundError(f"Directory not found: {dir_path}")
            decrypt.decrypt_directory(dir_path)
            print(f"Directory {dir_path} decrypted successfully!")
            
        else:
            print("Invalid choice. Exiting.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        logger.log_action("Error", f"{e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
        main()
