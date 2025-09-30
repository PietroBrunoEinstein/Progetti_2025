NumeroVoti = int(input("Inserisci il numero di voti: "))

SommaVoti = 0
for i in range(NumeroVoti):
    Voto = float(input(f"Inserisci il {i + 1}° voto: "))
    SommaVoti += Voto
MediaVoti = SommaVoti / NumeroVoti

print(f"La media dei voti è: {MediaVoti:.2f}")