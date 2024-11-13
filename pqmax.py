class FilaPrioridadeMaxima:
    def __init__(self):
        self.fila = []

    def _heapify_up(self, index):
        # Função auxiliar para subir o elemento até sua posição correta
        while index > 0:
            pai = (index - 1) // 2
            if self.fila[index] > self.fila[pai]:
                # Troca os elementos
                self.fila[index], self.fila[pai] = self.fila[pai], self.fila[index]
                index = pai
            else:
                break

    def _heapify_down(self, index):
        # Função auxiliar para descer o elemento até sua posição correta
        size = len(self.fila)
        while 2 * index + 1 < size:  # Enquanto o nó tiver filhos
            filho_esquerdo = 2 * index + 1
            filho_direito = 2 * index + 2
            maior = index

            if filho_esquerdo < size and self.fila[filho_esquerdo] > self.fila[maior]:
                maior = filho_esquerdo
            if filho_direito < size and self.fila[filho_direito] > self.fila[maior]:
                maior = filho_direito

            if maior != index:
                # Troca os elementos
                self.fila[index], self.fila[maior] = self.fila[maior], self.fila[index]
                index = maior
            else:
                break

    def inserir(self, elemento):
        # Adiciona o novo elemento ao final da fila
        print(f"Inserindo {elemento} na fila de prioridade.")
        self.fila.append(elemento)
        self._heapify_up(len(self.fila) - 1)

    def remover_maximo(self):
        # Remove e retorna o elemento de maior prioridade (primeiro da fila)
        if not self.fila:
            print("A fila está vazia, nada a remover.")
            return None
        if len(self.fila) == 1:
            max_elem = self.fila.pop(0)
            print(f"Removendo o único elemento na fila: {max_elem}")
            return max_elem

        max_elem = self.fila[0]
        self.fila[0] = self.fila.pop()
        self._heapify_down(0)
        print(f"Removendo o elemento de prioridade máxima: {max_elem}")
        return max_elem

    def mostrar_maximo(self):
        # Retorna o elemento de maior prioridade (o primeiro da lista)
        if self.fila:
            print(f"Elemento de prioridade máxima na fila: {self.fila[0]}")
            return self.fila[0]
        print("A fila está vazia.")
        return None

    def atualizar_prioridade(self, elemento_antigo, novo_elemento):
        # Substitui um elemento e garante que a propriedade de heap seja mantida
        try:
            index = self.fila.index(elemento_antigo)
            self.fila[index] = novo_elemento
            print(f"Atualizando o elemento {elemento_antigo} para {novo_elemento}.")
            if novo_elemento > elemento_antigo:
                self._heapify_up(index)
            else:
                self._heapify_down(index)
        except ValueError:
            print(f"Elemento {elemento_antigo} não encontrado na fila.")
            return None

    def remover_elemento(self, elemento):
        # Remove um elemento específico e restaura a propriedade de heap
        try:
            index = self.fila.index(elemento)
            print(f"Removendo elemento específico {elemento} da fila.")
            self.fila[index] = self.fila[-1]
            self.fila.pop()
            if index < len(self.fila):
                self._heapify_up(index)
                self._heapify_down(index)
        except ValueError:
            print(f"Elemento {elemento} não encontrado na fila.")
            return None

    def tamanho_fila(self):
        # Retorna o número de elementos na fila
        return len(self.fila)

    def fila_vazia(self):
        # Verifica se a fila está vazia
        return len(self.fila) == 0

    def limpar_fila(self):
        # Limpa todos os elementos da fila
        print("Limpando todos os elementos da fila.")
        self.fila = []

# implementação
fila = FilaPrioridadeMaxima()
fila.inserir(10)
fila.inserir(5)
fila.inserir(40)
fila.inserir(30)

print("Fila após inserções:", fila.fila)
fila.mostrar_maximo()  # Exibe o maior elemento

# Remove o elemento de maior prioridade
fila.remover_maximo()
print("Fila após remoção do máximo", fila.fila)
fila.mostrar_maximo()  # Exibe o novo maior elemento

# Atualiza a prioridade de um elemento
fila.atualizar_prioridade(5, 25)
print("Fila após troca de prioridades:", fila.fila)
fila.mostrar_maximo()  # Exibe o novo maior elemento

# Remove um elemento específico
fila.remover_elemento(25)
print("Fila atual:", fila.fila)

# Verifica se a fila está vazia
print("Fila está vazia?", fila.fila_vazia())

# Limpa a fila
fila.limpar_fila()
print("Fila após limpeza:", fila.fila)
