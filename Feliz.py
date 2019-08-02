class NumeroFeliz:

    def esfeliz(self, numero):
        feliz = 0
        for alg in numero:
            feliz += int(alg) **2

        if feliz == 1:
            return "numero feliz"
        elif feliz < 10:
            return "numero infeliz: " + str(feliz)
        else:
            resultado = NumeroFeliz()
            return resultado.esfeliz(str(feliz))

numero = 7
feliz = NumeroFeliz()

print(feliz.esfeliz(str(numero)))           