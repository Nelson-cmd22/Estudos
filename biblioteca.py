import json
import os
from livros import Livro
from usuario import Usuario

class biblioteca:
    def __init__(self):
        self.livros = self.carregar_livros()
        self.usuarios = self.carregar_usuarios()
        os.makedirs('dados', exist_ok=True)  # Garante que a pasta exista

    def carregar_livros(self):
        caminho = 'dados/livros.json'
        if not os.path.exists(caminho):
            return []
        with open(caminho, "r") as f:
            return [Livro.from_dict(l) for l in json.load(f)]

    def salvar_livros(self):
        with open('dados/livros.json', 'w') as f:
            json.dump([l.to_dict() for l in self.livros], f, indent=4)

    def carregar_usuarios(self):
        caminho = 'dados/usuarios.json'
        if not os.path.exists(caminho):
            return []
        with open(caminho, "r") as f:
            return [Usuario.from_dict(u) for u in json.load(f)]

    def salvar_usuarios(self):
        with open('dados/usuarios.json', 'w') as f:
            json.dump([u.to_dict() for u in self.usuarios], f, indent=4)

    def gerar_id_livro(self):
        if not self.livros:
            return 1
        return max(l.id for l in self.livros) + 1

    def gerar_id_usuario(self):
        if not self.usuarios:
            return 1
        return max(u.id for u in self.usuarios) + 1

    def adicionar_livro(self, titulo, autor):
        novo_id = self.gerar_id_livro()
        livro = Livro(novo_id, titulo, autor)
        self.livros.append(livro)
        self.salvar_livros()
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def listar_livros(self):
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"[{livro.id}] {livro.titulo} - {livro.autor} ({status})")

    def adicionar_usuario(self, nome):
        novo_id = self.gerar_id_usuario()
        usuario_novo = Usuario(novo_id, nome)
        self.usuarios.append(usuario_novo)
        self.salvar_usuarios()
        print(f"Usuário '{nome}' cadastrado com sucesso!")

    def emprestar_livro(self, id_livro):
        for livro in self.livros:
            if livro.id == id_livro:
                if livro.disponivel:
                    livro.disponivel = False
                    self.salvar_livros()
                    print(f"Livro '{livro.titulo}' emprestado!")
                else:
                    print("Livro já está emprestado.")
                return
        print("Livro não encontrado.")

    def devolver_livro(self, id_livro):
        for livro in self.livros:
            if livro.id == id_livro:
                if not livro.disponivel:
                    livro.disponivel = True
                    self.salvar_livros()
                    print(f"Livro '{livro.titulo}' devolvido!")
                else:
                    print("Este livro já está na biblioteca.")
                return
        print("Livro não encontrado.")
