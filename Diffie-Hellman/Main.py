import random, DiffieHellman

class Main:
    def main():
        # I have chosen extra smaller range for the numbers (1 -> 1000), 
        # so that the calculation time keeps shorter
        p = random.randint(1, 1000)
        g = random.randint(1, 1000)
        dh = DiffieHellman.DiffieHellman(p, g)
        firstKey, secondKey = dh.keyExchange()
        if firstKey == secondKey:
            print(f"The secret key from Bob: {firstKey}\nis the same secret key from Alice: {secondKey}")
        else:
            print("Error: The keys are different !!!")


if __name__ == '__main__':
    Main.main()