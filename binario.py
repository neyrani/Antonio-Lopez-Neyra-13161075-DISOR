 
class binario:
 _binario = ''
 

 def __init__(self):
    self._binario = ''
    

 def binarizar(self, decimal):
    self._binario = ''
    while decimal // 2 != 0:
        self._binario = str(decimal % 2) + self._binario
        decimal = decimal // 2
    return str(decimal) + self._binario
 

