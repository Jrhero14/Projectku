class Solution:
    def intToRoman(self, num):
        print("==CONVERT NUMBERS TO ROMAN==")
        print("=======JeremiHero14=========")
        print("Your Input: " + str(num))
        Angka = int(num)
        Romawi = ""
        
        #Bilangan 1000
        while(Angka >= 900):
            if(1 <= (1000 - Angka) <=100):
                Angka = Angka % 900
                Romawi = Romawi + "CM"
            else:
                Seribu = Angka // 1000
                Angka = Angka % 1000
                for c in range(Seribu):
                    Romawi = Romawi + "M"
                    
        #Bilangan 500
        while(Angka >= 400):
            if(1 <= (500 - Angka) <=100):
                Angka = Angka % 400
                Romawi = Romawi + "CD"
            else:
                LimRatus = Angka // 500
                Angka = Angka % 500
                for c in range(LimRatus):
                    Romawi = Romawi + "D"
                    
        #Bilangan 100
        while(Angka >= 90):
            if(1 <= (100 - Angka) <=10):
                Angka = Angka % 90
                Romawi = Romawi + "XC"
            else:
                Seratus = Angka // 100
                Angka = Angka % 100
                for c in range(Seratus):
                    Romawi = Romawi + "C"
                    
        #Bilangan 50
        while(Angka >= 40):
            if(1 <= (50 - Angka) <= 10):
                Angka = Angka % 40
                Romawi = Romawi + "XL"
            else:
                LimaPuluh = Angka // 50
                Angka = Angka % 50
                for l in range(LimaPuluh):
                    Romawi = Romawi + "L"
                    
        #Bilangan 10
        while (Angka >= 9):
            if((10 - Angka) == 1):
                Angka = Angka % 9
                Romawi = Romawi + "IX"
            else:
                Puluhan = Angka // 10
                Angka = Angka % 10
                for p in range(Puluhan):
                    Romawi = Romawi + "X"
                    
        #Bilangan 5
        while (Angka >= 4):
            if((5 - Angka) == 1):
                Angka = Angka % 4
                Romawi = Romawi + "IV"
            else:
                Limaan = Angka // 5
                Angka = Angka % 5
                for v in range(Limaan):
                    Romawi = Romawi + "V"
                    
        # Bilangan satuan
        Satuan = Angka // 1
        Angka = Angka % 1
        for i in range(Satuan):
            Romawi = Romawi + "I"
            
        print("Roman numerals: " + Romawi)
        return Romawi

A = Solution()
A.intToRoman(24)
