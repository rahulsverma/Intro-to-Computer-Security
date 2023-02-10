#ROW TRANSPOSITION CIPHER
import math
import sys
import string


def generate_matrix(text: str, rows: int, cols: int):
    matrix = []
    chars = list(text)
    for _ in range(rows):
        matrix.append(chars[:cols])
        remaining_chars = chars[cols:]
        chars = remaining_chars if len(remaining_chars) == cols else remaining_chars + ([''] * (cols - len(remaining_chars)))
    return matrix


def encrypt(plain_text: str, key: str):
    rows, cols = math.ceil(len(plain_text) / len(key)), len(key)
    paddingCharacters = list(string.ascii_lowercase)
    paddingCharacters.reverse()
    spaces = ''
    for i in range(rows*cols - len(plain_text)):
        spaces = spaces + paddingCharacters[(rows*cols - len(plain_text))-i-1]
    matrix = generate_matrix(plain_text+spaces, rows, cols)
    encrypted_text = []
    key_map = []
    for c in key:
        for r in range(rows):
            key_map.append(int(c)-1)
            encrypted_text.append(matrix[r][int(c)-1])
    return ''.join(encrypted_text)


def decrypt(plain_text: str, key: str):
    rows, cols = math.ceil(len(plain_text) / len(key)), len(key)
    matrix = generate_matrix(plain_text, cols, rows)
    key_map = { k: key.index(str(k+1)) for k in range(len(key)) }
    decrypted_text = []
    for r in range(rows):
        for c in range(cols):
            decrypted_text.append(matrix[key_map[c]][r])
    return ''.join(decrypted_text)


def main(inputfile, outputfile, key, choice):

    if choice == "1":
        plain_text = open(inputfile, "r").read().lower().strip()
        encrypted_text = encrypt(plain_text, key)
        open(outputfile,"w").write(encrypted_text)

    elif choice == "0":
        encrypted_text = open(inputfile, "r").read().lower().strip()
        open(outputfile,"w").write(decrypt(encrypted_text, key).strip())

    else:
        print('Invalid choice')


if __name__ == "__main__":
    main(*sys.argv[1:])