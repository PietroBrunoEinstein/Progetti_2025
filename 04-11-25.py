def principale():
    nome = input("Inserisci il tuo nome: ")
    età = int(input("Inserisci la tua età: "))
    stringa = f"Lunghezza della stringa insufficiente.\nLa stringa deve essere almeno di quattro caratteri,\nma è di {len(nome)}."
    if len(nome) < 4:
        print(stringa)
        return
    if età % 3 == 0 and età % 2 != 0:
        stringa = nome[:2] + nome[-2:]
    else:
        stringa = nome[2:-2]
    print(f"La nuova stringa è '{stringa}'.")
    return

try:
    principale()
except Exception as e:

    print(f"Si è verificato un errore: '{e}'.")

