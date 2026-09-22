import pandas as pd

positif = pd.read_csv("../data_label/kandidat_positif.csv")
netral = pd.read_csv("../data_label/kandidat_netral.csv")
negatif = pd.read_csv("../data_label/kandidat_negatif.csv")

positif = positif.sample(n=500, random_state=42)
netral = netral.sample(n=700, random_state=42)
negatif = negatif.sample(n=300, random_state=42)

positif["label"] = "positif"
netral["label"] = "netral"
negatif["label"] = "negatif"

dataset = pd.concat(
    [positif, netral, negatif],
    ignore_index=True
)

dataset = dataset.sample(
    frac=1,
    random_state=42
)

dataset.to_csv(
    "../data_label/dataset_final_1500.csv",
    index=False,
    encoding="utf-8-sig"
)

print(dataset["label"].value_counts())
print("\nTotal:", len(dataset))