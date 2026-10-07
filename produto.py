class Produto:
    def __init___(self, codigo=None, nome=None, quantidade=None, preco=None, tipo=None):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.tipo = tipo

        def listrar_produtos(self):
          return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "tipo": self.tipo,
            "situacao": self.situacao(),
        }
        def situacao(self):
           if self.quantidade == 0:
              return "Em falta"
           elif self.quantidade <= 1:
              return "Repor"
           else:
              return "ok"

        
        