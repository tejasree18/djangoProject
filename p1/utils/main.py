from .playFairC import generateKeyMatrix, convertPlainTextToDiagraphs, indexLocator


##CAESAR CIPHER
# encryption:
def caesar_encrypt(text, key):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result


##PLAYFAIR CIPHER
# encryption:
def playfairencrypt(plainText, key):
    result = []
    keyMatrix = generateKeyMatrix(key)
    i = 0
    while i < len(plainText):
        n1 = indexLocator(plainText[i], keyMatrix)
        n2 = indexLocator(plainText[i + 1], keyMatrix)
        if n1[1] == n2[1]:
            i1 = (n1[0] + 1) % 5
            j1 = n1[1]

            i2 = (n2[0] + 1) % 5
            j2 = n2[1]
            result.append(keyMatrix[i1][j1])
            result.append(keyMatrix[i2][j2])
            result.append(", ")

        # same row
        elif n1[0] == n2[0]:
            i1 = n1[0]
            j1 = (n1[1] + 1) % 5

            i2 = n2[0]
            j2 = (n2[1] + 1) % 5
            result.append(keyMatrix[i1][j1])
            result.append(keyMatrix[i2][j2])
            result.append(", ")

        # exchange columns of both value
        else:
            i1 = n1[0]
            j1 = n1[1]

            i2 = n2[0]
            j2 = n2[1]

            result.append(keyMatrix[i1][j2])
            result.append(keyMatrix[i2][j1])
            result.append(", ")

        i += 2
    return result


##TRANSPOSITION CIPHER
# encryption
def transposition_encrypt(message, key):
    cipherText = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return "".join(cipherText)
