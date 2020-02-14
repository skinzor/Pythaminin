def check(x):
    if x == 69:
        def result():
            print("YES. X is equal to 69")

    else:
        def result():
            print("No. X is not equal to 69")

    return result


checkme = check(69)
checkme()
