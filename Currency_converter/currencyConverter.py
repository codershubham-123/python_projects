# Program to convert currency

with open('currencyValue.txt') as f: # Currency value file open
    lines = f.readlines()

CurrencyDict = {}
for line in lines:
    parse = line.split('\t')
    CurrencyDict[parse[0]] = parse[1]

amount = int(input("Enter your amount:\n"))
print("choose your currency in which you want to convert your amount.\n Available currency option are:\n")
[print(item)for item in CurrencyDict.keys()]

currency = input("Enter your currency in which you want to change your amount: \n")

print(f"Your {amount} INR is equal to {amount*float(CurrencyDict[currency])} {currency}")
