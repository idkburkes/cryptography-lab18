from nltk.corpus import words as nltk


def encrypt(msg, shift):
    res = ''

    for char in msg:
        if char.isupper():
            caseASCII = 65 #uppercase ascii letters start at 65
            shiftedCharASCII = ((ord(char) + shift - caseASCII) % 26) + caseASCII
            res += chr(shiftedCharASCII)
        elif char.islower():
            caseASCII = 97 #lowercase ascii letters start at 97
            shiftedCharASCII = ((ord(char) + shift - caseASCII) % 26) + caseASCII
            res += chr(shiftedCharASCII)
        elif ord(char) == 32:
            res += ' ' # Handle whitespace
        else:
            res += char # Ignore all other characters

    return res

def decrypt(msg, shift):
    return encrypt(msg, 26-shift)

def crack(msg):
    word_list = nltk.words()
    res = ''
    max_words_matched = 0

    for shift in range(1,26):
        decrypted = decrypt(msg, shift)
        words_matched = 0
        for word in decrypted.split(' '):
            if word in word_list:
                words_matched += 1
        
        # We'll try a quick exit if more than 50% of the words match
        if words_matched > len(msg) // 2:
            return decrypted
        
        #Otherwise we'll return the decryption with the most words matched
        elif words_matched > max_words_matched:
            max_words_matched = words_matched
            res = decrypted
            
    return res
        


if __name__ == '__main__':
    shift = 10
    msg = 'We are typing a sentence. Lets see The Encrypted'
    print(f'message: {msg}')
    encrypted = encrypt(msg, shift)
    print(f'encrypting: {encrypted}')
    decrypted = decrypt(encrypted, shift)
    print(f'decrypted: {decrypted}')

    print(f'decrypting without shift: {encrypted}')
    cracked = crack(encrypted)
    print(f'cracked message: {cracked}')