class FilaPrioridadeMaxima:
    def __init__(self, elementos=None):
        self.fila = []
        if elementos:
            for elem in elementos:
                self.inserir(elem)

    def _heapify_up(self, index):  # Função auxiliar para subir o elemento até sua posição correta
        while index > 0:
            pai = (index - 1) // 2
            if self.fila[index] > self.fila[pai]:
                # Troca os elementos
                self.fila[index], self.fila[pai] = self.fila[pai], self.fila[index]
                index = pai
            else:
                break

    def _heapify_down(self, index):  # Função auxiliar para descer o elemento até sua posição correta
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

    def inserir(self, elemento):  # Adiciona o novo elemento ao final da fila
        self.fila.append(elemento)
        # Mantém a propriedade de heap, subindo o elemento para a posição correta
        self._heapify_up(len(self.fila) - 1)

    def remover_maximo(self):  # Remove e retorna o elemento de maior prioridade (primeiro da fila)
        if not self.fila:
            return None  # Retorna None se a fila estiver vazia
        if len(self.fila) == 1:
            return self.fila.pop(0)  # Se a fila tem apenas um elemento, apenas remove

        # Troca o primeiro elemento (máximo) com o último e remove o último
        max_elem = self.fila[0]
        self.fila[0] = self.fila.pop()
        # Restaura a propriedade de heap descendo o novo elemento para sua posição correta
        self._heapify_down(0)
        return max_elem

    def mostrar_maximo(self):  # Retorna o elemento de maior prioridade (o primeiro da lista)
        if self.fila:
            return self.fila[0]
        return None

    def atualizar_prioridade(self, elemento_antigo, novo_elemento):  # Substitui um elemento e garante que a propriedade de heap seja mantida
        try:
            index = self.fila.index(elemento_antigo)
            self.fila[index] = novo_elemento
            if novo_elemento > elemento_antigo:
                self._heapify_up(index)  # Se o novo elemento é maior, sobe
            else:
                self._heapify_down(index)  # Se o novo elemento é menor, desce
        except ValueError:
            return None

    def remover_elemento(self, elemento):  # Remove um elemento específico e restaura a propriedade de heap
        try:
            index = self.fila.index(elemento)
            self.fila[index] = self.fila[-1]  # Substitui o elemento pelo último
            self.fila.pop()  # Remove o último elemento
            if index < len(self.fila):
                # Restaura a propriedade de heap
                self._heapify_up(index)
                self._heapify_down(index)
        except ValueError:
            return None

    def tamanho_fila(self):  # Retorna o número de elementos na fila
        return len(self.fila)

    def fila_vazia(self):  # Verifica se a fila está vazia
        return len(self.fila) == 0

    def limpar_fila(self):  # Limpa todos os elementos da fila
        self.fila = []

# Função para solicitar os números ao usuário
def solicitar_numeros():
    numeros = []
    while True:
        try:
            entrada = input("Digite um número para inserir na fila (ou 'sair' para finalizar): ")
            if entrada.lower() == 'sair':
                break
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, insira um número válido ou 'sair' para finalizar.")
    return numeros

# Solicita os números ao usuário
numeros = solicitar_numeros()

# Cria a fila e realiza as operações
fila = FilaPrioridadeMaxima(numeros)

print("\nMáximo na fila:", fila.mostrar_maximo())  # Exibe o maior número

# Remover o elemento de maior prioridade
print("Removendo o máximo:", fila.remover_maximo())  # Exibe o maior número removido
print("Máximo após remoção:", fila.mostrar_maximo())  # Exibe o próximo maior número

# Atualizar a prioridade de um elemento
fila.atualizar_prioridade(5, 25)
print("Máximo após atualização:", fila.mostrar_maximo())  # Exibe o novo máximo

# Remover um elemento específico
fila.remover_elemento(25)
print("Fila após remoção de 25:", fila.fila)

# Verificar se a fila está vazia
print("Fila vazia?", fila.fila_vazia())  # Exibe False

# Limpar a fila
fila.limpar_fila()
print("Fila após limpar:", fila.fila)  # Exibe []
