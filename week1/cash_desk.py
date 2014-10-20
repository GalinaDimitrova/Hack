class CashDesk:

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, taken_money):
        for key in taken_money:
            self.money[key] = taken_money[key]
        return self.money

    def total(self):
        total = 0
        for item in self.money:
            total += item * self.money[item]
        return total


    def can_withdraw_money(self, amount_of_money):
        money_diction = {}
        for key in self.money:
            if self.money[key] != 0:
                money_diction[key] = self.money[key]
        for key in sorted(money_diction, reverse=True):
            while amount_of_money - key >= 0 and money_diction[key] > 0:
                amount_of_money -= key
                money_diction[key] -= 1
                return money_diction
        if amount_of_money == 0:
            return True
        else:
            return False

    # def can_withdraw_money(self, amount_of_money):
    #     count_notes = 0
    #     new_amount = amount_of_money
    #     for item in self.money:

    #         if item == amount_of_money:
    #             print(True)
    #             return True
    #         elif item < amount_of_money:
    # how many notes we have with that amount
    #             count_notes = self.money[item]
    #             for i in range(1, count_notes+1):
    #                 if new_amount - item*self.money[item] == amount_of_money:
    #                     print(True)
    #                     return True
    #                 elif


my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
my_cash_desk.total()  # 72
my_cach_desk.can_withdraw_money(30)  # False
my_cach_desk.can_withdraw_money(70)  # True
