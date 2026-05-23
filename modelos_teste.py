class Cliente:
    def __init__(self, nome: str, endereco: str, telefone: str, email: str) -> None:
        self.nome: str = nome
        self.endereco: str = endereco
        self.telefone: str = telefone
        self.email: str = email

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Endereço: {self.endereco}, Telefone: {self.telefone}, Email: {self.email}"
    
class Pedido:
    def __init__(self, codigo: int, data: str, status: str, total: float) -> None:
        self.codigo: int = codigo
        self.data: str = data
        self.status: str = status
        self.total: float = total

    def __str__(self) -> str:
        return f"Código: {self.codigo}, Data: {self.data}, Status: {self.status}, Total: R$ {self.total:.2f}"

class ItemPedido:
    def __init__(self, id_item: int, preco: float, quantidade: int) -> None:
        self.id_item: int = id_item
        self.preco: float = preco
        self.quantidade: int = quantidade

    def total_item(self) -> float:
        return self.preco * self.quantidade

    def __str__(self) -> str:
        return f"Id_item: {self.id_item}, Preço: R$ {self.preco:.2f}, Quantidade: {self.quantidade}"
    
class Produto:
    def __init__(self, id_produto: int, nome: str, tipo: str, descricao: str) -> None:
        self.id_produto: int = id_produto
        self.nome: str = nome
        self.tipo: str = tipo # esse atributo pode ter dois valores: fixo ou variável
        self.descricao: str = descricao

    def __str__(self) -> str:
        return f"Id_produto: {self.id_produto}, Nome: {self.nome}, Tipo: {self.tipo}, Descrição: {self.descricao}"