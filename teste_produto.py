from produto import Produto

p1 = Produto()
p1.nome ="Coca cola"
p1.quantidade = 100
p1.preco = 10
p1.tipo = "refrigerante"
p1.codigo = 65489


p2 = Produto()
p2.nome="pizza de frango"
p2.quantidade = 50
p2.preco = 15
p2.tipo = "pizza"
p2.codigo = 23450


p3 = Produto()
p3.nome="uva croc croc"
p3.quantidade = 150
p3.preco = 10
p3.tipo = "fruta"
p3.codigo = 95447

print(f"{p1.nome}: {p1.quantidade} un.")
print(f"{p2.nome}: {p2.quantidade} un.")
print(f"{p3.nome}: {p3.quantidade} un.")


