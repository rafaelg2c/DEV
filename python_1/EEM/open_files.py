with open ("test.txt", "r") as arch:
    data = arch.readlines()
    for m in data:
        word = m.split()
        print(word)
