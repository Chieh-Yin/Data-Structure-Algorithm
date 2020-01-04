def permutationCipher(password, key):
    table = {ord(i): key[(ord(i))-97] for i in password}
    return password.translate(table)
