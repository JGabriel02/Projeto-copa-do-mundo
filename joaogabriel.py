

lst_jogadores = []
lst_escalados = []
lst_reserva = []

class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao
        self.__situacao = "NORMAL"
        self.__participou_partida = False

    def get_numero(self):
        return self.__numero

    def get_nome_jogador(self):
        return self.__nome_jogador

    def get_posicao(self):
        return self.__posicao

    def get_situacao(self):
        return self.__situacao

    def get_participou_partida(self):
        return self.__participou_partida

    def set_participou_partida(self, sim):
        self.__participou_partida = sim

    def set_situacao(self, legal):
        self.__situacao = legal

    def __str__(self):
        return f"Nome: {self.__nome_jogador} - {self.__numero} {self.__posicao}"

def lerArquivo():
    arquivo = open("convocados.txt", "r")
    for i in arquivo:
        if i == '26:Gabriel Martinelli:ATACANTE':
            numero, nome, posicao = i[:].split(':')
            jogador = (Jogador(nome, numero, posicao))
            lst_jogadores.append(jogador)
        else:
            numero, nome, posicao = i[:].split(':')
            posicao = posicao[:-1]
            jogador = (Jogador(nome, numero, posicao))
            lst_jogadores.append(jogador)
    for i in (lst_jogadores):
        print(i)

    arquivo.close()




def GK():
    gk = ""
    while gk != 'GOLEIRO':
        ja_escalado = False
        jogador = input("Escolha o Goleiro titular pelo numero (Goleiros: 1,12,23): ")
        for i, goleiro in enumerate(lst_jogadores):
            print(f"{i+1}. {goleiro.get_nome_jogador()}")
            if goleiro.get_numero() == jogador:
                if goleiro.get_posicao() == 'GOLEIRO':
                    for linha in lst_escalados:
                        ja_escalado = False
                        if linha.get_numero() == jogador:
                            ja_escalado = True
                            print("Jogador já está escalado")
                            break
                    if not ja_escalado:
                        gk = 'GOLEIRO'
                        goleiro.set_participou_partida(True)
                        lst_escalados.append(goleiro)
                        lst_jogadores[i] = goleiro
                        break


def escalarLinha():
    duplicado = False
    jogador = input("Escolha os Jogadores Titulares pelos Numeros: ")
    for i, titulares in enumerate(lst_jogadores):
        if titulares.get_numero() == jogador:
            for linha in lst_escalados:
                duplicado = False
                if linha.get_numero() == jogador:
                    duplicado = True
                    print("Jogador já escalado")
                    break
            if not duplicado:
                titulares.set_participou_partida(True)
                lst_escalados.append(titulares)
                lst_jogadores[i] = titulares
                break
def reserva():
    for i in lst_jogadores:
        dentro = False
        for j in lst_escalados:
            if i.get_numero() == j.get_numero():
                dentro = True
                break
        if not dentro:
            lst_reserva.append(i)
def substituicao():
    for l in lst_escalados:
        print("Numero: ", l.get_numero(), " Nome: ", l.get_nome_jogador(), " Posição: ", l.get_posicao(),)
    entrou = False
    print("Substituição na equipe Brasieira")
    sai = input("\n Galvão está saindo o camisa: ")
    for j in lst_jogadores:
        if j.get_numero() == sai:
            lst_escalados.remove(j)
            lst_reserva.append(j)
            break
    print("------------------------------")
    for l in lst_reserva:
        print("Numero: ", l.get_numero(), " Nome: ", l.get_nome_jogador(), " Posição: ", l.get_posicao(),)
    entra = input("\n Para a entrada do camisa: ")
    for ind, jogadores in enumerate(lst_jogadores):
        if jogadores.get_numero() == entra:
            lst_reserva.remove(jogadores)
            lst_escalados.append(jogadores)
            jogadores.set_participou_partida(True)
            lst_jogadores[ind] = jogadores
            entrou = True

    if entrou:
        print("Substituição Feita")


def expulsao():
    print("primmm! Um Jogador foi expulso")
    for l in lst_escalados:
        print("Numero: ", l.get_numero(), " Nome: ", l.get_nome_jogador(), " Posição: ", l.get_posicao(),)
    sai = input("\n Galvão foi expulso o Jogador camisa: ")
    for i,  jogadores in enumerate(lst_jogadores):
        if jogadores.get_numero() == sai:
            for escalado in lst_escalados:
                if escalado.get_numero() == sai:
                    lst_escalados.remove(jogadores)
                    lst_reserva.append(jogadores)
                    jogadores.set_situacao("EXPULSO")
                    lst_jogadores[i] = jogadores
                    break



def imprimirJogaram():
    print("\n Escalação: ")
    for l in lst_jogadores:
        if l.get_participou_partida():
            grava_arquivo(l.get_numero(), l.get_nome_jogador(), l.get_posicao(), l.get_situacao())
            print("Numero: ", l.get_numero(), " Nome: ", l.get_nome_jogador(), " Posição: ", l.get_posicao(), "Situação: ", l.get_situacao())


def grava_arquivo(numero, nome, posicao, situacao):
    try:
        arquivo = open("todosjogadores.txt", "a")
    except:
        arquivo = open("todosjogadores.txt", "w")

    arquivo.write(str(numero) + ":" + nome + ":" + posicao + ":" + situacao + "\n")
    arquivo.close()


def menu():
    while True:
        escolha = input(
            """
        =======================================
            MENU:
        ---------------------------------------
        1- Ler arquivo de jogadores
        2- Escalar time
        3- Realizar Substiuição
        4- Expulsão
        5- Imprimir escalação
            Escolha: """
        )

        if escolha == '1':
            lerArquivo()
        if escolha == '2':
            GK()
            while True:
                escalarLinha()
                if (len(lst_escalados)) == 11:
                    break
            reserva()
        if escolha == '3': substituicao()
        if escolha == '4': expulsao()
        if escolha == '5': imprimirJogaram()

menu()
