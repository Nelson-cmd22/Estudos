import tkinter as tk
from tkinter import messagebox, simpledialog
from biblioteca import biblioteca

class App:
    def __init__(self, root):
        self.biblioteca = biblioteca()
        self.root = root
        root.title("Sistema Biblioteca")
        root.geometry("800x500")
        root.resizable(False, False)

        tk.Button(root, text="Cadastrar Livro", width=20, command=self.cadastrar_livro).pack(pady=5)
        tk.Button(root, text="Cadastrar Usuário", width=20, command=self.cadastrar_usuario).pack(pady=5)
        tk.Button(root, text="Listar Livros", width=20, command=self.listar_livros).pack(pady=5)
        tk.Button(root, text="Emprestar Livro", width=20, command=self.emprestar_livro).pack(pady=5)
        tk.Button(root, text="Devolver Livro", width=20, command=self.devolver_livro).pack(pady=5)
        tk.Button(root, text="Sair", width=20, command=root.quit).pack(pady=10)

    def cadastrar_livro(self):
        def salvar():
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            if not titulo or not autor:
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return
            self.biblioteca.adicionar_livro(titulo, autor)
            messagebox.showinfo("Sucesso", f"Livro '{titulo}' adicionado!")
            janela.destroy()

        janela = tk.Toplevel(self.root)
        janela.title("Cadastrar Livro")

        tk.Label(janela, text="Título:").pack(pady=5)
        entry_titulo = tk.Entry(janela, width=30)
        entry_titulo.pack(pady=5)

        tk.Label(janela, text="Autor:").pack(pady=5)
        entry_autor = tk.Entry(janela, width=30)
        entry_autor.pack(pady=5)

        tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)

    def cadastrar_usuario(self):
        def salvar():
            nome = entry_nome.get()
            if not nome:
                messagebox.showerror("Erro", "Preencha o nome.")
                return
            self.biblioteca.adicionar_usuario(nome)
            messagebox.showinfo("Sucesso", f"Usuário '{nome}' cadastrado!")
            janela.destroy()

        janela = tk.Toplevel(self.root)
        janela.title("Cadastrar Usuário")

        tk.Label(janela, text="Nome:").pack(pady=5)
        entry_nome = tk.Entry(janela, width=30)
        entry_nome.pack(pady=5)

        tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)

    def listar_livros(self):
        janela = tk.Toplevel(self.root)
        janela.title("Lista de Livros")

        frame = tk.Frame(janela)
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=60, height=20)
        for livro in self.biblioteca.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            listbox.insert(tk.END, f"[{livro.id}] {livro.titulo} - {livro.autor} ({status})")
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)

    def emprestar_livro(self):
        def emprestar():
            try:
                id_livro = int(entry_id.get())
                self.biblioteca.emprestar_livro(id_livro)
                messagebox.showinfo("Sucesso", "Livro emprestado!")
                janela.destroy()
            except ValueError:
                messagebox.showerror("Erro", "ID inválido.")

        janela = tk.Toplevel(self.root)
        janela.title("Emprestar Livro")

        tk.Label(janela, text="ID do livro para emprestar:").pack(pady=5)
        entry_id = tk.Entry(janela, width=10)
        entry_id.pack(pady=5)

        tk.Button(janela, text="Emprestar", command=emprestar).pack(pady=10)

    def devolver_livro(self):
        def devolver():
            try:
                id_livro = int(entry_id.get())
                self.biblioteca.devolver_livro(id_livro)
                messagebox.showinfo("Sucesso", "Livro devolvido!")
                janela.destroy()
            except ValueError:
                messagebox.showerror("Erro", "ID inválido.")

        janela = tk.Toplevel(self.root)
        janela.title("Devolver Livro")

        tk.Label(janela, text="ID do livro para devolver:").pack(pady=5)
        entry_id = tk.Entry(janela, width=10)
        entry_id.pack(pady=5)

        tk.Button(janela, text="Devolver", command=devolver).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
