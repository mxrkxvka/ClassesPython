import os, pickle

class Transaction:
    def __init__(self, sum, date, currency="usd", currency_to_usd=1, descr=None):
        self.__sum = sum
        self.__date = date
        self.__currency = currency
        self.__currency_to_usd = currency_to_usd
        self.__descr = descr

    @property
    def sum(self):
        return self.__sum
    
    @property
    def date(self):
        return self.__date
    
    @property
    def currency(self):
        return self.__currency
    
    @property
    def currency_to_usd(self):
        return self.__currency_to_usd
    
    @property
    def descr(self):
        return self.__descr
    
    @property
    def usd(self):
        return self.__sum * self.__currency_to_usd
    
class Account:
    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.account_name = account_name
        self.transactions = []

    @property
    def account_name(self):
        return self.__account_name
    
    @account_name.setter
    def account_name(self, value):
        if value and len(value) < 4:
            raise ValueError("not less than four")
        self.__account_name = value


    @property
    def balance(self):
        return sum(transaction.usd for transaction in self.transactions)
    
    @property
    def all_usd(self):
        return all(transaction.currency == 'usd' for transaction in  self.transactions)

    def apply(self, transaction):
        self.transactions.append(transaction)

    def save(self, file_name):
        with open(file_name, "wb") as file:
            pickle.dump((self.__account_number, self.account_name, self.transactions), file)

    def load(self, file_name):
        with open(file_name, "rb") as file:
            self.__account_number, self.account_name, self.transactions = pickle.load(file)

    def __len__(self):
        return len(self.transactions)

def main():
    data_dir = "D:\\ClassesPython\\"

    dollar = Transaction(100, '01.09.2005')
    print(dollar.sum, dollar.date, dollar.currency, dollar.currency_to_usd, dollar.descr, dollar.usd)

    account_name = "TestAccount"
    account_number = "123456"
    file_name = os.path.join(data_dir, f"{account_number}.acc")

    account = Account(account_number, account_name)
    account.apply(Transaction(100, '01.09.2005'))
    account.apply(Transaction(200, '02.09.2005', currency="eur", currency_to_usd=1.2))

    print("Balance in USD:", account.balance)
    print("All transactions in USD:", account.all_usd)

    try:
        account.save(file_name)
        print("Account data saved successfully.")
    except Exception as e:
        print(f"Error saving account data: {e}")


    loaded_account = Account(account_number, "LoadedAccount")
    if os.path.exists(file_name):
        try:
            loaded_account.load(file_name)
            print("Loaded account name:", loaded_account.account_name)
            print("Loaded balance in USD:", loaded_account.balance)
        except Exception as e:
            print(f"Error loading account data: {e}")
    else:
        print("No saved account data found.")

    if os.path.exists(file_name):
        os.remove(file_name)


if __name__ == "__main__":
    main()