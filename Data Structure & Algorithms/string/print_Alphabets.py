def alphabets(c1,c2):
    #Code below to print alphabets from c1 to c2
    # Don't provide a new line after printing
    order = ord(c1)
    while order <= ord(c2):
        print(chr(order), end = ' ')
        order +=1
    print()

alphabets('A','Z')
alphabets('A','z')
alphabets('a','z')