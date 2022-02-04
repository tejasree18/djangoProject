def convertPlainTextToDiagraphs(plainText):
    # append X if Two letters are being repeated
    for s in range(0, len(plainText) + 1, 2):
        if s < len(plainText) - 1:
            if plainText[s] == plainText[s + 1]:
                plainText = plainText[:s + 1] + 'X' + plainText[s + 1:]

    # append X if the total letters are odd, to make plaintext even
    if len(plainText) % 2 != 0:
        plainText = plainText[:] + 'X'

    return plainText


def generateKeyMatrix(key):
    matrix_5x5 = [[0 for i in range(5)] for j in range(5)]

    simpleKeyArr = []

    """
     Generate SimpleKeyArray with key from user Input 
     with following below condition:
     1. Character Should not be repeated again
     2. Replacing J as I (as per rule of playfair cipher)
    """
    for c in key:
        if c not in simpleKeyArr:
            if c == 'J':
                simpleKeyArr.append('I')
            else:
                simpleKeyArr.append(c)

    """
    Fill the remaining SimpleKeyArray with rest of unused letters from english alphabets 
    """

    is_I_exist = "I" in simpleKeyArr

    # A-Z's ASCII Value lies between 65 to 90 but as range's second parameter excludes that value we will use 65 to 91
    for i in range(65, 91):
        if chr(i) not in simpleKeyArr:
            # I = 73
            # J = 74
            # We want I in simpleKeyArr not J

            if i == 73 and not is_I_exist:
                simpleKeyArr.append("I")
                is_I_exist = True
            elif i == 73 or i == 74 and is_I_exist:
                pass
            else:
                simpleKeyArr.append(chr(i))

    ##mapping simpleKeyArr to matrix_5x5

    index = 0
    for i in range(0, 5):
        for j in range(0, 5):
            matrix_5x5[i][j] = simpleKeyArr[index]
            index += 1

    return matrix_5x5


def indexLocator(char, cipherKeyMatrix):
    indexOfChar = []

    # convert the character value from J to I
    if char == "J":
        char = "I"

    for i, j in enumerate(cipherKeyMatrix):
        # enumerate will return object like this:
        # [
        #   (0, ['K', 'A', 'R', 'E', 'N']),
        #   (1, ['D', 'B', 'C', 'F', 'G']),
        #   (2, ['H', 'I', 'L', 'M', 'O']),
        #   (3, ['P', 'Q', 'S', 'T', 'U']),
        #   (4, ['V', 'W', 'X', 'Y', 'Z'])
        # ]
        # i,j will map to tupels of above array

        # j refers to inside matrix =>  ['K', 'A', 'R', 'E', 'N'],
        for k, l in enumerate(j):
            # again enumerate will return object that look like this in first iteration:
            # [(0,'K'),(1,'A'),(2,'R'),(3,'E'),(4,'N')]
            # k,l will map to tupels of above array
            if char == l:
                indexOfChar.append(i)  # add 1st dimension of 5X5 matrix => i.e., indexOfChar = [i]
                indexOfChar.append(k)  # add 2nd dimension of 5X5 matrix => i.e., indexOfChar = [i,k]
                return indexOfChar

            # Now with the help of indexOfChar = [i,k] we can pretty much locate every element,
            # inside our 5X5 matrix like this =>  cipherKeyMatrix[i][k]
