def is_pangram(sentence):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    sentence = sentence.lower()
    
    for letter in alphabet:
        if (sentence.find(letter) < 0):
            return False
    
    return True