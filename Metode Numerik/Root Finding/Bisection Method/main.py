class pers:

    def __init__(self, xa, xb, cons):
        self.xa = float(xa)
        self.xb = float(xb)
        self.cons = float(cons)
        self.x = 0


    def func(self, x):
        return float(self.xa*(x*x) + self.xb*(x) + self.cons)

    def solve(self, a, b):
        print("Pers "+ str(int(self.xa))+"X^2" + str(int(self.xb))+"X"+ str(int(self.cons)))
        a1 = a
        b1 = b
        a = self.func(a)
        b = self.func(b)
        if((a*b)>0):
            print("Akar persamaan tidak ada dalam rentang itu")
            return 0
        else:
            print("Akar persamaan ada dalam rentang itu")
        c1 = (a1+b1)/2.0
        c = self.func(c1)
        if(a*c < 0):
            b1 = c1
            c1 = (a1+b1)/2.0
        elif(a*c>0):
            a1 = c1
            c1 = (a1+b1)/2.0
        a = self.func(a1)
        b = self.func(b1)
        c = self.func(c1)
        while(c != 0):
            if (a * c < 0):
                b1 = c1
                c1 = (a1 + b1) / 2.0
            elif (a * c > 0):
                a1 = c1
                c1 = (a1 + b1) / 2.0
            a = self.func(a1)
            b = self.func(b1)
            c = self.func(c1)


        print("Akar persamaannya adalah X = "+ str(c1))




a = pers(2, 7, -5)
a.solve(0.5, 1)