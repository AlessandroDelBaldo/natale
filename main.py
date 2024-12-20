import random, os
deposito = 1000
premio = 0
simboli = ["🍒","💸","🍇","💥"]
play = input("Play? (S/N)")
while play == "S" or play == "s":
    while True:
        puntata = int(input("Inserisci puntata:"))
        if puntata < 1:
            print("Puntata non corretta, riprova.")
        else:
            break
    slot = ["-", "-", "-"]
    input(f"Premi INVIO per giocare!\n{slot}")
    while True:
        os.system('cls'if os.name == 'nt' else 'clear')
        for i in range(3):
            simbolo = random.choice(simboli)
            slot[i] = simbolo
        print(slot)
        if slot[0] == slot[1] and slot[1] == slot[2]:
            if slot[0] == "🍒":
                premio = puntata*4
                deposito += puntata
                print(f"Che fortuna! Hai vinto {premio}€!!\ncredito: {deposito} \t puntata: {puntata}")
            elif slot[0] == "💸":
                premio = puntata*5
                deposito += puntata
                print(f"Che fortuna! Hai vinto {premio}€!!\ncredito: {deposito} \t puntata: {puntata}")
            elif slot[0] == "🍇":
                premio = puntata*10
                deposito += puntata
                print(f"Che fortuna! Hai vinto {premio}€!!\ncredito: {deposito} \t puntata: {puntata}")
            elif slot[0] == "💥":
                premio = puntata*20
                deposito += puntata
                print(f"Sbancato cazzo {premio}€!!\ncredito: {deposito} \t puntata: {puntata}")
        else:
            deposito -= puntata
            print(f"Ritenta, sarai più fortunato\ncredito: {deposito} \t puntata: {puntata}")
        replay = input("Rprovare? (S/N)")
        if replay == "S" or replay == "s":
            continue
        else:
            print("Grazie per aver giocato!")
            break
    break