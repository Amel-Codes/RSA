import hashlib

def hacher_fichier(chemin_fichier):
    with open(chemin_fichier, "rb") as f:
        contenu = f.read()
        hash_bytes = hashlib.sha256(contenu).digest()
        return int.from_bytes(hash_bytes, byteorder='big')
