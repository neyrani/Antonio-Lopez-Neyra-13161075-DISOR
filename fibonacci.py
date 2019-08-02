class fibonacci:
    _numeroAnterior = 0
    _numeroActual = 0
    _numeroVecesLlamado = 0
    _valor = 0
   
    def __init__(self):
        self._numeroAnterior = 0
        self._numeroActual = 0
        self._numeroVecesLlamado = 0
        self._valor = 0
        
    def siguiente(self):
        self.avanzar()
        self._numeroVecesLlamado += 1
        return self._numeroActual
    
    def numerofibonacci(self):
        return self.valor

    def actualizarRetroceder(self):
        if self._numeroActual == 0:
         self._numeroAnterior = 0 
        relpaldoNumeroActual = self._numeroActual
        self._numeroActual = self._numeroAnterior
        self._numeroAnterior = relpaldoNumeroActual - self._numeroActual  
        

    def anterior(self):
        self.actualizarRetroceder()
        self._numeroVecesLlamado -= 1
        return  self._numeroActual
    
    def avanzar(self):
        if self._numeroVecesLlamado == 0:
            self._numeroActual = 0

        if self._numeroVecesLlamado == 1:
            self._numeroActual = 1

        if self._numeroVecesLlamado >= 2:
            almacenarNumeroAnterior = self._numeroAnterior
            self._numeroAnterior = self._numeroActual
            self._numeroActual = self._numeroAnterior + almacenarNumeroAnterior

        self.valor = self._numeroActual
        self._numeroVecesLlamado += 1
        return self._numeroActual

   
