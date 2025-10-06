def keyword_cipher(key : str,msg : str):
    nkey = []
    nsetkey= set(key)
    for i in key:
        if nkey.count(i) < 1:
            nkey.append(i)
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    naplh = [i for i in alph if i not in nkey]
    nkey.extend(naplh) # unique letters only 
    nmsg = list(msg)
    translator = dict(zip(alph,nkey))
    for i in range(len(msg)):
        if msg[i] in translator:
            ind = translator.get(msg[i])
            nmsg[i] = ind           
    return ''.join(nmsg)
print(keyword_cipher('purplepineapple','abc'))