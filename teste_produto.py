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

print(p1.listar_produtos())
p1.entrada(30)
print(p1.listar_produtos())

p1.saida(15)
print(p1.listar_produtos())
if p1.saida(100):
    print("saida registrada")
else:
    print("saida recusada")
print(p1.quantidade)
