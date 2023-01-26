''' Project-1 Band name idea generator '''
# Function to generate the band name
def band_name_gen():
    Q1 = input("What is your first name?")
    Q2 = input("What is your pet name?")
    BandName = Q1 + ' ' +  Q2
    return BandName

print('Your Band Name can be.... \n',band_name_gen())

