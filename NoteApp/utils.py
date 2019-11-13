import binascii
import base64

from cryptography.fernet import Fernet, InvalidToken

from Note.settings import CRYPT_KEY


def encrypt_val(txt):
    cipher_suite = Fernet(CRYPT_KEY)
    encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
    encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
    return encrypted_text


def decrypt_val(txt):
    txt = base64.urlsafe_b64decode(txt)
    cipher_suite = Fernet(CRYPT_KEY)
    decoded_text = cipher_suite.decrypt(txt).decode("ascii")
    return decoded_text


def crypt(note):
    try:
        note = decrypt_val(note)
        return note
    except binascii.Error:
        note = encrypt_val(note)
        return note
    except InvalidToken:
        note = encrypt_val(note)
        return note
