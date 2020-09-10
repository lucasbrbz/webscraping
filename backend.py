class Backend():
    chave = None
    lista = None
    flag = None

    @property
    def chave(self):
        return self._chave

    @chave.setter
    def chave(self,value):
        self._chave = value

    @property
    def lista(self):
        return self._lista

    @lista.setter
    def lista(self, value):
        self._lista = value