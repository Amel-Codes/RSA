from constants import ALPHABET

def taille_max_bloc(M, n):
    b = 1
    while M**b <= n:
        b += 1
    return b - 1

def texte_en_blocs_nombres(message, b, alphabet):
    blocs = []
    message = message.upper()
    for i in range(0, len(message), b):
        bloc = message[i:i+b].ljust(b, '_')
        val = 0
        for j, c in enumerate(bloc):
            val += alphabet[c] * (len(alphabet) ** (b - 1 - j))
        blocs.append(val)
    return blocs

def blocs_nombres_en_texte(blocs, b, alphabet):
    inverse_alphabet = {v: k for k, v in alphabet.items()}
    message = ""
    for val in blocs:
        bloc = ""
        for i in range(b):
            puissance = len(alphabet) ** (b - 1 - i)
            index = val // puissance
            val %= puissance
            bloc += inverse_alphabet[index]
        message += bloc
    return message
