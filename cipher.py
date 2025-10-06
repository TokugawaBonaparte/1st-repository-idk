def keyword_cipher(key : str,msg : str):
    new_key = []
    for i in key:
        if new_key.count(i) < 1:
            new_key.append(i)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_alpbhabet = [i for i in alphabet if i not in new_key]
    new_key.extend(new_alpbhabet) # unique letters only 
    new_msg = list(msg)
    translator = dict(zip(alphabet,new_key)) # key - abcd , value - corresponding cipher
    for i in range(len(msg)):
        if msg[i] in translator:
            ind = translator.get(msg[i])
            new_msg[i] = ind           
    return ''.join(new_msg)
print(keyword_cipher('purplepineapple','abc'))
