catalogo = {}

emprestimoAtivo = {}

historico = []

def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com codigo{codigo} já existe!")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
    }

    print(f"Livro'{titulo}' adicionado com sucesso")
    return True 

#emprestar

def emprestarLivro(codigo, nome_aluno):

   if codigo not in catalogo:
       print(f"Erro: livro com código{codigo}não encontrado") 
       return False
   
   if catalogo[codigo]["quantidade"]<= 0:
       print(f"Erro: '{catalogo[codigo['titulo']]}'não está disponível")
       return False
   
   livroAluno = contarLivrosAlunos(nomeAluno)
   if livroAluno >= 2:
       print(f"Erro: Aluno já pegou a quantidade máxima")
       return False

