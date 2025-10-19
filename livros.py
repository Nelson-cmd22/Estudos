class Livro:
    def __init__(self, id, titulo, autor, disponivel=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    @classmethod
    def from_dict(cls, d):
        return cls(
            d['id'], 
            d['titulo'], 
            d['autor'], 
            d.get('disponivel', True)
        )

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'disponivel': self.disponivel
        }
