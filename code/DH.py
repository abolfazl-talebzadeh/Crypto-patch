import random
class DH:
    primes=[]
    q_primes=[]
    p=0
    y=0
    a=0
    def __init__(self, n,g):
        self.n=n
        #self.x=x
        self.g=g
        self.primes_gen()
        self.p_creator()
        self.q_assigner()
        return
    ##############################
    def primes_gen(self):
        is_prime=True
        for i in range (2,self.n):
            for j in range(2,i):
                if i % j ==0:
                    is_prime=False
                    break
                else:
                    is_prime=True
            if is_prime==True:
                self.primes.append(i)
                is_prime=False
    #################################
    def p_creator(self):
        self.q_primes=[(2*self.primes[i])+1 for i in range (0,len(self.primes)-1)]
    ####################################
    def q_assigner(self):
        pos=random.randint(0,len(self.primes)-1)
        self.p=self.primes[pos]-1
    #####################################
    def secret_number_generattor(self):
        self.a=random.randint(1,self.p)
        self.y=(self.g**self.a)%(self.p)
    ######################################
d=DH(90,2)
#print(d.primes_gen())
d.secret_number_generattor()

print("prime number chosen: {}, number chosen 1<x<p-1: {}, g ^ x mod p:{}".format(d.p,d.a,d.y))
d.secret_number_generattor()
print("prime number chosen: {}, number chosen 1<x<p-1: {}, g ^ x mod p:{}".format(d.p,d.a,d.y))