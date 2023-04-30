import string
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text):
        ans = ''
        listofletterstobeadded = []
        idklist = []
        i = 0
        for letter in text:
            if letter in self.alphabet:
                listofletterstobeadded.clear()
                idklist.clear()
                letterindex = text.index(letter)
                keyletter = self.key[i%len(self.key)]
                keyletterindex = self.alphabet.index(keyletter)
                for j in range(self.alphabet.index(keyletter)):
                    indextouse = (0+j) % len(self.alphabet)
                    listofletterstobeadded.append(self.alphabet[indextouse])
                    
                for k in range(len(self.alphabet)):
                    indexforuse = (keyletterindex+k)
                    idklist.append(self.alphabet[indexforuse])
                    if self.alphabet[indexforuse] == self.alphabet[len(self.alphabet)-1]:
                        break 
                idklist.extend(listofletterstobeadded)
                ans += idklist[self.alphabet.index(letter)]
                i += 1
            else:
                ans += letter
                i += 1
        return ans
    
    def decode(self, text):
        ans = ''
        listofletterstobeadded = []
        idklist = []
        i = 0
        for letter in text:
            print(letter)
            if letter in self.alphabet:
                listofletterstobeadded.clear()
                idklist.clear()
                keyletter = self.key[i%len(self.key)]
                keyletterindex = self.alphabet.index(keyletter)
                
                for j in range(self.alphabet.index(keyletter)):
                    indextouse = (0+j) % len(self.alphabet)
                    listofletterstobeadded.append(self.alphabet[indextouse])
                
                for k in range(len(self.alphabet)-1):
                    indexforuse = (keyletterindex+k)
                    idklist.append(self.alphabet[indexforuse])
                    if self.alphabet[indexforuse] == self.alphabet[len(self.alphabet)-1]:
                        break
                    
                idklist.extend(listofletterstobeadded)
                ans += self.alphabet[idklist.index(letter)]
                i += 1
            else:
                ans += letter
                i += 1 
        return ans
key = "password"
text = "pythonisthegoat"
alphabet = string.ascii_lowercase
Vigenere = VigenereCipher(key,alphabet)
print(Vigenere.encode(text))
