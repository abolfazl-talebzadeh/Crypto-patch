class DH:
    primes={2,3}
    def __init__(self, n, g):
        self.n=n
        self.g=g
        return
    def primes_gen(self):
        primes_set1=set()
        primes_set2=set()
        for i in range (1,((self.n-1)//6)+1):
            primes_set1.add((6*i)-1)
            primes_set2.add((6*i)+1)
        temp=primes_set2.union(primes_set1)
        print(temp)
        temp2=self.primes.union(temp)
        return temp2
d=DH(10,2)
print(d.primes_gen())