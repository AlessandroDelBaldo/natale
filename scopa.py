import random, os

class Carta:
    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore
        self.valore_reale = 0

    def __repr__(self):
        return f"{self.valore} di {self.seme}"

class Mazzo:
    def __init__(self):
        self.carte = []
        self.costruisci_mazzo()

    def costruisci_mazzo(self):
        self.carte = []
        for seme in ["⚔", "🏆", "💲", "🌲"]:
        #for seme in ["denari", "coppe", "spade", "bastoni"]:
            for valore in ["asso", "due", "tre", "quattro", "cinque", "sei", "sette", "fante", "cavallo", "re"]:
                self.carte.append(Carta(seme, valore))

    def mischia(self):
        if len(self.carte) > 1:
            for _ in range(5):
                random.shuffle(self.carte)
    
    def pesca(self):
        carta = self.carte.pop(0)
        return carta

class Mano:
    def __init__(self):
        self.carte = []

    def get_valore_reale(self,carta_scelta):
        if carta_scelta.valore == "asso":
            carta_scelta.valore_reale = 12
        elif carta_scelta.valore == "due":
            carta_scelta.valore_reale = 2
        elif carta_scelta.valore == "tre":
            carta_scelta.valore_reale = 11
        elif carta_scelta.valore == "quattro":
            carta_scelta.valore_reale = 4
        elif carta_scelta.valore == "cinque":
            carta_scelta.valore_reale = 5
        elif carta_scelta.valore == "sei":
            carta_scelta.valore_reale = 6
        elif carta_scelta.valore == "sette":
            carta_scelta.valore_reale = 7
        elif carta_scelta.valore == "fante":
            carta_scelta.valore_reale = 8
        elif carta_scelta.valore == "cavallo":
            carta_scelta.valore_reale = 9
        elif carta_scelta.valore == "re":
            carta_scelta.valore_reale = 10
        
    def __repr__(self):
        return f"{self.carte}"

class Player:
    def __init__(self, nome):
        self.nome = nome
        self.mano = Mano()
    
    def gioca(self):
        print(f"{self.nome} tocca a te")
        scelta = int(input(f"scegli quale carta giocare (1-{len(self.mano.carte)-1}): "))
        scelta -= 1
        carta_scelta = self.mano.carte[scelta]
        self.mano.carte.pop(scelta)
        return carta_scelta
    
    def calcola_punteggio(self, carte_prese):
        punteggio = 0
        for carta in carte_prese:
            if carta.valore == "asso":
                carta.punteggio = 11
            elif carta.valore == "due":
                carta.punteggio = 0
            elif carta.valore == "tre":
                carta.punteggio = 10
            elif carta.valore == "quattro":
                carta.punteggio = 0
            elif carta.valore == "cinque":
                carta.punteggio = 0
            elif carta.valore == "sei":
                carta.punteggio = 0
            elif carta.valore == "sette":
                carta.punteggio = 0
            elif carta.valore == "fante":
                carta.punteggio = 2
            elif carta.valore == "cavallo":
                carta.punteggio = 3
            elif carta.valore == "re":
                carta.punteggio = 4
            punteggio += carta.punteggio
        return punteggio

