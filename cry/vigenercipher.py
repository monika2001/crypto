def covertToCipherText(plain_text,key):
    i=0
    while len(key)<len(plain_text):
        key+=key[i]
        i+=1
    
    map={}
    num=0
    for i in range(97,123):
        map.update({chr(i):num})
        num+=1
    print(map)
    l1=[]
    for i in range(len(plain_text)):
        if plain_text[i]==" ":
            l1.append(100)
        else:
            l1.append( (map[plain_text[i]]+map[key[i]]) % 25)
    cipherText=""
    print("***")
    print("l1:",l1)
    for i in range(len(l1)):
        if l1[i]==100:
            cipherText+=" "
        else:
            cipherText+=list(map.keys())[list(map.values()).index(l1[i])]
    print(cipherText)
    return cipherText


def convertToPlainText(cipherText,key):
    i=0
    while len(key)<len(cipherText):
        key+=key[i]
        i+=1
    map={}
    num=0
    for i in range(97,123):
        map.update({chr(i):num})
        num+=1
    # print(map)
    l1=[]
    for i in range(len(cipherText)):
        if cipherText[i]==" ":
            l1.append(100)
        else:
            l1.append( (map[cipherText[i]]-map[key[i]]) % 25)
    plain_text=""
    print(l1)
    for i in range(len(l1)):
        if l1[i]==100:
            plain_text+=' '
        else:
            plain_text+=list(map.keys())[list(map.values()).index(l1[i])]
    print("-----")
    print(plain_text)

plain_text="my name is monika"
key="cipher"
cipherText=covertToCipherText(plain_text,key)
convertToPlainText(cipherText,key)