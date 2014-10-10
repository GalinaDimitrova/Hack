def nan_expand(times):
    result = ["NaN"]
    if times == 0:
        print(" ")
        return " "
    else:
        for i in range(times):
            result.insert(0,"Not a ")
        print("".join(result))
        return "".join(result)

nan_expand(0)
nan_expand(1)
nan_expand(2)
nan_expand(3)