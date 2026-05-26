from classes import Cliente, ItemPedido, Pedido, Produto

def main() -> None:
    # teste
    novo_cliente = Cliente(1, "João", "Rua dos Bobos, 0", "119928342", "email@example.com", "senhacompletamentesegura")
    produto = Produto(456, "Iogurte natural", "Fixo", "Iogurte natural sem conservantes feito com muito amor!")
    item = ItemPedido(1, 20.0, 3)
    pedido = Pedido(123, "2026-05-21", "Pago", item.total_item())

    print(novo_cliente)
    print(produto)
    print(item)
    print(pedido)

if __name__ == "__main__":
    main()