from ClaseFechaHora import FechaHora

class Hora:

    __hs = 0
    __min = 0
    __seg = 0

    def __init__(self, hs=0, min=0, seg=0):
        self.__hs = hs
        self.__min = min
        self.__seg = seg

    def Mostrar(self):
        print('%.2d:%.2d:%.2d' % (self.__hs, self.__min, self.__seg))
        self.validaEntrada(self.__hs, self.__min, self.__seg)

    def validaEntrada(self, hs, min, seg):
        valido = False
        if hs in range(0, 24):
            if min in range(0, 60):
                if seg in range(0, 60):
                    valido = True
        if valido:
            print('La fecha y la hora ingresadas son válidas')
        else:
            print('La fecha y la hora ingresadas no son válidas')
        return valido

    def getHora(self):
        return self.__hs

    def getMin(self):
        return self.__min

    def getSeg(self):
        return self.__seg

    def __add__(self, otro):
        h = self.__hs + otro.getHora()
        m = self.__min + otro.getMin()
        s = self.__seg + otro.getSeg()
        return FechaHora(otro.getDia(), otro.getMes(), otro.getAño(), h, m, s)

    def __radd__(self, otro):
        return FechaHora(otro.getDia(), otro.getMes(), otro.getAño(), self.__hs + otro.getHora(),
                         self.__min + otro.getMin(), self.__seg + otro.getSeg())