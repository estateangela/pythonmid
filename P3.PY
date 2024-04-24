while True:
    userinput = input()
    if int(userinput) < 0:
        break
    print(int(userinput[::-1]))