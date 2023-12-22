import string
import random

# Password generator (CHALLENGE: each sign has to be different)

class Password:

    def __init__(self,length, if_letters = True, if_numbers = True, if_specials = True):
        self.length = length
        self.letters = if_letters
        self.numbers = if_numbers
        self.specials = if_specials        
        self.list_of_chars = self.set_list_of_chars()


    def set_list_of_chars(self):
        list_of_chars = []
        list_of_letters = [i for i in string.ascii_letters]
        list_of_numbers = [i for i in string.digits]
        list_of_specials = [i for i in string.punctuation]
        if self.letters:
            list_of_chars.extend(list_of_letters)
        if self.numbers:
            list_of_chars.extend(list_of_numbers)
        if self.specials:
            list_of_chars.extend(list_of_specials)
        for i in range(self.length):
            random.shuffle(list_of_chars)
        return list_of_chars
    
    def set_password(self):
        psword = ''
        i = 0
        while i < self.length:
            char = random.choice(self.list_of_chars)
            if char not in psword: 
                psword = psword + char
                i+=1
            else: continue     
        return psword

unique_password = Password(12,True,True,False)
print(unique_password.set_password())

