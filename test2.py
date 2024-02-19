state = 'California'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 3
index = alphabet.find(state[0].lower())
shifted = alphabet[index + shift]
caesar_encrypted = ''
decrypted = ''
for letter in state:
    index = alphabet.find(letter.lower())
    newletter = alphabet[index + shift]
    caesar_encrypted += newletter
print(caesar_encrypted)
for letter in caesar_encrypted:
    index = alphabet.find(letter.lower())
    newletter = alphabet[index - shift]
    decrypted += newletter
print(decrypted)
