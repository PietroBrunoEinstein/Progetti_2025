import math
import os

def esercizio_1():
    # Inserisci tre numeri interi e verifica se sono tutti diversi
    numero1 = int(input("Inserisci il primo numero intero: "))
    numero2 = int(input("Inserisci il secondo numero intero: "))
    numero3 = int(input("Inserisci il terzo numero intero: "))
    if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        # Se non lo sono , stampa un messaggio di errore
        print("Errore\nAlmeno due numeri sono uguali")
        return
    elif numero1 == 0 or numero2 == 0 or numero3 == 0:
        # Se uno dei numeri è zero, stampa un messaggio di errore
        print("Errore\nAlmeno un numero è uguale a zero")
        return
    else:
        # Se lo sono, stampali in ordine decrescente
        lista = [numero1, numero2, numero3]
        lista = sorted(lista)
        print(f"I numeri sono tutti diversi. Ecco i numeri in ordine decrescente:\n{lista[2]}\n{lista[1]}\n{lista[0]}")
        return

def esercizio_2():
    # Inserimento del voto
    voto = int(input("Inserisci il voto (0-10): "))
    # Verifica del voto e stampa del giudizio
    if voto > 10 or voto < 0:
        # Se il voto non è valido, stampa un messaggio di errore
        print("Valore del voto non valido")
        return
    elif 10 >= voto >= 6:
        # Se il voto è sufficiente o superiore (6+), stampa "sei sufficiente"
        print("sei sufficiente")
        return
    else:
        if voto <= 4:
            # Se il voto è gravemente insufficiente (0-4), stampa "sei gravemente insufficiente"
            print("Sei gravemente insufficiente")
            return
        else:
            # Altrimenti stampa "sei insufficiente"
            print("Sei insufficiente")
            return

def esercizio_3():
    # Inserimento lati del triangolo
    lato1 = float(input("Inserisci il primo lato del triangolo: "))
    lato2 = float(input("Inserisci il secondo lato del triangolo: "))
    lato3 = float(input("Inserisci il terzo lato del triangolo: "))
    lati = [lato1, lato2, lato3]
    lati = sorted(lati)
    if lato1 < 0 or lato2 < 0 or lato3 < 0:
        # Se uno dei lati è negativo, stampa un messaggio di errore
        print("La misura dei lati non può essere negativa")
        return
    elif lati[0] + lati[1] <= lati[2]:
        # Se la somma dei due lati più piccoli non è maggiore del lato più grande, stampa un messaggio di errore
        # (I lati specificati non possono formare un triangolo)
        print("Valori dei lati non validi")
        return
    # Calcolo del teorema di Pitagora
    cateto1 = lati[0]
    cateto2 = lati[1]
    ipotenusa = math.sqrt((cateto1 ** 2) + (cateto2 ** 2))
    if ipotenusa == lati[2]:
        # Se il teorema di Pitagora è verificato, stampa che il triangolo è rettangolo
        print("Il triangolo è rettangolo")
        return
    else:
        # Altrimenti stampa che il triangolo non è rettangolo
        print("Il triangolo non è rettangolo")
        return

def esercizio_4():
    # Inserimento di due orari in formato oo:mm:ss (24 ore) e verifica quale dei due viene prima
    orario1 = input("Inserisci il primo orario (formato: oo:mm:ss | 24 ore): ")
    orario2 = input("Inserisci il secondo orario (formato: oo:mm:ss | 24 ore): ")
    if ":" not in orario1 or ":" not in orario2 or len(orario2) != 8 or len(orario2) != 8:
        # Se il formato non è corretto, stampa un messaggio di errore
        print("Formato o valore non valido")
        return
    orario1 = orario1.replace(":", "")
    orario2 = orario2.replace(":", "")
    if int(orario1[0:2]) > 23 or int(orario1[2:4]) > 59 or int(orario1[4:6]) > 59 or int(orario2[0:2]) > 23 or int(orario2[2:4]) > 59 or int(orario2[4:6]) > 59:
        # Se uno degli orari non è valido, stampa un messaggio di errore
        print("Formato o valore non valido")
        return
    # Confronto degli orari
    orario1 = int(orario1)
    orario2 = int(orario2)
    if orario1 == orario2:
        print("I due orari inseriti sono uguali")
        return
    elif orario1 < orario2:
        print("Il primo orario viene prima del secondo orario")
        return
    else:
        print("Il secondo orario viene prima del primo orario")
        return

def esercizio_5():
    # Conversione della temperatura da Celsius a Kelvin e Fahrenheit
    temperatura_celsius = float(input("Inserisci la temperatura in Celsius: "))
    if temperatura_celsius < -273.15:
        # Se la temperatura è inferiore allo zero assoluto, stampa un messaggio di errore.
        print("Valore della temperatura non valido")
        return
    # Calcolo delle temperature convertite
    temperatura_kelvin = temperatura_celsius * (9/5) + 32.0
    temperatura_fahrenheit = temperatura_celsius + 273.15
    print(f"La temperatura converita in Kelvin è di {temperatura_kelvin:.2f}°K\nLa temperatura in Fahrenheit è di {temperatura_fahrenheit:.2f}°F")
    return

