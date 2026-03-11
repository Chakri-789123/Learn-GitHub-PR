import random


def generate_code(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    code = ""

    for i in range(length):
        random_index = random.randint(0, len(characters) - 1)
        code += characters[random_index]

    return code
