import time
import random

from rsa_utils import generer_cles_rsa, montgomery_exponentiation, factoriser, inverse_modulaire
from encoding import texte_en_blocs_nombres, blocs_nombres_en_texte, taille_max_bloc
from constants import ALPHABET
from hashing import hacher_fichier

if __name__ == "__main__":
    random.seed(time.time())

    message = "HELLO AMELMO___ULA__"
    (e, n), (d, n) = generer_cles_rsa(100)
    M = len(ALPHABET)
    b = taille_max_bloc(M, n)
    blocs = texte_en_blocs_nombres(message, b, ALPHABET)
    blocs_chiffres = [montgomery_exponentiation(m, e, n) for m in blocs]
    texte_chiffre = blocs_nombres_en_texte(blocs_chiffres, b+1, ALPHABET)
    blocs_chiffres2 = texte_en_blocs_nombres(texte_chiffre, b+1, ALPHABET)
    blocs_dechiffres = [montgomery_exponentiation(m, d, n) for m in blocs_chiffres2]
    texte_dechiffre = blocs_nombres_en_texte(blocs_dechiffres, b, ALPHABET).rstrip('_')

    print("Message original:", message)
    print("Message déchiffré:", texte_dechiffre)

    # Signature de fichier
    chemin = "fichiertest.txt"
    hash_val = hacher_fichier(chemin) % n
    signature = montgomery_exponentiation(hash_val, d, n)
    est_valide = montgomery_exponentiation(signature, e, n) == hash_val
    print("Signature valide ?", est_valide)
