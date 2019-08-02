
class capicua():
    _capicua = ""

    def __init__(self):
        self._capicua = ""

    def capicua(self, decimal):
        if decimal <= 9:
           self._capicua = "No capicua"
        #return  self._capicua
        #return "No capicua" 

        if decimal > 9:
         self.calculoCapicua(decimal)
           


    def calculoCapicua(self, numero):
        valor = 0
        invertir = 0
        cifra = 0
        valor = numero
        while valor != 0:
            cifra = valor % 10
            invertir = invertir * 10 + cifra
            valor = valor / 10
        if numero != invertir:
           self._capicua = "No capicua"
           #return self._capicua
           #return "No capicua"

        if numero == invertir:
           self._capicua = "Capicua"
           #return self._capicua
           #return "Capicua"

    def resultadoCapicua(self):
        return self._capicua

    
cap = capicua()
print(cap.capicua(161))
print(cap.resultadoCapicua())

