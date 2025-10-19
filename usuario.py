class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    @classmethod
    def from_dict(cls, d):
        return cls(d['id'], d['nome'])

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome
        }
