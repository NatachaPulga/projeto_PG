def main():
    # Funcionalidades relativas a um utilizador
    class Utilizador:
            #Construtor
            def __init__(self, nome, interesses, artigos_disponiveis):
                self.nome = nome
                self.interesses = interesses
                self.artigos_disponiveis = artigos_disponiveis
                # Lista para armazenar as avaliações.
                self.avaliacoes = []
                # Armazena pycoins
                self.pycoins = 50


            #Altera os interesses e/ou os artigos de um utilizador
            def editar_conta(self, novos_interesses, novos_artigos):
                self.interesses = novos_interesses
                self.artigos_disponiveis = novos_artigos
                print(f"A conta do usuário {self.nome} atualizada com sucesso!")


            #Adiciona uma nova avaliação, podendo incluir um comentário
            def deixar_avaliacao(self, estrelas, comentario):
                # O '\n' é para fazer uma quebra de linha.
                self.avaliacoes.append({"estrelas": estrelas, "comentario": comentario})
                print(f"Avaliação do usuário {self.nome}, foi registrada com sucesso!")


            #Apresenta todas as avaliações e comentários
            def listar_avaliacoes(self):
                # Para verificar se a lista 'self.avaliacoes' está vazia.
                if not self.avaliacoes:
                    print(f"Ainda não há avaliações para {self.nome}.")
                else:
                    # Loop que percorre cada item da lista 'self.avaliacoes' e atribui temporariamente a cada um dos itens à variável 'avaliacao'.
                    # A 'avaliacao' representa um dicionário que contém informações sobre uma avaliação específica, como estrelas e comentários associados a essa avaliação.
                    for avaliacao in self.avaliacoes:
                        print(f"Usuário: {self.nome}.")
                        # O '\n' é para fazer uma quebra de linha.
                        # Em '{avaliacao['estrelas']}' e '{avaliacao['comentário']}' estamos extrair e exibir o número de estrelas da avaliação e o comentário, armazenada no dicionário 'avaliacao'.
                        print(f"Avaliação: {avaliacao['estrelas']} estrelas. \n Comentário: {avaliacao['comentário']}.")


            #Apresenta todos os interesses.
            def mostrar_interesses(self):  
                print(f"Interesses de {self.nome}:")
                if not self.interesses:
                    print("O utilizador não tem interesses registados.")
                else:
                    print(self.interesses)
            

            #Apresenta todos os artigos.
            def mostrar_artigos(self):
                print(f"Artigos disponíveis de {self.nome}:")
                if not self.artigos_disponiveis:
                    print("O utilizador não tem artigos disponíveis.")
                else:
                    for artigo in self.artigos_disponiveis:
                        print(f"Nome: {artigo.nome}, Preço: {artigo.preco}, Tipologia: {artigo.tipologia}, Quantidade: {artigo.quantidade}")


            #Altera o número de pycoins.
            def alterar_pycoins(self, numero_pycoins):
                self.pycoins = numero_pycoins
                print(f"O Número de pycoins de {self.nome} foi atualizado para {numero_pycoins}.")


            #Apresenta o número de pycoins.
            def mostrar_pycoins(self):
                if not self.pycoins:
                    print("O utilizador não tem pycoins disponíveis.")
                else:
                    print(f"O número de pycoins de {self.nome}: {self.pycoins}")

            #Remover o artigo da lista de artigos do utilizador
            def remover_artigo(self,artigo):
                self.artigos_disponiveis.remove(artigo)
                print(f"O artigo {artigo.nome} foi eliminado da Feira Virtual.")






    #Funcionalidades relativas a um artigo
    class Artigo:
        #Construtor
            def __init__(self, nome, preco, tipologia, quantidade):
                self.nome = nome
                self.preco = preco
                self.tipologia = tipologia
                self.quantidade = quantidade
                # Percentagem fixa da subida ou descido do preço dos artigos.
                self.percentagem_alteracao = 0.25


            #Altera o nome de um artigo para o novo nome recebido
            def editar_nome(self, nome):
                self.nome = nome
                print(f"Nome do artigo foi alterado para: {nome}")
            

            #Altera o preço de um artigo de acordo com a percentagem dada
            def ajustar_preco(self, percentagem_alteracao):
                # Preço aumenta 25%, se a quantidade do artigo for menor ou igual a 3.
                if self.quantidade <= 3:
                    self.preco = self.preco + (self.preco * percentagem_alteracao)
                # Preço diminui 25%, se a quantidade do artigo for maior que 10.
                elif self.quantidade > 10:
                    self.preco = self.preco - (self.preco * percentagem_alteracao)
            

            #Altera o preço para o novo preço recebido
            def editar_preco(self, preco):
                self.preco = preco
                print(f"Preço do artigo foi alterado para: {preco}")
            

            #Apresenta o preço do artigo
            def mostrar_preco(self):
                print(f"Preço do artigo: {self.preco}")
            

            #Altera a quantidade
            def editar_quantidade(self, nova_quantidade):   
                self.quantidade = nova_quantidade
                print(f"A quantidade do artigo {self.nome} foi atualizada para {nova_quantidade}.")


            #Apresenta a quantidade do artigo
            def mostrar_quantidade(self):
                if not self.quantidade:
                    print(f"Não existem unidades disponíveis para o artigo {self.nome}.")
                else:
                    print(f"O artigo {self.nome} tem {self.quantidade} unidades disponiveis.")
            

            #Altera a tipologia
            def editar_tipo (self, novo_tipo):
                self.tipologia = novo_tipo
                print(f"A tipologia do artigo {self.nome} foi atualizada para {novo_tipo}.")
            

            #Apresenta a tipologia do artigo
            def mostrar_tipo (self):    
                if not self.tipologia:
                    print(f"A tipologia do artigo {self.nome} não se encontra definida.")
                else:
                    print(f"A tipologia do artigo {self.nome} é {self.tipologia}")





    #Gestão da feira, avaliações e negociação automática
    class FeiraVirtual:
            #Construtor
            def __init__(self):
                # Iniciar listas vazias.
                self.utilizadores = []
                self.artigos = []
                self.avaliacoes = []
        
        
            #!!!! A FAZER: Requisito nome de utilizador único -> verifica se o nome já existe. se existir, concatena "_1" e verifica novamente se existe
            #!!!! A VALIDAR: Quando é que se ajusta preço de um artigo? quando é criado o utilizador?

            #Adiciona um novo utilizador recebendo o nome, interesses e artigos
            def registar_utilizador (self, nome, interesses, artigos_disponiveis):
                
                #Exemplo Input artigos_disponiveis: Jogo, 10, Tecnologia, 5
                #Exemplo Input artigos_disponiveis: Jogo, 10, Tecnologia, 5 & Livro HP, 12, Livro, 2
                artigos_manuais = artigos_disponiveis.split("&") # Artigos separados pelo caracter "&" em vários artigos
                tem_artigo = len(artigos_disponiveis)

                # Transforma cada artigo em lista (split campos pela virgula para termos uma posição por cada caracteristica do artigo). Remove os caracteres "[" e "]" caso existam
                artigos = []

                if tem_artigo > 0: #Só avança se existirem artigos a importar
                    for artigo in artigos_manuais:
                        artigos.append(artigo.replace("[", "").replace("]", "").split(","))

                # Criação da lista de artigos do utilizador. Caso não existem artigos, é criado um utilizador com lista de artigos vazia
                artigos_utilizador = []
                for artigo in artigos:
                    novo_artigo = Artigo(artigo[0], int(artigo[1]), artigo[2], int(artigo[3])) #artigo[0] corresponde ao nome, artigo[1] é o preço, artigo[2] é a tipologia e artigo[3] a quantidade
                    artigos_utilizador.append(novo_artigo)

                novo_utilizador = Utilizador(nome, interesses, artigos_utilizador)
                self.utilizadores.append(novo_utilizador)

                print(f"O utilizador {nome} foi registado na Feira Virtual.")



            # NOVO!!!!!!!!!!
            # NOVO!!!!!!!!!! ----> ValueError: could not convert string to float: 'preço'
            # NOVO!!!!!!!!!!
            def registar_utilizador_ficheiro(self, nome_ficheiro):
               with open(nome_ficheiro, "r", encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()

                    for linha in linhas:
                        campos = linha.strip().split(';')
                        if len(campos) == 3:
                            nome = campos[0]
                            interesses = campos[1][1:-1].split(',')
                            artigos_info = campos[2][1:-1].split('&')

                            artigos_disponiveis = []
                            for artigo in artigos_info:
                                info_artigo = artigo.split(',')
                                if len(info_artigo) == 4:
                                    nome_artigo = info_artigo[0]
                                    preco = float(info_artigo[1])
                                    tipologia = info_artigo[2]
                                    quantidade = int(info_artigo[3])
                                    novo_artigo = Artigo(nome_artigo, preco, tipologia, quantidade)
                                    artigos_disponiveis.append(novo_artigo)

                            novo_utilizador = Utilizador(nome, interesses, artigos_disponiveis)
                            self.utilizadores.append(novo_utilizador)




            #Importa uma lista de utilizadores a partir de um ficheiro
            def importar_utilizadores(self, nome_ficheiro):

                #Abre o ficheiro em modo leitura e encoding utf-8 para a acentuação aparecer ok
                with open(nome_ficheiro, "r", encoding='utf-8') as ficheiro: 
                    registos = ficheiro.readlines()

                    #Avança para processar apenas a partir da linha seguinte ao header 
                    for registo in registos[1:]: #O 0 corresponde ao header
                        #Remove caracter /n (usando o strip). Separa pelo caracter ";" e cria a lista valores_a_inserir com os campos separados
                        valores_a_inserir = registo.strip().split(";")

                        nome_utilizador = valores_a_inserir[0]
                        interesses_utilizador = valores_a_inserir[1] # Lista de interesses
                        artigos_ficheiro = valores_a_inserir[2].split("&") # Artigos separados pelo caracter "&" em vários artigos
                        tem_artigo = len(valores_a_inserir[2])

                        # Transforma cada artigo em lista (split campos pela virgula). Remove os caracteres "[" e "]"
                        #Exemplo: [['telemóvel', '5', 'tecnologia', '1'], ['raquete de ténis', '10', 'desporto', '2']]
                        artigos = []

                        if tem_artigo > 0: #Só avança se existirem artigos a importar
                            for artigo in artigos_ficheiro:
                                artigos.append(artigo.replace("[", "").replace("]", "").split(","))

                        # Criação da lista de artigos do utilizador
                        artigos_utilizador = []
                        for artigo in artigos:
                            novo_artigo = Artigo(artigo[0], int(artigo[1]), artigo[2], int(artigo[3])) #artigo[0] corresponde ao nome, artigo[1] é o preço, artigo[2] é a tipologia e artigo[3] a quantidade
                            artigos_utilizador.append(novo_artigo)

                        #Cria o novo utilizador e adiciona à lista
                        novo_utilizador = Utilizador(nome_utilizador, interesses_utilizador, artigos_utilizador)
                        self.utilizadores.append(novo_utilizador)
                            
                    print(f"O ficheiro {nome_ficheiro} foi importado com sucesso.")
                        
                        
            #Elimina um utilizador
            def eliminar_conta(self, nome_utilizador):
                for utilizador in self.utilizadores:
                    if utilizador.nome == nome_utilizador:
                        self.utilizadores.remove(utilizador)
                        print(f"O utilizador {nome_utilizador} foi eliminado da Feira Virtual.")


            #Apresenta todos os utilizadores inseridos
            def listar_utilizadores(self): 
                if not self.utilizadores:
                    print("Não existem utilizadores registados.")
                else:
                    for utilizador in self.utilizadores:
                        print(f"{utilizador.nome}")


            #Apresenta a quantidade de utilizadores na feira (função útil para testes)
            def listar_qtd_utilizadores(self): 
                quantidade_utilizadores = len(self.utilizadores)
                print(f"{quantidade_utilizadores} utilizador/es registado/s na Feira Virtual.")


            #Apresenta os interesses para um dado utilizador
            def mostrar_interesses_utilizador(self, nome):
                for utilizador in self.utilizadores:
                    if nome == utilizador.nome:
                        utilizador.mostrar_interesses()


            #Apresenta os artigos para um dado utilizador
            def mostrar_artigos_utilizador(self, nome):
                for utilizador in self.utilizadores:
                    if nome == utilizador.nome:
                        utilizador.mostrar_artigos()


            #Apresenta os pycoins para um dado utilizador
            def mostrar_pycoins_utilizador(self, nome):
                for utilizador in self.utilizadores:
                    if nome == utilizador.nome:
                        utilizador.mostrar_pycoins()


            #Função auxiliar para agregar todos os artigos numa única lista
            def devolve_lista_completa_artigos(self):
                lista_completa_artigos = []
                for utilizador in self.utilizadores:
                    for artigo in utilizador.artigos_disponiveis:
                        lista_completa_artigos.append(artigo)
                return lista_completa_artigos
            

            #Apresenta todos os artigos disponíveis ordenados por preço
            def listar_artigos(self):

                #Devolve a lista de artigos de todos os utilizadores
                lista_completa_artigos = self.devolve_lista_completa_artigos()

                if not lista_completa_artigos:
                    print("Não existem artigos disponíveis.")
                else:
                    print("Artigos disponíveis ordenados por preço:")

                    #Apresenta os artigos, por ordem crescente, de acordo com o preço
                    artigos_ordem = sorted(lista_completa_artigos, key=lambda x: x.preco)
                    
                    for artigo in artigos_ordem:
                        print(f"{artigo.nome}, Preço: {artigo.preco}")
                        
                

            #Efetua uma compra de um artigo. O comprador e o vendedor são os nomes de dois utilizadores registados
            def comprar_artigo(self, comprador, vendedor, artigo):

                #Devolve a lista de artigos de todos os utilizadores
                lista_completa_artigos = self.devolve_lista_completa_artigos()

                #Variaveis para guardar objetos Utilizador e Artigo
                artigo_a_vender = None
                utilizador_comprador = None
                utilizador_vendedor = None

                #Guarda o objeto Artigo para depois aceder à quantidade e preço
                for artigo_aux in lista_completa_artigos:
                    if artigo_aux.nome == artigo:
                        artigo_a_vender = artigo_aux

                #Valida a disponibilidade do artigo
                if artigo_a_vender is None or artigo_a_vender.quantidade < 1: #Caso não encontre o artigo na lista ou a quantidade não seja positiva
                    print(f"O artigo {artigo} não se encontra disponível para venda.")
                else:
                    #Guarda os objetos Utilizador do comprador e vendedor
                    for utilizador in self.utilizadores:
                        if comprador == utilizador.nome:
                            utilizador_comprador = utilizador
                        if vendedor == utilizador.nome:
                            utilizador_vendedor = utilizador   
                    
                    if utilizador_comprador.pycoins >= artigo_a_vender.preco:
                        #Processamento comprador
                        pycoins_atualizar = utilizador_comprador.pycoins - artigo_a_vender.preco
                        utilizador_comprador.alterar_pycoins(pycoins_atualizar)
                        #Processamento vendedor
                        pycoins_atualizar = utilizador_vendedor.pycoins + artigo_a_vender.preco
                        utilizador_vendedor.alterar_pycoins(pycoins_atualizar)
                        #Finalização compra
                        print(f"{comprador} comprou {artigo} de {vendedor} com sucesso!")
                        if artigo_a_vender.quantidade == 1:
                            utilizador_vendedor.remover_artigo(artigo_a_vender) #Remove o artigo porque apenas tinha 1 unidade
                        else:
                            artigo_a_vender.editar_quantidade(artigo_a_vender.quantidade-1) #Diminui a quantidade em 1
                    else:
                        print(f"{comprador} não tem pycoins suficientes.")
            


            #Calcula a reputação de um utilizador com base nas suas avaliações
            def calcular_reputacao(self, utilizador):
                # Para sabermos o total de avaliações.
                total_avaliacoes = len(utilizador.avaliacoes)
                # Se não houver avaliações.
                if total_avaliacoes == 0:
                    print(f"O utilizador {utilizador.nome} ainda não recebeu nenhuma avaliação.")
                    # Devolve 0, pois não existem avaliações.
                    return 0
                else:
                    # Número inicial do contador de estrelas (avaliações).
                    soma_estrelas = 0
                    # Loop para somar as estrelas (avaliações).
                    for avaliacao in utilizador.avaliacoes:
                        soma_estrelas = soma_estrelas + avaliacao["estrelas"]

                    # Váriavel que tem a média de estrelas (avaliações) de um utilizador.
                    reputacao_media = soma_estrelas / total_avaliacoes
                    # Em '{reputacao_media:.2f}': o 'f', significa que o número será formatado como um float (número decimal); e o '.2', especifica que queremos exibir apenas duas casas decimais, após o ponto decimal.
                    print(f"A reputação média de {utilizador.nome} é {reputacao_media:.2f} estrelas.")
                    # Devolve reputação média de um utilizador, de acordo com as avaliações existentes.
                    return reputacao_media


            #Coloca um artigo à venda. O vendedor é o nome de um utilizador
            def colocar_artigo_para_venda(self, vendedor, artigo, preco):
                # Verifica se o vendedor existe na feira virtual.
                if vendedor in self.utilizadores:
                    # Verifica se o artigo pertence ao vendedor.
                    if artigo in vendedor.artigos_disponiveis:
                        # Define o preço do artigo e o coloca à venda.
                        artigo.editar_preco(preco)
                        print(f"O artigo '{artigo.nome}' foi colocado à venda por {preco} pycoins.")

                     # Se não se verificar que o artigo pertence ao vendedor.
                    else:
                        print(f"O utilizador {vendedor.nome} não possui o artigo '{artigo.nome}' para venda.")

                # Se não se verificar que o vendedor existe na feira virtual.
                else:
                    print(f"O vendedor '{vendedor}' não está registrado na feira virtual.")


            #Encontra os nomes de utilizadores interessados no artigo recebido
            def encontrar_compradores_interessados(self, artigo):
                # Iniciar a lista de interesses dos utilizadores vazia.
                compradores_interessados = []

                # Loop que percorre cada usuário na lista de utilizadores.
                for usuario in self.utilizadores:
                    # Verifica se o artigo está na lista de interesses do usuário.
                    if artigo.nome in usuario.interesses:
                        compradores_interessados.append(usuario.nome)

                # Uma lista com elementos será avaliada como True, e uma lista vazia será avaliada como False.
                # Caso a lista com elementos seja avaliada.
                if compradores_interessados:
                    # O 'join()' é utilizado para juntar (ou concatenar) elementos. Ou seja, em {', '.join(compradores_interessados)} acontce uma uniam dos elementos da lista 'compradores_interessados' em uma única string, separando cada elemento da lista por ', '.
                    print(f"Compradores interessados no artigo '{artigo.nome}' são: {', '.join(compradores_interessados)}")
                
                # Caso a lista com elementos não seja avaliada.
                else:
                    print(f"Nenhum comprador está interessado no artigo '{artigo.nome}'.")

                # Devolve os compradores interessados num artigo.
                return compradores_interessados


            #Exporta a lista de artigos para um ficheiro ordenados por quantidade
            def exportar_artigos_preco(self, nome_ficheiro):
                # Uma lista com elementos será avaliada como True, e uma lista vazia será avaliada como False.
                # Verifica se existem artigos na feira virtual.
                if not self.utilizadores:
                    print("Não há artigos para exportar.")
                    return

                # Ordena os artigos por quantidade.
                # Em '.sort(key=lambda x: x.quantidade)', nesta caso específico, o 'key=lambda x: x.quantidade' dentro do método 'sort()', esta a usar uma função 'lambda' para extrair o atributo 'quantidade' de cada elemento da lista antes de ordená-los. Isso significa que estamos a ordenar os elementos com base nos valores do atributo 'quantidade'.
                self.utilizadores.sort(key=lambda x: x.quantidade)

                # Abre o arquivo para escrita.
                with open(nome_ficheiro, 'w') as arquivo:
                    # Escreve o cabeçalho ou informações iniciais, se necessário.
                    # O '\n' é para fazer uma quebra de linha.
                    arquivo.write("Lista de Artigos Ordenados por Quantidade:\n")

                    # Itera sobre os artigos ordenados por quantidade
                    for artigo in self.utilizadores:
                        # Escreve as informações do artigo no arquivo.
                        arquivo.write(f"Nome: {artigo.nome}, Quantidade: {artigo.quantidade}, Preço: {artigo.preco}\n")

                print(f"Lista de artigos ordenada por quantidade exportada para '{nome_ficheiro}' com sucesso.")


            #Exporta a lista de utilizadores para um ficheiro ordenados por reputação
            def exportar_utilizadores(self):
                # Nome do arquivo predefinido.
                nome_ficheiro = "utilizadores_ordenados.txt"

                # Uma lista com elementos será avaliada como True, e uma lista vazia será avaliada como False.
                # Verifica se existem utilizadores na feira virtual.
                if not self.utilizadores:
                    print("Não há utilizadores para exportar.")
                    return

                # Ordena a lista de utilizadores por reputação, utilizando a função 'calcular_reputacao'.
                # Em '.sort(key=self.calcular_reputacao, reverse=True)', o 'sort()' organiza os elementos de uma lista, ele recebe um argumento 'key', que é uma função para ser chamada em cada elemento da lista, e 'reverse', que determina se a ordem de classificação deve ser reversa ou não.
                # Ou seja: Ordena a lista de utilizadores ('utilizadores') com base na reputação de cada utilizador ('calcular_reputacao').
                self.utilizadores.sort(key=self.calcular_reputacao, reverse=True)

                # Abre o arquivo para escrita.
                with open(nome_ficheiro, 'w') as arquivo:
                    # Escreve o cabeçalho ou informações iniciais, se necessário.
                    # O '\n' é para fazer uma quebra de linha.
                    arquivo.write("Lista de Utilizadores Ordenados por Reputação:\n")

                    # Itera sobre os utilizadores ordenados por reputação
                    for utilizador in self.utilizadores:
                        # Escreve as informações do utilizador no arquivo.
                        # Em '{self.calcular_reputacao(utilizador):.2f}': o 'f', significa que o número será formatado como um float (número decimal); e o '.2', especifica que queremos exibir apenas duas casas decimais, após o ponto decimal. O '\n' é para fazer uma quebra de linha.
                        arquivo.write(f"Nome: {utilizador.nome}, Reputação: {self.calcular_reputacao(utilizador):.2f} estrelas \n")

                print(f"Lista de utilizadores ordenada por reputação exportada para '{nome_ficheiro}' com sucesso.")



            #Início da feira. O grupo deve apresentar testes do projeto nesta função
            def main():
                pass





    # Gestão da lista de artigos disponíveis na feira
    class Mercado:
            #Construtor
            def __init__(self):
                # Inicia a lista de artigos vazia.
                self.artigos = []

            #Adiciona um novo artigo
            def adicionar_artigo(self, artigo):
                self.artigos.append(artigo)

            #Elimina um artigo
            def remover_artigo(self, artigo):
                if artigo in self.artigos:
                    self.artigos.remove(artigo)

            #Mostra o nome, preço e quantidade do artigo recebido
            def mostrar_artigo(self, artigo):
                # Percorre cada item na lista de artigos.
                for artigo in self.artigos:
                    # Verifica se o nome do artigo, coincide com o nome do artigo recebido como parâmetro.
                    if artigo.nome == artigo:
                        # Exibe o nome, preço e quantidade do artigo.
                        print(f"Artigo: {artigo.nome}")
                        print(f"Preço: {artigo.preco}")
                        print(f"Quantidade: {artigo.quantidade}")
                        # Para encerra a função após encontrar o artigo correspondente.
                        return

                # Exibe mensagem se o artigo não for encontrado na lista.
                print("Artigo não encontrado.")




    









    # Iniciar programa.
    def main():
        # Para a class 'FeiraVirtual' funcionar.
        feira = FeiraVirtual() 

        print("Bem-vindo/a à Feira Virtual. Pretende aceder a:")
        print("1 - Utilizadores")
        print("2 - Artigos")
        print("3 - Mercado")

        escolha = input(" ")

        # Para garantir uma das escolhas pretendidas.
        while escolha not in ["1", "2", "3"]:
            print("Escolha entre:")
            print("1 - Utilizadores")
            print("2 - Artigos")
            print("3 - Mercado")

            escolha = input(" ")

        
        # Se o utilizador escolher '1 - Utilizadores'.
        if escolha == "1":
            # Tem de estar dentro do loop para se conseguir voltar a atrás.
            while True:
                print("Pretende aceder a:")
                print("1 - Registo de utilizadores")
                print("2 - Alteração de um utilizador")
                print("3 - Eliminação de conta de um utilizador")
                print("4 - Lista de utilizadores")
                print("5 - Mostrar artigos de um utilizador")
                print("6 - Mostrar interesses de um utilizador")
                print("7 - Mostrar Pycoins de um utilizador")
                print("V - Voltar atrás")
                print("S - Sair")

                escolha_utilizadores = input(" ")

                # Para garantir uma das escolhas pretendidas.
                while escolha_utilizadores not in ["1", "2", "3", "4", "5", "6", "7", "V", "S"]:
                    print("Escolha entre:")
                    print("1 - Registo de utilizadores")
                    print("2 - Alteração de um utilizador")
                    print("3 - Eliminação de conta de um utilizador")
                    print("4 - Lista de utilizadores")
                    print("5 - Mostrar artigos de um utilizador")
                    print("6 - Mostrar interesses de um utilizador")
                    print("7 - Mostrar Pycoins de um utilizador")
                    print("V - Voltar atrás")
                    print("S - Sair")

                    escolha_utilizadores = input(" ")

                # Se o utilizador escolher '1 - Registo de utilizadores'.
                if escolha_utilizadores == "1":
                    # Tem de estar dentro do loop para se conseguir voltar a atrás.
                    while True:
                        print("Pretende aceder a:")
                        print("1 - Registo manual")
                        print("2 - Registo por ficheiro")
                        print("V - Voltar atrás")

                        escolha_registo = input(" ")

                        # Para garantir uma das escolhas pretendidas.
                        while escolha_registo not in ["1", "2", "V"]:
                            print("Escolha entre:")
                            print("1 - Registo manual")
                            print("2 - Registo por ficheiro")
                            print("V - Voltar atrás")

                            escolha_registo = input(" ")

                        #  Se o utilizador escolher '1 - Registo manual'.
                        if escolha_registo == "1":
                            nome_utilizador = input("Digite o nome do utilizador: ")
                            interesses_utilizador = input("Digite os interesses do utilizador (separados por vírgula): ")
                            print("Os artigos disponíveis devem de ser escritos no formato seguinte: 'Nome, Preço, Tipologia, Quantidade', se quizer adicionar outro artigo deve de separa-lo com '&')")
                            artigos_utilizador = input("Digite os artigos disponíveis (no formato 'Nome, Preço, Tipologia, Quantidade & Nome, Preço, Tipologia, Quantidade', separados por '&'): ")

                            # Chama o método registar_utilizador com as informações fornecidas pelo usuário.
                            feira.registar_utilizador(nome_utilizador, interesses_utilizador, artigos_utilizador)

    
                            print("Registo manual criado com sucesso!")
                            break # Para voltar ao menu.


                         #  Se o utilizador escolher '2 - Registo por ficheiro'.
                        elif escolha_registo == "2":
                            # Tem de estar dentro do loop para se conseguir voltar a atrás.
                            while True:
                                nome_ficheiro = input("Insira o nome do ficheiro de utilizadores para importar: ")

                                # Verifica se o nome do arquivo inserido termina com '.txt'.
                                # 'endswith()' é um método usado para verificar se uma string termina com um sufixo específico, '(".txt")'. Ele retorna True se a string terminar com o sufixo especificado e False caso contrário.
                                if nome_ficheiro.endswith(".txt"):
                                    # Importa os utilizadores a partir do ficheiro especificado.
                                    
                                    feira.registar_utilizador_ficheiro(nome_ficheiro)
                                    print("Registo por ficheiro criado com sucesso!")
                                    break  # Para voltar ao menu.
                                else:
                                    print("Por favor, insira um nome de arquivo válido com a extensão '.txt'.")


                         #  Se o utilizador escolher 'V - Voltar atrás'.
                        elif escolha_registo.upper() == "V":
                            break  # Para voltar ao menu.
          



                 # Se o utilizador escolher '2 - Alteração de um utilizador'.
                elif escolha_utilizadores == "2":
                    # Tem de estar dentro do loop para se conseguir voltar a atrás.
                    while True:
                        nome_utilizador = input("Insira o nome do utilizador: ")

                        if nome_utilizador not in feira.utilizadores:
                            print("Nome do utilizador inválido.")
                            break
                         #
                        elif nome_utilizador in feira.utilizadores:
                            print("Pretende aceder a:")
                            print("1 - Editar interesses")
                            print("2 - Editar artigos")
                            print("V - Voltar atrás")

                            escolha_edicao = input("Escolha uma opção: ")

                            # Para garantir uma das escolhas pretendidas.
                            while escolha_edicao not in ["1", "2", "V"]:
                                print("Escolha entre:")
                                print("1 - Editar interesses")
                                print("2 - Editar artigos")
                                print("V - Voltar atrás")

                                escolha_edicao = input("Escolha uma opção: ")


                            if escolha_edicao == "1":
                                # Editar interesses do utilizador
                                novos_interesses = input("Insira os novos interesses (separados por vírgula): ")
                                nome_utilizador.editar_conta(novos_interesses.split(','))
                                break
                             #
                            elif escolha_edicao == "2":
                                print("Aqui estão seus artigos:")
                                feira.mostrar_artigos_utilizador(nome_utilizador)

                                nome_artigo = input("Insira o nome do artigo que deseja editar: ")

                                if nome_artigo not in feira.mostrar_artigos_utilizador(nome_utilizador):
                                    print("Artigo inválido.")
                                    break
                                 #
                                elif nome_artigo in feira.mostrar_artigos_utilizador(nome_utilizador):
                                    novo_nome = input("Novo nome do artigo: ")
                                    novo_preco = int(input("Novo preço: "))
                                    nova_tipologia = input("Nova tipologia: ")
                                    nova_quantidade = int(input("Nova quantidade: "))
                                    # Alterar.
                                    nome_artigo.editar_nome(novo_nome)
                                    nome_artigo.editar_preco(novo_preco)
                                    nome_artigo.editar_tipo(nova_tipologia)
                                    nome_artigo.editar_quantidade(nova_quantidade)
                                    # Confirmação de alteração
                                    print(f"Detalhes do artigo {nome_artigo.nome} foram atualizados:")
                                    nome_artigo.mostrar_artigo()

                                    break
                                 #
                            elif escolha_edicao == "3":
                                    break  # Para voltar ao menu.

                 # Se o utilizador escolher '3 - Eliminação de conta de um utilizador'.
                elif escolha_utilizadores == "3":
                    # Tem de estar dentro do loop para se conseguir voltar a atrás.
                    while True:
                        nome_usuario = input("Digite o nome do utilizador que deseja eliminar: ")
                        # Chama a função para eliminar o utilizador.
                        feira.eliminar_conta(nome_usuario)
                        break

                 # Se o utilizador escolher '4 - Lista de utilizadores'.
                elif escolha_utilizadores == "4":
                    lista_utilizadores = feira.listar_utilizadores()
                    print("Lista de Utilizadores: ")
                    break

                 # Se o utilizador escolher '5 - Mostrar artigos de um utilizador'.
                elif escolha_utilizadores == "5":
                    nome_mostrar_artigos = input("Escreve o nome do utilizador para obter os seus artigos: ")

                    feira.mostrar_artigos_utilizador(nome_mostrar_artigos)
                    break
                             
                 # Se o utilizador escolher '6 - Mostrar interesses de um utilizador'.
                elif escolha_utilizadores == "6":
                    nome_mostrar_interesses = input("Escreve o nome do utilizador para obter os seus interesses: ")
                    
                    feira.mostrar_interesses_utilizador(nome_mostrar_interesses)
                    break
                    

                 # Se o utilizador escolher '7 - Mostrar Pycoins de um utilizador'.
                elif escolha_utilizadores == "7":
                    nome_mostrar_pycoins = input("Escreve o nome do utilizador para saber a quantidade de Pycoins: ")
                    
                    feira.mostrar_pycoins_utilizador(nome_mostrar_pycoins)
                    break

                 # Se o utilizador escolher 'V - Voltar atrás'.
                elif escolha_utilizadores.upper() == "V":
                    break  # Para voltar ao menu.

                 # Se o utilizador escolher 'S - Sair'.
                elif escolha_utilizadores.upper() == "S":
                    print("Obrigado por usar a Feira Virtual. Até logo!")
                    return  # Para encerra o programa.







         # Se o utilizador escolher '2 - Artigos'.
        elif escolha == "2":
            # Tem de estar dentro do loop para se conseguir voltar a atrás.
            while True:
                print("Pretende aceder a:")
                print("1 - Mostrar preço de um artigo")
                print("2 - Mostrar quantidade de um artigo")
                print("3 - Mostrar tipo de um artigo")
                print("4 - Importar Artigos")
                print("V - Voltar atrás")
                print("S - Sair")

                escolha_artigos = input(" ")

                # Para garantir uma das escolhas pretendidas.
                while escolha_artigos not in ["1", "2", "3", "4", "V", "S"]:
                    print("Escolha uma opção válida:")
                    print("1 - Mostrar preço de um artigo")
                    print("2 - Mostrar quantidade de um artigo")
                    print("3 - Mostrar tipo de um artigo")
                    print("4 - Importar Artigos")
                    print("V - Voltar atrás")
                    print("S - Sair")

                    escolha_artigos = input(" ")

                # Se o utilizador escolher '1 - Mostrar preço de um artigo'.
                if escolha_artigos == "1":
                    pass

                 # Se o utilizador escolher '2 - Mostrar quantidade de um artigo'.
                elif escolha_artigos == "2":
                    pass
                 
                 # Se o utilizador escolher '3 - Mostrar tipo de um artigo'.
                elif escolha_artigos == "3":
                    pass

                 # Se o utilizador escolher '4 - Importar Artigos'.
                elif escolha_artigos == "4":
                    pass
                 
                  # Se o utilizador escolher 'V - Voltar atrás'.
                elif escolha_artigos.upper() == "V":
                    break  # Para voltar ao menu.
                 
                 # Se o utilizador escolher 'S - Sair'.
                elif escolha_artigos.upper() == "S":
                    print("Obrigado por usar a Feira Virtual. Até logo!")
                    return  # Para encerra o programa.







         # Se o utilizador escolher '3 - Mercado'.
        elif escolha == "3":
            # Tem de estar dentro do loop para se conseguir voltar a atrás.
            while True:
                print("Pretende aceder a:")
                print("1 - Adicionar Artigo ao Mercado")
                print("2 - Remover Artigo do Mercado")
                print("3 - Listar Artigos do Mercado")
                print("V - Voltar atrás")
                print("S - Sair")

                escolha_mercado = input(" ")

                # Para garantir uma das escolhas pretendidas.
                while escolha_mercado.upper() not in ["1", "2", "3", "V", "S"]:
                    print("Escolha entre:")
                    print("1 - Adicionar Artigo ao Mercado")
                    print("2 - Remover Artigo do Mercado")
                    print("3 - Listar Artigos do Mercado")
                    print("V - Voltar atrás")
                    print("S - Sair")

                    escolha_mercado = input(" ")

                # Se o utilizador escolher '1 - Adicionar Artigo ao Mercado'.
                if escolha_mercado == "1":
                    pass

                 # Se o utilizador escolher '2 - Remover Artigo do Mercado'.
                elif escolha_mercado == "2":
                    pass

                 # Se o utilizador escolher '3 - Listar Artigos do Mercado'.
                elif escolha_mercado == "3":
                    pass

                 #  Se o utilizador escolher 'V - Voltar atrás'.
                elif escolha_mercado.upper() == "V":
                    break  # Para voltar ao menu.

                 #  Se o utilizador escolher 'S - Sair'.
                elif escolha_mercado.upper() == "S":
                    print("Obrigado por usar a Feira Virtual. Até logo!")
                    return  # Para encerra o programa.


    main()

main()




    


    ###### Testes

    # feira_virtual = FeiraVirtual()

    ## Teste registar utilizador via ficheiro
    #feira_virtual.importar_utilizadores("C:/Users/biaga/Downloads/utilizadoresartigos.txt") #as barras têm que ser na direção /
    #feira_virtual.listar_utilizadores()

    ## Teste registar utilizador manualmente
    #nome_utilizador = input("Nome utilizador: ")
    #interesses_utilizador = input("Interesses: ")
    #artigos_utilizador = input("Artigos: ")

    #feira_virtual.registar_utilizador(nome_utilizador, interesses_utilizador, artigos_utilizador)
    #feira_virtual.registar_utilizador("Maria", "Cinema", "Jogo, 10, Tecnologia, 5")
    #feira_virtual.registar_utilizador("Beatriz", "Cinema", "Jogo, 10, Tecnologia, 5 & Livro HP, 12, Livro, 2")
    #feira_virtual.registar_utilizador("Sofia","[jogos,música]","[panela elétrica,8,cozinha,1&bilhete de avião para as Caraíbas,39,viagens,2]")
    #feira_virtual.listar_utilizadores()

    #Teste compra de artigo
    #feira_virtual.comprar_artigo("Manuel", "Ana", "telemóvel")
    #feira_virtual.mostrar_artigos_utilizador("Ana")

    #Teste comprar artigo nao disponivel
    #feira_virtual.comprar_artigo("Manuel", "Ana", "tv")

    #Teste listar interesses de todos os utilizadores
    #for utilizador in feira_virtual.utilizadores:
    #    utilizador.mostrar_interesses()

    #Teste listar artigos de todos os utilizadores
    #for utilizador in feira_virtual.utilizadores:
    #    utilizador.mostrar_artigos()

    #Teste alterar pycoins e mostrar
    #for utilizador in feira_virtual.utilizadores:
    #    utilizador.alterar_pycoins(1300)
    #    utilizador.mostrar_pycoins()

    #Teste mostrar interesses para utilizador
    #feira_virtual.mostrar_interesses_utilizador("Ana")

    #Teste mostrar artigos para utilizador
    #feira_virtual.mostrar_artigos_utilizador("Ana")

    #Teste mostrar pycoins para utilizador
    #feira_virtual.mostrar_pycoins_utilizador("Ana")

    #Testes aos artigos (editar e mostrar qtd, editar e mostrar tipo)
    #novo_artigo = Artigo("Jogo", 10, "Tecnologia", 2)

    #novo_artigo.editar_quantidade(5)
    #novo_artigo.mostrar_quantidade()
    #novo_artigo.editar_tipo("Desconhecido")
    #novo_artigo.mostrar_tipo()

    #Teste eliminar conta
    #feira_virtual.eliminar_conta("Ana")
    #feira_virtual.listar_utilizadores()

    #Teste listar artigos da feira por ordem 
    #feira_virtual.listar_artigos()


# diversão começa quando os utilizadores descobrem que certos artigos têm valores de 
#mercado que podem variar com base na oferta e procura

















if __name__ == '__main__':
    main()



#
#dados = [5, 1, 4, 2, 3, 4, 5, 2, 6, 5]

#frequencia = [0 for i in range(len(dados))] 

#for num in dados: 

#       frequencia[num-1] += 1 

#max_freq = max(frequencia)

#print(max_freq)

