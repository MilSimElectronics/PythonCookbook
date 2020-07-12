# The Caesar cipher is one of the earliest known and simplest ciphers. It is a type of substitution cipher in which
# each letter in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift
# of 1, A would be replaced by B, B would become C, and so on. The method is named after Julius Caesar,
# who apparently used it to communicate with his generals.

alpha = "abcdefghijklmnopqrstuvwxyz"


def encrypt(clear_text):
    cypher_text = ""

    for char in clear_text:
        if char in alpha:
            new_pos = (alpha.find(char) + 13) % 26
            cypher_text += alpha[new_pos]
        else:
            cypher_text += char

    return cypher_text


user_input = input("Enter String: ")
user_input = user_input.lower()
print(encrypt(user_input))
