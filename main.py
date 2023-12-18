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
            # O '.append()' é um método que adiciona um elemento ao final da lista.
            # O '{"estrelas": estrelas, "comentario": comentario}' é um dicionário. Está a ser adicionado à lista de avaliações. Este dicionário representa uma única avaliação feita pelo usuário. Ele tem duas chaves: "estrelas" e "comentario".
            # 'estrelas' e 'comentario' atribuiem o valor da variável à palavra chave "estrelas" e "comentario" no dicionário. 
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
            pass

        #Apresenta todos os artigos.
        def mostrar_artigos(self):
            pass

        #Altera o número de pycoins.
        def alterar_pycoins(self, numero_pycoins):
            pass

        #Apresenta o número de pycoins.
        def mostrar_pycoins(self):
            pass
    


if __name__ == '__main__':
    main()