def esercizio_6():
    # Rimozione della prima e dell'ultima lettera di una parola di almeno tre caratteri
    parola = input("Inserisci la tua parola di almeno tre caratteri: ")
    if len(parola) < 3:
        # Se la parola è troppo corta, stampa un messaggio di errore.
        print("Lunghezza della stringa non sufficiente")
        return
        # Rimozione della prima e dell'ultima lettera
    nuova_parola = parola[1:-1]
    print(f"La parola senza la prima e l'ultima lettera è {nuova_parola}")
    return

def esercizio_7():
    # Sostituzione della prima lettera di una parola con la lettera successiva nell'alfabeto (ciclica: "z"->"a" e "Z"->"A")
    parola = input("Inserisci una parola: ")
    if len(parola) < 1:
        # Se la stringa è vuota stampa errore
        print("Lunghezza della stringa non sufficiente")
        return
    # Sostituzione della prima lettera
    # Selezione della prima lettera
    prima_lettera = parola[0]
    if "a" <= prima_lettera <= "z":
        # Se la prima lettera è "z", sostituiscila con "a"
        if prima_lettera == "z":
            nuova_prima_lettera = "a"
        else:
            nuova_prima_lettera = chr(ord(prima_lettera) + 1)
    elif "A" <= prima_lettera <= "Z":
        # Se la prima lettera è "Z", sostituiscila con "A"
        if prima_lettera == "Z":
            nuova_prima_lettera = "A"
        else:
            nuova_prima_lettera = chr(ord(prima_lettera) + 1)
    # Creazione nuova parola
    nuova_parola = nuova_prima_lettera + parola[1:]
    print(f"La stringa modificata è: {nuova_parola}")
    return

def esercizio_8():
    # Verifica se il primo e l'ultimo carattere di una parola di almeno due caratteri sono uguali o diversi
    parola = input("Inserisci la tua parola di almeno due caratteri: ")
    if len(parola) < 2:
        # Se la parola è troppo corta, stampa un messaggio di errore.
        print("Lunghezza della stringa non sufficiente")
        return
    prima_lettera = parola[0]
    ultima_lettera = parola[-1]
    if prima_lettera == ultima_lettera:
        # Se il primo e  l'ultimo carattere sono uguali, stampa "Il primo e l'ultimo carattere sono uguali"
        print("Il primo e l'ultimo carattere sono uguali")
        return
    else:
        # Altrimenti stampa "Il primo e l'ultimo carattere sono diversi"
        print("Il primo e l'ultimo carattere sono diversi")
        return

def esercizio_9():
    # Creazione di una nuova parola composta dalla prima metà della prima parola e dalla seconda metà della seconda parola
    parola1 = input("Inserisci la prima parola : ")
    parola2 = input("Inserisci la seconda parola : ")
    if len(parola1) < 2 or len(parola2) < 2:
        # Se una delle due parole è troppo corta, aggiungi le due parole senza modificarle
        metà_parola1 = parola1
        metà_parola2 = parola2
        nuova_parola = metà_parola1 + metà_parola2
        print(f"La nuova parola è: {nuova_parola}")
        return
    elif len(parola1) % 2 == 0 and len(parola2) % 2 == 0:
        # Se entrambe le parole hanno una lunghezza pari, prendi esattamente la metà di ciascuna parola
        metà_parola1 = parola1[:(len(parola1) // 2)]
        metà_parola2 = parola2[(len(parola2) // 2):]
    else:
        # Se una delle due parole ha una lunghezza dispari, prendi la metà arrotondata per eccesso della prima parola e la metà arrotondata per difetto della seconda parola
        metà_parola1 = parola1[:((len(parola1) // 2 + 1))]
        metà_parola2 = parola2[(len(parola2) // 2):]
    nuova_parola = metà_parola1 + metà_parola2
    print(f"La nuova parola è: {nuova_parola}")
    return

def esercizio_10():
    # Creazione di una nuova stringa sostituendo una parte della prima stringa con una parte della seconda stringa
    s1 = input("Inserisci la prima stringa: ")
    s2 = input("Inserisci la seconda stringa: ")
    n1 = int(input("Inserisci un numero intero per la prima stringa: "))
    n2 = int(input("Inserisci un numero intero per la seconda stringa: "))
    l1 = len(s1)
    l2 = len(s2)
    if n1 < 0 or n2 < 0 or n2 > l1 or n1 > l2 or l1 == 0 or l2 == 0:
        print("Valori non validi")
        return
    nuova_stringa = s1[:n1] + s2[n1:(n2 + 1)] + s1[(n2 + 1):]
    print(f"La nuova stringa è: {nuova_stringa}")
    return

def principale():
    try:
        esercizio_1(), esercizio_2(), esercizio_3(), esercizio_4(), esercizio_5(), esercizio_6(), esercizio_7(), esercizio_8(), esercizio_9(), esercizio_10()
    except Exception as e:
        os.system("cls")
        os.system("color 4")
        print(f"Si è verificato un errore: '{e}'.\nRiprova l'esecuzione del programma.")
    finally:
        os.system("pause")
        os.system("color 7")
        os.system("cls")
    return

principale()