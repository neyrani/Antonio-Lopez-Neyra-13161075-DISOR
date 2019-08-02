

class hexadecimal:


     def DecimalAHexadecimal(self, decimal):
        
        hexadecimal = ""
        while decimal != 0: 
            rem = self.CambiarDigitos(decimal % 16)
            hexadecimal = str(rem) + hexadecimal
            decimal = int(decimal / 16)
        return hexadecimal    
       

     def CambiarDigitos(self, digitos):
        decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
        hexadecimal = ["A", "B", "C", "D", "E", "F"]
        for c in range(7):
            if digitos == decimales[c - 1]:
                digitos = hexadecimal[c - 1]
        return digitos



    