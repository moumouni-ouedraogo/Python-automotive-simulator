capacite_batterie = 60  # en KWh
consommation_totale = 0.15  # KWh/km

print("=== SIMULATEUR DE BATTERIE EV ===")
distance = float(input("Entrez la distance à parcourir (en km) : "))

energie_consommee = distance * consommation_totale
energie_restante = capacite_batterie - energie_consommee
pourcentage_restante = (energie_restante * 100) / capacite_batterie

if pourcentage_restante < 0:
    print("ALERTE ! La batterie sera vide avant l'arrivée.")
else:
    print(f"Il vous restera {pourcentage_restante:.2f}% de batterie.")
