#Programador mirim - Vinícius da Silva Santana
# ========================================================================================== #

# =============================== # Funções reservadas # =================================== #
import os
def LPT():
    os.system("clear")  # Limpar Tela
    
def ExibirFilme(movies):      #Exibir filmes salvos
    print(f"{'Nome do Filme':^30} {'Gênero':^20}")
    for movie in movies:
        print(f"{movie['Nome']:^30} {movie['Gênero']:^20}")
        
def ExibirSerie(series):      #Exibir Séries salvas
    print(f"{'Nome da Série':^30} {'Episódio Atual':^15} {'Temporada Atual':^25} {'Quantidade de Temporadas disponíveis':^25}")
    for serie in series:
        print(f"{serie['Nome']:^30} {serie['Episódio Atual']:^15} {serie['Temporada Atual']:^25} {serie['Quantidade de Temporadas disponíveis']:^25}")

# ============================== # Função de Formatação # =================================== #
def negrito(text):
    return f"\033[1;37;1m{text}\033[0m"
    
def semibold(text):
    return f"\033[2;37;1m{text}\033[0m"
    
def italico(text):
    return f"\033[3;37;1m{text}\033[0m"
    
def sublinhado(text):
    return f"\033[4;97;101m{text}\033[0m"
# =================== # ===================== # ==================== # ====================== #

LFILMES = []  #Lista Filmes
LSERIES = []  #Lista Series

if os.path.exists("filmes.txt"):     #verificar se há filmes salvos
    with open("filmes.txt", "r") as arquivo_filmes:
        conteudo_filmes = arquivo_filmes.read().splitlines()[1:]
        for linha in conteudo_filmes:
            dados_filme = linha.split(", ")
            filme = {"Nome": dados_filme[0].split(": ")[1], "Gênero": dados_filme[1].split(": ")[1]}
            LFILMES.append(filme)

if os.path.exists("series.txt"):      #verificar se há séries salvas
    with open("series.txt", "r") as arquivo_series:
        conteudo_series = arquivo_series.read().splitlines()[1:]
        for linha in conteudo_series:
            dados_serie = linha.split(", ")
            serie = {"Nome": dados_serie[0].split(": ")[1], 
                     "Episódio Atual": dados_serie[1].split(": ")[1],
                     "Temporada Atual": dados_serie[2].split(": ")[1],
                     "Quantidade de Temporadas disponíveis": dados_serie[3].split(": ")[1]}

            LSERIES.append(serie)



