from distutils.command.clean import clean

casas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

fim_do_jogo = False
vez_jogador_a = True
casa_escolhida = 0
casas_livres = 9
marcador_casa = "X"
ganhador = "Velha"

while fim_do_jogo == False: 
    print("\nJogador da vez:", marcador_casa, "\n\n")

    print("| ", end='')
    for casa in range(9):
        print(casas[casa], "| ", end='')
        if casa == 2 or casa == 5:
            print("\n-------------\n| ", end='')

    print("\n")
    casa_escolhida = int(input("Escolha uma casa válida ou 0 para sair: "))

    if casa_escolhida == 0:
        fim_do_jogo = True

    elif casa_escolhida >= 1 and casa_escolhida <= 9:

        if (not (casas[casa_escolhida - 1] == "X") and not (casas[casa_escolhida - 1] == "0")):
            # Marcar casa escolhida
            casas[casa_escolhida - 1] = marcador_casa
            vez_jogador_a = not vez_jogador_a
            casas_livres - 1

            if (casas[0] == casas[1] and casas[1] == casas[2]) or (casas[3] == casas[4] and casas[4] == casas[5]) or (casas[6] == casas[7] and casas[7] == casas[8]) or (casas[0] == casas[3] and casas[3] == casas[6]) or (casas[1] == casas[4] and casas[4] == casas[7]) or (casas[2] == casas[5] and casas[5] == casas[8]) or (casas[0] == casas[4] and casas[4] == casas[8]) or (casas[2] == casas[4] and casas[4] == casas[6]) :
                ganhador = "Jogador " + marcador_casa
                casas_livres = 0

    if casas_livres == 0:
        fim_do_jogo = True

    if vez_jogador_a:
        marcador_casa = "X"
    else:
        marcador_casa = "O"

print("Fim de Jogo!\n")
print("Ganhador: ", ganhador, "\n")

print("| ", end='')
for casa in range(9):
    print(casas[casa], "| ", end='')
    if casa == 2 or casa == 5:
         print("\n-------------\n| ", end='')






    



