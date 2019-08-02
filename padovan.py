class padovan:
    _numeroanterior1 = 0
    _numeroanterior2 = 1
    _numeroanterior3 = 1
    _numeropadovan = 0
    _numeroVecesLlamado = 0
    _valor = 0
   
    def __init__(self):
        self._numeroanterior1 = 1
        self._numeroanterior2 = 1
        self._numeroanterior3 = 1
        self._numeropadovan = 0
        self._numeroVecesLlamado = 0
        self._valor = 0
        
    def siguiente(self):
        self.avanzar()
        self._numeroVecesLlamado += 1
        return self._numeropadovan
    
    def numeropadovan(self):
        return self.valor
    
    def actualizarRetroceder(self):
        if self._numeroVecesLlamado == 0 or self._numeroVecesLlamado == 1 or self._numeroVecesLlamado == 2:
           self._numeropadovan = 1

        if self._numeroVecesLlamado >= 3:
           self._numeropadovan = self._numeroanterior3
           self._numeroanterior3 = self._numeroanterior2
           self._numeroanterior2 = self._numeroanterior1
           

    def anterior(self):
        self.actualizarRetroceder()
        self._numeroVecesLlamado -= 1
        self._valor = self._numeropadovan
        return  self._numeropadovan

    
    def avanzar(self):
        if self._numeroVecesLlamado == 0 or self._numeroVecesLlamado == 1 or self._numeroVecesLlamado == 2:
           self._numeropadovan = 1
        
        if self._numeroVecesLlamado >= 3:
            self._numeroanterior1 = self._numeroanterior2
            self._numeroanterior2 = self._numeroanterior3
            self._numeroanterior3 = self._numeropadovan
            self._numeropadovan = self._numeroanterior1 + self._numeroanterior2 
            
        self.valor = self._numeropadovan
        self._numeroVecesLlamado += 1
        return self._numeropadovan

