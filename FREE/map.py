def farenheit(T):
    return (9.0 / 5) * T + 32


farenheit(0)
temp = [0, 66.5, 50, 100]
stub = map(farenheit, temp)


map(lambda T: (9.0 / 5) * T + 32, temp)
