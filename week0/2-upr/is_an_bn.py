def is_an_bn(word):
    if word == "":
        return True
    count_a = word.count("a")
    count_b = word.count("b")
    if count_a == count_b:
        a = str("a" * count_a)
        b = str("b" * count_b)
        if word.find(a) != -1 and word.find(b) != -1:
            if word.find(a) < word.find(b):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
