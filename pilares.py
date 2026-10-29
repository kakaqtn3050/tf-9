from abc import ABC, abstractmethod


class Medivel(ABC):
    @property
    @abstractmethod
    def tamanho(self) -> int:
        pass


class Item(Medivel):
    def __init__(self, nome: str, pai=None):
        self.nome = nome
        self.pai = pai

    @property
    def caminho(self) -> str:
        if self.pai is None:
            return self.nome
        return f"{self.pai.caminho}/{self.nome}"


class Arquivo(Item):
    def __init__(self, nome: str, tamanho: int, pai=None):
        super().__init__(nome, pai)
        self._tamanho = tamanho

    @property
    def tamanho(self) -> int:
        return self._tamanho


class Pasta(Item):
    def __init__(self, nome: str, pai=None):
        super().__init__(nome, pai)
        self.filhos = []

    def adicionar(self, item: Item):
        item.pai = self
        self.filhos.append(item)

    def remover(self, item: Item):
        if item in self.filhos:
            self.filhos.remove(item)
            item.pai = None

    @property
    def tamanho(self) -> int:
        return sum(f.tamanho for f in self.filhos)


class Lixeira(Pasta):
    def __init__(self, nome: str = "Lixeira", pai=None):
        super().__init__(nome, pai)

    def esvaziar(self):
        self.filhos.clear()


def espaco_total(*itens: Medivel) -> int:
    return sum(item.tamanho for item in itens)


def tentar(funcao, *args, **kwargs):
    try:
        return funcao(*args, **kwargs)
    except Exception as e:
        print(f"Erro ao executar {funcao.__name__}: {e}")
        from abc import ABC, abstractmethod


class Medivel(ABC):
    @property
    @abstractmethod
    def tamanho(self) -> int:
        pass


class Item(Medivel):
    def __init__(self, nome: str, pai=None):
        self.nome = nome
        self.pai = pai

    @property
    def caminho(self) -> str:
        if self.pai is None:
            return self.nome
        return f"{self.pai.caminho}/{self.nome}"


class Arquivo(Item):
    def __init__(self, nome: str, tamanho: int, pai=None):
        super().__init__(nome, pai)
        self._tamanho = tamanho

    @property
    def tamanho(self) -> int:
        return self._tamanho


class Pasta(Item):
    def __init__(self, nome: str, pai=None):
        super().__init__(nome, pai)
        self.filhos = []

    def adicionar(self, item: Item):
        item.pai = self
        self.filhos.append(item)

    def remover(self, item: Item):
        if item in self.filhos:
            self.filhos.remove(item)
            item.pai = None

    @property
    def tamanho(self) -> int:
        return sum(f.tamanho for f in self.filhos)


class Lixeira(Pasta):
    def __init__(self, nome: str = "Lixeira", pai=None):
        super().__init__(nome, pai)

    def esvaziar(self):
        self.filhos.clear()


class Atalho(Item):
    __slots__ = ('__destino',)

    def __init__(self, nome: str, destino: Item, pai=None):
        super().__init__(nome, pai)
        self.__destino = destino

    @property
    def destino(self) -> Item:
        return self.__destino

    @property
    def tamanho(self) -> int:
        return 0


def espaco_total(*itens: Medivel) -> int:
    return sum(item.tamanho for item in itens)


def tentar(funcao, *args, **kwargs):
    try:
        return funcao(*args, **kwargs)
    except Exception as e:
        print(f"Erro ao executar {funcao.__name__}: {e}")