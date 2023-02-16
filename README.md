# Projeto-copa-do-mundo
Projeto realizado no segundo semestre de ADS, utilizando Phyton 

"""
Faça um algoritmo que utilize o menu abaixo:

MENU
======
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir escalação
Escolha: 


Opção 1: Ler de um arquivo texto todos os jogadores
        escalados para a copa e armazenar em uma
        lista (lst_jogadores)
        Cada Elemento da lista será uma instância
            da classe Jogador.

Opção 2: Você deverá escalar 11 dos jogadores para
        iniciar a partida.
        Os Jogadores escalados para a partida ficam
            em uma lista (lst_escalados)
            Alterar o atributo 'participou_partida'
                para True
        Os jogadores que não forem escalados para
            iniciar a partida ficam em uma outra
            lista (lst_reserva)
Opção 3: Você poderá realizar a substituição de um
        jogador por outro.
        Quando isso acontecer o jogador vai para
            a lista de Reserva e o outro para a
            lista Escalados.

Opção 4: Caso haja alguma expulsão, o jogador sai
        da lista de Escalados e vai para a lista
        Reserva.

Opção 5: Mostrar a escalação de todos jogadores que
        participaram do jogo, inclusive as substituições
        e expulsões. 
        Salve esses dados em um arquivo (todosjogadores.txt)


class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False # ou True


arquivo texto para leitura (convocados.txt):
1:Alisson:GOLEIRO
2:Danilo:DEFESA
3:Thiago Silva:DEFESA
4:Marquinhos:DEFESA
5:Casemiro:MEIO-CAMPO
6:Alex Sandro:DEFESA
7:Lucas Paquetá:MEIO-CAMPO
8:Fred:MEIO-CAMPO
9:Richarlison:ATACANTE
10:Neymar:ATACANTE
11:Raphinha:ATACANTE
12:Weverton:GOLEIRO
13:Dani Alves:DEFESA
14:Éder Millitão:DEFESA
15:Fabinho:MEIO-CAMPO
16:Alex Telle:DEFESA
17:Bruno Guimarães:MEIO-CAMPO
18:Gabriel Jesus:ATACANTE
19:Antony:ATACANTE
20:Vinicius Junior:ATACANTE
21:Rodrygo:ATACANTE
22:Éverton Ribeiro:MEIO-CAMPO
23:Ederson:GOLEIRO
24:Bremer:DEFESA
25:Pedro:ATACANTE
26:Gabriel Martinelli:ATACANTE
"""
