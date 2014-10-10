def is_an_bn(word):
    if word == "":
        print(True)
        return True

    count_a = word.count("a")
    count_b = word.count("b")
   
    if count_a == count_b:
        a = str("a"*count_a)
        b = str("b"*count_b)

        if word.find(a) != -1 and word.find(b)!= -1:
            if word.find(a) < word.find(b):
                print(True)
                return True
            else:
                print(False)
                return False
        else:
            print(False)
            return False
    else:
        print(False)
        return False
    





is_an_bn("")            #True
is_an_bn("rado")        #False
is_an_bn("aaabb")       #False
is_an_bn("aaabbb")      #True
is_an_bn("aabbaabb")    #False
is_an_bn("bbbaaa")      #False
is_an_bn("aaaaabbbbb")  #True