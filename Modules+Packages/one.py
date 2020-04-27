#one.py

def func(): #Creating a function
    print("FUNC() IN ONE.PY")
print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    #Usually, all your functions go in here
    print('ONE.PY is being run directly')
else: #There is usually no else statment
    print('ONE.PY is an import')