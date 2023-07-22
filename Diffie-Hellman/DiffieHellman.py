import random

class DiffieHellman:
    def __init__(self, p, g):
        self.p = p
        self.g = g
        

    def keyExchange(self):
        # generate the private Key for Bob and Alice
        bobKey = random.randint(1, self.g)
        aliceKey = random.randint(1, self.g)

        #Calculation of the public key (Encrypt)
        pubKeyBob = ((pow(self.g,bobKey))%self.p)
        pubKeyAlice = ((pow(self.g,aliceKey))%self.p)

        #Calculation of the secret key (Dencrypt)
        priKeyBob = ((pow(pubKeyAlice,bobKey))%self.p)
        priKeyAlice = ((pow(pubKeyBob,aliceKey))%self.p)

        # return both  keys to check up
        return priKeyBob, priKeyAlice