from cryptography.fernet import Fernet
from config import encrypt_key

fernet = Fernet(encrypt_key)

def generate_token(passwd:str):
  passwd = str.encode(passwd)
  token = fernet.encrypt(passwd)
  return token 

def decrypt_token(token):
  passwd = fernet.decrypt(token)
  return passwd