def briscola():
    mazzo = Mazzo()
    mazzo.mischia()
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    comanda = mazzo.carte.pop(0)
    mazzo.carte.append(comanda)
    carte_prese1 = []
    carte_prese2 = []
    turno = True
    n_turno = 1
    for i in range(3):
        player1.mano.carte.append(mazzo.pesca())
        player2.mano.carte.append(mazzo.pesca())
    while True:
        os.system('cls'if os.name == 'nt' else 'clear')
        print(f"{player1.nome}: {player1.mano.carte}\t{player2.nome}: {player2.mano.carte}\n Comanda: {comanda}\t Carte rimanenti: {len(mazzo.carte)}")
        if len(mazzo.carte) > 0:
            if turno is True:
                player1.mano.carte.append(mazzo.pesca())
                player2.mano.carte.append(mazzo.pesca())
                carta_scelta1 = player1.gioca()
                print(f"{player1.nome} ha giocato: {carta_scelta1}")
                carta_scelta2 = player2.gioca()
                print(f"{player2.nome} ha giocato: {carta_scelta2}")

            elif turno is False:
                player2.mano.carte.append(mazzo.pesca())
                player1.mano.carte.append(mazzo.pesca())
                carta_scelta2 = player2.gioca()
                print(f"{player2.nome} ha giocato: {carta_scelta2}")
                carta_scelta1 = player1.gioca()
                print(f"{player1.nome} ha giocato: {carta_scelta1}")

            elif n_turno == 1:
                carta_scelta1 = player1.gioca()
                print(f"{player1.nome} ha giocato: {carta_scelta1}")
                carta_scelta2 = player2.gioca()
                print(f"{player2.nome} ha giocato: {carta_scelta2}")
        else:
            if turno is True:
                carta_scelta1 = player1.gioca()
                print(f"{player1.nome} ha giocato: {carta_scelta1}")
                carta_scelta2 = player2.gioca()
                print(f"{player2.nome} ha giocato: {carta_scelta2}")
            
            elif turno is False:
                carta_scelta2 = player2.gioca()
                print(f"{player2.nome} ha giocato: {carta_scelta2}")
                carta_scelta1 = player1.gioca()
                print(f"{player1.nome} ha giocato: {carta_scelta1}")
                
        if turno == True:
            if carta_scelta1.seme == carta_scelta2.seme:
                if carta_scelta1.valore_reale > carta_scelta2.valore_reale:
                    carte_prese1.append(carta_scelta1)
                    carte_prese1.append(carta_scelta2)
                    print(f"{player1.nome} ha preso {carta_scelta1} e {carta_scelta2}")
                    turno = True
                else:
                    carte_prese2.append(carta_scelta1)
                    carte_prese2.append(carta_scelta2)
                    print(f"{player2.nome} ha preso {carta_scelta1} e {carta_scelta2}")
                turno = False
            else:
                if carta_scelta2.seme == comanda.seme:
                    carte_prese2.append(carta_scelta1)
                    carte_prese2.append(carta_scelta2)
                    print(f"{player2.nome} ha preso {carta_scelta1} e {carta_scelta2}")
                    turno = False
                else:
                    carte_prese1.append(carta_scelta1)
                    carte_prese1.append(carta_scelta2)
                    print(f"{player1.nome} ha preso {carta_scelta1} e {carta_scelta2}")
                    turno = True
        else:
            if carta_scelta1.seme == carta_scelta2.seme:
                if carta_scelta1.valore_reale > carta_scelta2.valore_reale:
                    carte_prese1.append(carta_scelta1)
                    carte_prese1.append(carta_scelta2)
                    print(f"{player1.nome} ha preso {carta_scelta1} e {carta_scelta2}")
                    turno = True
                else:
                    carte_prese2.append(carta_scelta1)
                    carte_prese2.append(carta_scelta2)
                    print(f"{player2.nome} ha preso {carta_scelta1} e {carta_scelta2}")
                    turno = False
                    
            else:
                if carta_scelta1.seme == comanda.seme:
                    carte_prese1.append(carta_scelta1)
                    carte_prese1.append(carta_scelta2)
                    print(f"{player1.nome} ha preso {carta_scelta1} e {carta_scelta2}")
                    turno = True
                else:
                    carte_prese2.append(carta_scelta1)
                    carte_prese2.append(carta_scelta2)
                    print(f"{player2.nome} ha preso {carta_scelta1} e {carta_scelta2}")
                    turno = False

        print(player1.calcola_punteggio(carte_prese1))
        print(player2.calcola_punteggio(carte_prese2))
        n_turno += 1
        input("Premi un tasto per continuare")
        if len(player1.mano.carte) == 0 and len(player2.mano.carte) == 0:
            if player1.calcola_punteggio(carte_prese1) > player2.calcola_punteggio(carte_prese2):
                print(f"{player1.nome} ha vinto con {player1.calcola_punteggio(carte_prese1)} punti")
            else:
                print(f"{player2.nome} ha vinto con {player2.calcola_punteggio(carte_prese2)} punti")
            break

if __name__ == "__main__":
    briscola()