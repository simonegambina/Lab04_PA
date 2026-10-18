from stand import Stand, StandPreseExtra, StandPremium

s1 = Stand("ST1", 9, 1, 150)
s2 = StandPreseExtra("ST2", 12, 2, 220, 3)
s3 = StandPremium("ST3", 6, 1, 180, "Ingresso")

print(s1.calcola_prezzo())
print(s2.calcola_prezzo())
print(s3.calcola_prezzo())

print(s1)
print(s2)
print(s3)