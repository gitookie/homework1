import socket
import sys

def send_translation_request(source_lang, target_lang, text):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))

    request = f"{source_lang},{target_lang},{text}"
    client.send(request.encode())
    response = client.recv(4096).decode()
    if response: #如果翻译成功的话
        print(f"Translation: {response}")
    else:
        print('something gets wrong')
    client.close()

if __name__ == "__main__":
    text = input("Enter text to translate: ")
    source_lang = input("Enter source language: ")
    target_lang = input("Enter target language: ")
    send_translation_request(source_lang, target_lang, text)
