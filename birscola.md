```mermaid
classDiagram
    class Carta {
    +Str seme
    +Str valore
    }
    
    class Mazzo {
    +List carte
    + costruisci_mazzo()
    + mischia()
    + pesca()
    }

    class Mano {
    +List carte
    + get_valore_reale()
    }

    class Player {
    +Str nome
    + Obj Mano
    + gioca()
    + calcola_punteggio()
    }

    class Computer {
    +Str nome
    +Obj player
    +Obj comanda
    +Obj Mano
    + gioca()
    + calcola_punteggio()
    }
    
    Mazzo "1"--"n" Carta: contiene
    Player "1"--"1" Mano
    Player "1" -- "1" Player: si batte con
    Player "1" -- "1" Computer: si batte con
    Mano "1" -- "3" Carta: contiene