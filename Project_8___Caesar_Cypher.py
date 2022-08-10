#German Krugkov
# 100 days of coding project 6
# random password generator


a=input("text to encrypt : ")

charachters = [chr(i) for i in range(97,123)] #+ [chr(i) for i in range(65,91)]



print(charachters)

def encryption(text) :
    #convert from ascii to ints
    text2=[ord(c) for c in text]
    text=[c-97 for c in text2]
   
    #print(text)
    shift = int(input("shift by how many "))

    #shift ints by specified ammount
    encrypted = [((x+shift)%26) for x in text]

    #wraparound for characters shifted past z
    #for i, x in enumerate(encrypted) :
    #    if x > 122 :
    #        encrypted[i] = int(x%122)+96

    #store back as text string
    text = "".join([chr(x+97) for x in encrypted])
 
    print(text)

    return text




def decryption(text) :

    #convert from ascii to ints
    text2=[ord(c) for c in text]
    text=[c-97 for c in text2]
   
    #print(text)
    shift = int(input("shift by how many "))

    #shift ints by specified ammount
    encrypted = [((x-shift)%26) for x in text]

    #wraparound for characters shifted past z
    #for i, x in enumerate(encrypted) :
    #    if x > 122 :
    #        encrypted[i] = int(x%122)+96

    #store back as text string
    text = "".join([chr(x+97) for x in encrypted])
 
    print(text)

    return text


a = encryption(a)

a = decryption(a)