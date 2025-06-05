def key_matrix(key):
    key = key.upper().replace('J', 'I')
    seen = set()
    key = ''.join([c for c in key if c.isalpha() and not (c in seen or seen.add(c))])
    alpha = ''.join([c for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ" if c not in seen])
    full = key + alpha
    matrix = [list(full[i:i+5]) for i in range(0, 25, 5)]
    pos = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    return matrix, pos

def prepare(text):
    text = ''.join(filter(str.isalpha, text.upper().replace('J', 'I')))
    pad = next(c for c in 'XABCDEFGHIJKLMNOPQRSTUVWXYZ' if c not in text)
    i, pairs = 0, []
    while i < len(text):
        a, b = text[i], text[i+1] if i+1 < len(text) else pad
        if a == b:
            pairs.append(a + pad)
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs, pad

def process(pairs, matrix, pos, enc=True):
    res = ''
    for a, b in pairs:
        r1, c1 = pos[a]
        r2, c2 = pos[b]
        if r1 == r2:
            res += matrix[r1][(c1 + (1 if enc else -1)) % 5]
            res += matrix[r2][(c2 + (1 if enc else -1)) % 5]
        elif c1 == c2:
            res += matrix[(r1 + (1 if enc else -1)) % 5][c1]
            res += matrix[(r2 + (1 if enc else -1)) % 5][c2]
        else:
            res += matrix[r1][c2] + matrix[r2][c1]
    return res

def main():
    key = input("Key: ")
    text = input("Plaintext: ")
    matrix, pos = key_matrix(key)
    print("\nKey Matrix:")
    [print(' '.join(row)) for row in matrix]
    pairs, pad = prepare(text)
    print("\nPairs:", ' '.join(pairs))
    cipher = process(pairs, matrix, pos)
    print("\nCiphertext:", cipher)
    plain = process([cipher[i:i+2] for i in range(0, len(cipher), 2)], matrix, pos, enc=False)
    print("\nDecrypted:", plain.replace(pad, ''))

if __name__ == "__main__":
    main()
