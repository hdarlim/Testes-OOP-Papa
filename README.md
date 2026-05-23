![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)

Projeto de exemplo com modelos simples: `Cliente`, `Pedido`, `ItemPedido`, `Produto`.

Uso rápido (exemplo):

```python
from modelos_teste import Cliente, ItemPedido, Pedido, Produto

novo_cliente = Cliente(1, "João", "Rua dos Bobos, 0", "119928342", "email@example.com", "senhacompletamentesegura")
produto = Produto(456, "Iogurte natural", "Fixo", "Iogurte natural sem conservantes feito com muito amor!")
item = ItemPedido(1, 20.0, 3)
pedido = Pedido(123, "2026-05-21", "Pago", item.total_item())

print(novo_cliente)
print(produto)
print(item)
print(pedido)
```

Observações:
- Nenhuma modificação com IA realizada.
- Execute com Python 3.8+ em um virtualenv.