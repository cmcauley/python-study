def recall_password(cipher_grille, ciphered_password):
    password = ""
    x = 0

    password += lookup_password(cipher_grille, ciphered_password)

    while x < 3:
        cipher_grille = rotate_matrix_90cw(cipher_grille)
        password += lookup_password(cipher_grille, ciphered_password)
        x += 1

    return password

def lookup_password(cipher_grille, ciphered_password):
    passwd = ""

    for x in range(len(cipher_grille)):
        for y in range(len(cipher_grille[x])):
            if cipher_grille[x][y] == 'X':
                passwd += str(ciphered_password[x][y])

    return passwd

def rotate_matrix_90cw(matrix):
    rotated_matrix = [[0 for x in range(4)] for y in range(4)]

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            rotated_matrix[y][3-x] = matrix[x][y]

    return rotated_matrix

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
