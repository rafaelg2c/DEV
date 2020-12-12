import sys

def letter(output):
    result = "tu letra" + output 
    return result

if __name__ == "__main__":  
    try:
        name = input(str(sys.argv[1]))
    except (IndexError, ValueError) as e:

        print("ingresa una letra")
        print("ejemplo, sys.py w")
        sys.exit(1)

    resultado = letter(name)
    print(resultado)