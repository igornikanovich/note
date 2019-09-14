import base64

from Crypto.Cipher import AES

from Note.settings import CRYPT_KEY


def encrypt_val(clear_text):
    enc_secret = AES.new(CRYPT_KEY)
    tag_string = (str(clear_text) +
                  (AES.block_size -
                   len(str(clear_text)) % AES.block_size) * "\0")
    cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))
    return cipher_text


def decrypt_val(cipher_text):
    dec_secret = AES.new(CRYPT_KEY)
    raw_decrypted = dec_secret.decrypt(base64.b64decode(cipher_text[2:-1]))
    clear_val = raw_decrypted.decode().rstrip("\0")
    return clear_val


def crypt(note):
    try:
        note = decrypt_val(note)
        return note
    except ValueError:
        note = encrypt_val(note)
        return note
