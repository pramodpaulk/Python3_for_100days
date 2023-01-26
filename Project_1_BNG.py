# Project-1 Band name idea generator
def bandnamegen():
    Q1 = input("What is your first name?")
    Q2 = input("What is your pet name?")
    BandName = Q1 + ' ' +  Q2
    return BandName

print('Your Band Name can be.... \n',bandnamegen())

