import random
class DH:
    primes=[]
    p=0
    ya=0
    yb=0
    k=0
    a=0
    b=0
    def __init__(self, n,g):
        self.n=n
        self.g=g
        self.primes_gen()
        self.q_assigner()
        self.g_calculator()
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
    ####################################
    def q_assigner(self):
        pos=random.randint(0,len(self.primes)-1)
        self.p=self.primes[pos]
    #####################################
    def g_calculator(self):
        generators=[]
        z=[]
        for x in range(1, self.p):
            z.append(x)
        for g in self.primes:
            if g<self.p:
                temp=[]
                for y in range(1, self.p):
                    temp.append((g**y)%self.p)
                temp.sort()
                temp_set=set(temp)
                if temp_set==set(z):
                    generators.append(g)
        self.g=generators[random.randint(0,len(generators)-1)]
        return generators
    #####################################
    def secret_number_generattor(self):
        self.a=random.randint(1,self.p-1)
        self.ya=(self.g**self.a)%(self.p)
        self.b=random.randint(1,self.p-1)
        self.yb=(self.g**self.b)%(self.p)
        if (self.ya ** self.b) % (self.p) == (self.yb ** self.a) % (self.p):
            self.k=(self.ya ** self.b) % (self.p)
            return self.k
        else:
            return float('NaN')
    ######################################
d=DH(90,2)
#print(d.primes_gen())
print("P= ", d.p)
print("Generators: ",d.g_calculator())
print("g= ",d.g, "** g is selected randomly among other numbers")
print("Secret Key (K):",d.secret_number_generattor())
print("Alice's private Key= ", d.a)
print("Alice's Publuc Key= ", d.ya)
print("Bob's private Key= ", d.b)
print("Alice's Publuc Key= ", d.yb)