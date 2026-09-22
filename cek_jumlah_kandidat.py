import pandas as pd

positif = pd.read_csv("../data_label/kandidat_positif.csv")
netral = pd.read_csv("../data_label/kandidat_netral.csv")
negatif = pd.read_csv("../data_label/kandidat_negatif.csv")

print("Positif :", len(positif))
print("Netral  :", len(netral))
print("Negatif :", len(negatif))