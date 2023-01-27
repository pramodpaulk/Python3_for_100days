''' Project-1 Band name idea generator '''
# Function to generate the band name
def band_name_gen():
    Q1 = input("What is your first name? \n")
    Q2 = input("What is your pet name? \n")
    return Q1 + ' ' +  Q2

# To Print the final statement and execute the function
print('Your Band Name can be.... \n',band_name_gen())

