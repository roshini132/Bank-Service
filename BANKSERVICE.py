import json

class RBI:
    def __init__(self):
        self.Total_funds1 = 100000
        self.Total_accounts1 = 10000


class SBI(RBI):
    def __init__(self):
        self.Total_funds2 = 50000
        self.Total_accounts2 = 5000
        super().__init__()


class TamilnaduBank(SBI):
    def __init__(self):
        self.Total_funds3 = 25000
        self.Total_accounts3 = 2500
        super().__init__()


class CUB(TamilnaduBank):
    def __init__(self):
        self.Total_funds4 = 12000
        self.Total_accounts4 = 1000
        super().__init__()

    def deposit(self):
        self.dep = int(input("Enter amount to be deposited: "))
        self.Total_funds4 += self.dep
        print("Amount Deposited:", self.dep)
        print("Your City Union Bank Account Balance is: ", self.Total_funds4)
        self.Total_funds3 += self.dep
        print("TamilNadu Bank Account Balance is: ", self.Total_funds3)
        self.Total_funds2 += self.dep
        print("State Bank Account Balance is: ", self.Total_funds2)
        self.Total_funds1 += self.dep
        print("Reserve Bank Account Balance is: ", self.Total_funds1)

        self.withdraw()

    def withdraw(self):
        self.wd = int(input("\nEnter your withdrawn amount: "))
        if self.Total_funds4 >= self.wd:
            self.Total_funds4 -= self.wd
            print("Your amount is withdrawn: ", self.wd)
            print("Your City Union Bank Account Balance is: ", self.Total_funds4)

            self.Total_funds3 -= self.wd
            print("Tamilnadu Bank Account Balance is: ", self.Total_funds3)

            self.Total_funds2 -= self.wd
            print("State Bank Account Balance is: ", self.Total_funds2)

            self.Total_funds1 -= self.wd
            print("Reserve Bank Account Balance is: ", self.Total_funds1)
        else:
            print("\nInsufficient Balance")
            print("Please Enter Your Available Balance")
            self.withdraw()

        self.open_acc()

    def open_acc(self):
        self.open = int(input("\nEnter the Number to open a New Account: "))
        self.Total_accounts4 += self.open
        print("Your Account is Successfully Created from our Chennai Bank")
        print("Total Account of City Union Bank is: ", self.Total_accounts4)

        self.Total_accounts3 += self.open
        print("Total Account of Tamilnadu Bank is: ", self.Total_accounts3)
        self.Total_accounts2 += self.open
        print("Total Account of State Bank is: ", self.Total_accounts2)
        self.Total_accounts1 += self.open
        print("Total Account of Reserve Bank is: ", self.Total_accounts1)

        self.close_acc()

    def close_acc(self):
        self.close = int(input("\nEnter the Number to Close Account: "))
        if self.Total_accounts4 >= self.close:
            self.Total_accounts4 -= self.close
            print("Your Account is successfully closed from our Bank")
            print("Total Account of City Union Bank is: ", self.Total_accounts4)

            self.Total_accounts3 -= self.close
            print("Total Account of Tamilnadu Bank is: ", self.Total_accounts3)
            self.Total_accounts2 -= self.close
            print("Total Account of State Bank is: ", self.Total_accounts2)
            self.Total_accounts1 -= self.close
            print("Total Account of Reserve Bank is: ", self.Total_accounts1)
        else:
            print("Sorry, ", self.close, " accounts are not available in our Chennai Bank")


def read_data_from_file():
    try:
        with open(r"C:\Users\crosh\OneDrive\Desktop\Banking Service.py.txt", "r") as file:
            content = file.read()
            if content:
                data = json.loads(content)
                return data
    except FileNotFoundError:
        return None


def write_data_to_file(data):
    with open(r"C:\Users\crosh\OneDrive\Desktop\Banking Service.py.txt", "a") as file:
        json.dump(data, file, indent=2)


data_from_file = read_data_from_file()
if data_from_file:
    x = CUB()
    x.Total_accounts1 = data_from_file['rbi'][0]
    x.Total_funds1 = data_from_file['rbi'][1]
    x.Total_accounts2 = data_from_file['sbi'][0]
    x.Total_funds2 = data_from_file['sbi'][1]
    x.Total_accounts3 = data_from_file['Tamilnadu_bank'][0]
    x.Total_funds3 = data_from_file['Tamilnadu_bank'][1]
    x.Total_accounts4 = data_from_file['cub'][0]
    x.Total_funds4 = data_from_file['cub'][1]
else:
    x = CUB()

x.deposit()

account_data = {
    'rbi': [x.Total_accounts1, x.Total_funds1],
    'sbi': [x.Total_accounts2, x.Total_funds2],
    'Tamilnadu_bank': [x.Total_accounts3, x.Total_funds3],
    'cub': [x.Total_accounts4, x.Total_funds4]
}

write_data_to_file(account_data)
