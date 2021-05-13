class FechaHora:
    __dd = 0
    __mm = 0
    __aa = 0
    __hs = 0
    __min = 0
    __seg = 0

    def __init__(self, dd=1, mm=1, aa=2020, hs=0, min=0, seg=0):
        self.__dd = dd
        self.__mm = mm
        self.__aa = aa
        self.__hs = hs
        self.__min = min
        self.__seg = seg

    def Mostrar(self):
        print('%.2d/%.2d/%.2d\t -\t %.2d:%.2d:%.2d' % (self.__dd, self.__mm, self.__aa,
                                                       self.__hs, self.__min, self.__seg))
        self.validaEntrada(self.__dd, self.__mm, self.__aa, self.__hs, self.__min, self.__seg)

    def validaEntrada(self, dd, mm, aa, hs, min, seg):
        valido = False
        if hs in range(0, 24):
            if min in range(0, 60):
                if seg in range(0, 60):
                    if mm in [1, 3, 5, 7, 8, 10, 12]:
                        if dd in range(1, 32):
                            valido = True
                    elif mm in [4, 6, 9, 11]:
                        if dd in range(1, 31):
                            valido = True
                    elif mm == 2:
                        bisiesto = self.bisiesto(aa)
                        if bisiesto:
                            if dd in range(1, 30):
                                valido = True
                        else:
                            if dd in range(1, 29):
                                valido = True
        if valido:
            print('La fecha y la hora ingresadas son válidas')
        else:
            print('La fecha y la hora ingresadas no son válidas')
        return valido

    def bisiesto(self, aa):
        bisiesto = False
        if aa % 4 == 0 and (aa % 100 != 0 or aa % 400 == 0):
            bisiesto = True
        return bisiesto

    def __sub__(self, otro):
        if type(otro)==int:
            return FechaHora(self.__dd - otro, self.__mm, self.__aa, self.__hs, self.__min, self.__seg)

    def __radd__(self, otro):
        if type(otro)==int:
            return FechaHora(self.__dd + otro, self.__mm, self.__aa, self.__hs, self.__min, self.__seg)
    
    def getDia(self):
        return self.__dd

    def getMes(self):
        return self.__mm

    def getAño(self):
        return self.__aa

    def getHora(self):
        return self.__hs

    def getMin(self):
        return self.__min

    def getSeg(self):
        return self.__seg