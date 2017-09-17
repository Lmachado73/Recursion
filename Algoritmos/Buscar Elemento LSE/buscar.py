class LSE:
    def __init__(self, informacao = None, proximo = None):
        self.informacao = informacao
        self.proximo = proximo

    def __str__(self):
        return str(self.informacao)


def exibirLista(lista):
     if lista != None:
         print(lista, end=" ")
         exibirLista(lista.proximo)
     else:
         print() # Pular linha no final

def exibirListaInvertida(lista):
     if lista != None:
         exibirListaInvertida(lista.proximo)
         print(lista, end=" ")
     else:
         print() # Pular linha no final
         

def buscar(lista, informacao):
   if lista == None or lista.informacao == informacao:
      return lista
   else:
      return buscar(lista.proximo, informacao)


lista = LSE(1, LSE(2, LSE(3, None)))

exibirListaInvertida(lista)


