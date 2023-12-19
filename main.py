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
            for interesse in self.interesses:
              
                print(interesse)

        #Apresenta todos os artigos.
        def mostrar_artigos(self):
         print(f"Artigos disponíveis de {self.nome}:")
         if not self.artigos_disponiveis:
            print("O utilizador não tem artigos disponíveis.")
         else:
            for artigo in self.artigos_disponiveis:
              
                print(artigo)

        #Altera o número de pycoins.
        def alterar_pycoins(self, numero_pycoins):
           self.pycoins = numero_pycoins
           print(f" O Número de pycoins de {self.nome} altera para o {numero_pycoins}.")

        #Apresenta o número de pycoins.
        def mostrar_pycoins(self):
         print(f" número de pycoins de {self.nome}")
         if not self.pycoins:
            print("O utilizador não tem pycoins disponíveis.")
         else:
             print(self.pycoins)
    

    #Funcionalidades relativas a um artigo
    class Artigo:
       #Construtor
        def __init__(self, nome, preco, tipologia, quantidade):
            self.nome = nome
            self.preco = preco
            self.tipologia = tipologia
            self.quantidade = quantidade

        #Altera o nome de um artigo para o novo nome recebido
        def editar_nome(self, nome):
            pass
        
        #Altera o preço de um artigo de acordo com a percentagem dada
        def ajustar_preco(self, percentagem_alteracao):
            pass
        
        #Altera o preço para o novo preço recebido
        def editar_preco(self, preco):
            pass
        
        #Apresenta o preço do artigo
        def mostrar_preco(self):
            pass
        
        #Altera a quantidade
        def editar_quantidade(self, nova_quantidade):
            pass
        
        #Apresenta a quantidade do artigo
        def mostrar_quantidade(self):
            pass
        
        #Altera a tipologia
        def editar_tipo (self, novo_tipo):
            pass
        
        #Apresenta a tipologia do artigo
        def mostrar_tipo (self):    
            pass
        















if __name__ == '__main__':
    main()



#
dados = [5, 1, 4, 2, 3, 4, 5, 2, 6, 5]

frequencia = [0 for i in range(len(dados))] 

for num in dados: 

       frequencia[num-1] += 1 

max_freq = max(frequencia)

print(max_freq)
