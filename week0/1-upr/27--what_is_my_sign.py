def what_is_my_sign(day, month):
    sign_dict = {
        1: "Aquarius",
        2: "Pisces",
        3: "Arias",
        4: "Taurus",
        5: "Gemini",
        6: "Cancer",
        7: "Leo",
        8: "Virgo",
        9: "Libra",
        10: "Scorpio",
        11: "Sagittarius",
        12: "Capricorn"
    }

    if day in range(1, 21):
        if month == 1:
            print(sign_dict[12])
            return sign_dict[12]
        else:
            print(sign_dict[month - 1])
            return sign_dict[month - 1]
    else:
        print(sign_dict[month])
        return sign_dict[month]


what_is_my_sign(5, 8)
what_is_my_sign(29, 1)
what_is_my_sign(30, 6)
what_is_my_sign(31, 5)
what_is_my_sign(2, 2)
what_is_my_sign(8, 5)
what_is_my_sign(9, 1)
