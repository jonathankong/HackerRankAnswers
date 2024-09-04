def CaesarCipher(s, k):
    encryptedMsg = []
    capitalLettersASCIILimit = 90
    
    for c in s:
        if c.isalpha():
            if ord(c) <= capitalLettersASCIILimit:
                encryptedMsg.append(chr(((ord(c) + k - ord('A')) % 26) + ord('A')))
            else:
                encryptedMsg.append(chr(((ord(c) + k - ord('a')) % 26) + ord('a')))
        else:
            encryptedMsg.append(c)
            
    return ''.join(encryptedMsg)
    
print(CaesarCipher("middle-Outz", 2))