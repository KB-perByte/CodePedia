def msgHolder(msg): #firstClass methord

    def wrapper(txt):
        return f'{msg}{txt}{msg}'

    return wrapper

mx = msgHolder('<h1>') #closure concept
print(mx("Data"))