while True:
    LPT()     #Limpar Tela
    print(sublinhado("Bem vindo ao gerenciador de séries e filmes".center(100)))
    print("""
    Escolha uma das opções abaixo:
    [1] para adicionar um filme.
    [2] para adicionar uma série.
    [3] para remover um filme ou série.
    [4] para atualizar o progresso de uma série/filme.
    [5] para verificar suas séries e filmes já adicionados
    [6] para SALVAR e SAIR do gerenciador.
    """)
    OPC = input(negrito("Digite a opção desejada: "))

    if OPC == "1":
        LPT()
        print(negrito("ADICIONAR FILME SELECIONADO".center(100)))
        Generos = ["Ação ou Aventura", "Comédia", "Drama", "Ficção Cientifica", "Romance", "Suspense ou Terror", "Outros"]
    
        print(semibold("OPÇÕES DE GÊNERO"))
        for i, GEN in enumerate(Generos):
            print(f"{i+1}. {GEN}")
    
        while True:
            try:
                genero_escolhido = int(input(italico("Escolha o número correspondente ao gênero do filme ou [0] para voltar ao menu: ")))
                if genero_escolhido == 0:
                    break
                elif genero_escolhido < 1 or genero_escolhido > len(Generos):
                    print("Opção inválida! Escolha um número correspondente ao gênero ou [0] para voltar ao menu.")
                else:
                    LPT()
                    GEN = Generos[genero_escolhido - 1]
                    print(negrito(f"Gênero selecionado: {GEN}"))
                    filme = {
                        "Nome": input("Nome do filme: "),
                        "Gênero": GEN
                    }
                    LFILMES.append(filme)
                    print(negrito("Filme adicionado com sucesso!"))
                    input("Pressione ENTER para voltar ao menu.")
                    break
            except ValueError:
                print("Opção inválida! Escolha um número correspondente ao gênero ou [0] para voltar ao menu.")

    
    elif OPC == "2":
        LPT()
        print(negrito("ADICIONAR SÉRIE SELECIONADO".center(100)))
        nome = input("Nome da Série: ")
        episodio_atual = input("Episódio Atual: ")

        while True:
            try:
                temporada_atual = int(input("Temporada Atual: "))
                break
            except ValueError:
                print(italico("Erro: Digite apenas números para a Temporada Atual."))
        
        while True:
            try:
                quantidade_temporadas = int(input("Quantidade de Temporadas disponiveis: "))
                break
            except ValueError:
                print(italico("Erro: Digite apenas números para a quantidade de temporadas disponíveis."))
        
        serie = {
            "Nome": nome,
            "Episódio Atual": episodio_atual,
            "Temporada Atual": temporada_atual,
            "Quantidade de Temporadas disponíveis": quantidade_temporadas
        }
        
        LSERIES.append(serie)
        print(negrito("Série adicionada com sucesso."))
        input("Pressione ENTER para voltar ao menu.")
    
    elif OPC == "3":
        LPT()
        print(negrito("REMOVER FILME OU SÉRIE SELECIONADO".center(100)))
        print(semibold("""Escolha o tipo de conteúdo a ser removido:
        \033[0m[1] Filme
        [2] Série"""))
        tipo = input(italico("Digite o número correspondente ao tipo de conteúdo ou [0] para voltar ao menu: "))
        
        if tipo == "1":
            while True:
                LPT()
                if len(LFILMES) == 0:
                    print(negrito("Não há filmes para remover."))
                    input("Pressione ENTER para voltar ao menu.")
                    break
                else:
                    print(sublinhado("FILMES DISPONÍVEIS".center(100)))
                    ExibirFilme(LFILMES)
                    nome_filme = input(italico("Digite o nome do filme que deseja remover ou [0] para voltar ao menu: "))
    
                    if nome_filme == "0":
                        break
    
                    for filme in LFILMES:
                        if filme['Nome'] == nome_filme:
                            LFILMES.remove(filme)
                            print(negrito("Filme removido com sucesso."))
                            input("Pressione ENTER para voltar ao menu.")
                            break
                    else:
                        print(negrito("Filme não encontrado."))
                        input("Pressione ENTER para continuar.")
        
        elif tipo == "2":
            while True:
                LPT()
                if len(LSERIES) == 0:
                    print(negrito("Não há séries para remover!!"))
                    input("Pressione ENTER para voltar ao menu.")
                    break
                else:
                    print(sublinhado("SÉRIES DISPONÍVEIS".center(100)))
                    ExibirSerie(LSERIES)
                    nome_serie = input(italico("Digite o nome da série que deseja remover ou [0] para voltar ao menu: "))
    
                    if nome_serie == "0":
                        break
    
                    for serie in LSERIES:
                        if serie['Nome'] == nome_serie:
                            LSERIES.remove(serie)
                            print(negrito("Série removida com sucesso."))
                            input("Pressione ENTER para voltar ao menu.")
                            break
                    else:
                        print(negrito("Série não encontrada."))
                        input("Pressione ENTER e digite novamente.")
        
        else:
            print("Opção inválida!")
            input("Pressione ENTER para voltar ao menu.")
    
    elif OPC == "4":
        LPT()
        print(negrito("ATUALIZAR PROGRESSO DE SÉRIE/FILME SELECIONADO".center(100)))
        print(semibold("""Escolha o tipo de conteúdo a ser atualizado:
        \033[0m[1] Filme
        [2] Série"""))
        tipo = input(italico("Digite o tipo de conteúdo a ser atualizado: "))
    
        if tipo == "1":
            if len(LFILMES) == 0:
                print("Não há filmes disponíveis para atualizar.")
                input("Pressione ENTER para voltar ao menu.")
            else:
                print(sublinhado("FILMES DISPONÍVEIS".center(100)))
                ExibirFilme(LFILMES)
                nome_filme = input("Digite o nome do filme que deseja atualizar: ")
                for filme in LFILMES:
                    if filme['Nome'] == nome_filme:
                        novo_nome = input("Digite o novo nome do filme (deixe em branco para manter o mesmo): ")
                        novo_genero = input("Digite o novo gênero do filme (deixe em branco para manter o mesmo): ")
                        if novo_nome:
                            filme['Nome'] = novo_nome
                        if novo_genero:
                            filme['Gênero'] = novo_genero
                        print(italico("Filme atualizado com sucesso."))
                        break
                else:
                    print("Filme não encontrado.")
                    
        elif tipo == "2":
            while True:
                if len(LSERIES) == 0:
                    print("Não há séries disponíveis para atualizar.")
                    input("Pressione ENTER para voltar ao menu.")
                    break
                else:
                    print(sublinhado("SÉRIES DISPONÍVEIS".center(100)))
                    ExibirSerie(LSERIES)
                    nome_serie = input("Digite o nome da série que deseja atualizar ou [0] para voltar ao menu: ")
                    if nome_serie == "0":
                        break
    
                    for serie in LSERIES:
                        if serie['Nome'] == nome_serie:
                            novo_nome = input("Digite o novo nome da série (deixe em branco para manter o mesmo): ")
                            while True:
                                try:
                                    novo_episodio = input("Digite o novo número do episódio atual (deixe em branco para manter o mesmo): ")
                                    if novo_episodio == "":
                                        break
                                    else:
                                        novo_episodio = int(novo_episodio)
                                        break
                                except ValueError:
                                    print(italico("Erro: Digite apenas números para o número do episódio atual."))
    
                            while True:
                                try:
                                    nova_temporada = input("Digite a nova temporada atual (deixe em branco para manter a mesma): ")
                                    if nova_temporada == "":
                                        break
                                    else:
                                        nova_temporada = int(nova_temporada)
                                        break
                                except ValueError:
                                    print(italico("Erro: Digite apenas números para a nova temporada atual."))
    
                            while True:
                                try:
                                    nova_quantidade = input("Digite a nova quantidade de temporadas disponíveis (deixe em branco para manter a mesma): ")
                                    if nova_quantidade == "":
                                        break
                                    else:
                                        nova_quantidade = int(nova_quantidade)
                                        break
                                except ValueError:
                                    print(italico("Erro: Digite apenas números para a nova quantidade de temporadas disponíveis."))
    
                            if novo_nome:
                                serie['Nome'] = novo_nome
                            if novo_episodio is not None:
                                serie['Episódio Atual'] = novo_episodio
                            if nova_temporada is not None:
                                serie['Temporada Atual'] = nova_temporada
                            if nova_quantidade is not None:
                                serie['Quantidade de Temporadas disponíveis'] = nova_quantidade
                            print("Série atualizada com sucesso.")
                            break
                    else:
                        print("Série não encontrada.")
                        continue
                break
    
        else:
            print("Opção inválida!")
            input("Pressione ENTER para voltar ao menu.")
            
    elif OPC == "5":
        LPT()
        print(negrito("LISTA DE SÉRIE/FILME SELECIONADO".center(100)))
        tipo = input("""Digite a opção para verificar a lista disponivel
        [1] FILMES
        [2] SERIES
        [3] AMBOS""")
        
        if tipo == "1":
            print("LISTAGEM DE FILMES")
            ExibirFilme(LFILMES)
        
        elif tipo == "2":
            print("LISTAGEM DE SÉRIES")
            ExibirSerie(LSERIES)
        
        else:
            ExibirFilme(LFILMES)
            ExibirSerie(LSERIES)
        input("Pressione ENTER para voltar ao menu.")
    
    elif OPC == "6":
        LPT()
        print(negrito("Salvando dados e saindo do gerenciador...".center(100)))
        
        # Salvar filmes em um arquivo separado
        with open("filmes.txt", "w") as arquivo_filmes:
            arquivo_filmes.write("=== FILMES ===\n")
            for filme in LFILMES:
                arquivo_filmes.write(f"Nome: {filme['Nome']}, Gênero: {filme['Gênero']}\n")
        
        # Salvar séries em um arquivo separado
        with open("series.txt", "w") as arquivo_series:
            arquivo_series.write("=== SÉRIES ===\n")
            for serie in LSERIES:
                arquivo_series.write(f"Nome: {serie['Nome']}, Episódio Atual: {serie['Episódio Atual']}, "
                                     f"Temporada Atual: {serie['Temporada Atual']}, "
                                     f"Quantidade de Temporadas disponíveis: {serie['Quantidade de Temporadas disponíveis']}\n")
        
        print(negrito("Dados salvos com sucesso!"))
        input("Pressione ENTER para sair do gerenciador.")
        break

        
    

