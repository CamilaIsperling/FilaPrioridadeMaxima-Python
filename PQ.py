class FilaPrioridadeMaxima:
    def __init__(self):
        self.fila = []

    def inserir(self, elemento):
        # Adiciona o elemento e ordena a fila em ordem decrescente
        self.fila.append(elemento)
        self.fila.sort(reverse=True)

    def remover_maximo(self):
        # Remove e retorna o elemento de prioridade máxima (primeiro da lista)
        if self.fila:
            return self.fila.pop(0)
        else:
            return None  # Retorna None se a fila estiver vazia

    def mostrar_fila(self):
        # Exibe os elementos na fila
        print("Fila de prioridade máxima:", self.fila)


# Testando a implementação
fila_prioridade = FilaPrioridadeMaxima()
fila_prioridade.inserir(10)
fila_prioridade.inserir(5)
fila_prioridade.inserir(20)
fila_prioridade.inserir(15)


fila_prioridade.mostrar_fila()

print("Elemento de prioridade máxima removido:", fila_prioridade.remover_maximo())
print("Elemento de prioridade máxima removido:", fila_prioridade.remover_maximo())
fila_prioridade.mostrar_fila()
