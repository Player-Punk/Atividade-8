from abc import ABC, abstractmethod

class Categoria:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def getInformacoes(self):
        return f"ID: {self.id}, Nome: {self.nome}, Descrição: {self.descricao}"

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco:.2f}, Categoria: {self.categoria.getInformacoes()}"

    @abstractmethod
    def cadastrar(self):
        pass

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte, processador, memoriaRAM):
        super().__init__(modelo, cor, preco, categoria)
        self.potenciaDaFonte = potenciaDaFonte
        self.processador = processador
        self.memoriaRAM = memoriaRAM

    def getInformacoes(self):
        return super().getInformacoes() + f", Potência da Fonte: {self.potenciaDaFonte}, Processador: {self.processador}, Memória RAM: {self.memoriaRAM}GB"

    def cadastrar(self):
        # Lógica para cadastrar um desktop
        pass

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria, processador, memoriaRAM, armazenamento):
        super().__init__(modelo, cor, preco, categoria)
        self.tempoDeBateria = tempoDeBateria
        self.processador = processador
        self.memoriaRAM = memoriaRAM
        self.armazenamento = armazenamento

    def getInformacoes(self):
        return super().getInformacoes() + f", Tempo de Bateria: {self.tempoDeBateria}, Processador: {self.processador}, Memória RAM: {self.memoriaRAM}GB, Armazenamento: {self.armazenamento}"

    def cadastrar(self):
        # Lógica para cadastrar um notebook
        pass

# Exemplo de uso:

# Criando uma categoria
categoria1 = Categoria(1, "Eletrônicos", "Categoria que engloba produtos eletrônicos")

# Criando um desktop
desktop1 = Desktop("Desktop Modelo i7", "Preto", 2500, categoria1, "500W", "Intel Core i7", 16)

# Criando um notebook
notebook1 = Notebook("Notebook Modelo g15", "Prata", 3000, categoria1, "8 horas", "AMD Ryzen 5", 8, "512GB SSD")

# Exibindo informações dos produtos
print(desktop1.getInformacoes())
print(notebook1.getInformacoes())
