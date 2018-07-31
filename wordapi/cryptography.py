import rsa
import hashlib

pubkey, privkey = rsa.newkeys(512)


def encrypt_message(message):
    """encrypts the message"""
    message = message.encode('utf8')
    return rsa.encrypt(message, pubkey).hex()


def decrypt_message(message):
    """decrypt the message"""
    message = rsa.decrypt(bytes.fromhex(message), privkey)
    return message.decode('utf8')


def salt_hash(word):
    """generates a salt hash"""
    salt = "sugar"
    m = hashlib.md5()
    m.update((salt + word).encode('utf8'))
    return m.hexdigest()