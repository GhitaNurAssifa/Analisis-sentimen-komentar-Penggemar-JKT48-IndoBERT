import pandas as pd

df = pd.read_csv("../data_clean/dataset_clean_youtube.csv")

kata_positif = [
    "keren",
    "bagus",
    "semangat",
    "mantap",
    "hebat",
    "bangga",
    "cantik",
    "lucu",
    "gemas",
    "gacor",
    "love",
    "best",
    "wow",
    "suka",
    "cocok",
    "menyala",
    "kece",
    "letsgo",
    "akhirnya",
    "selamat"
]

mask = df["clean_comment"].str.contains(
    "|".join(kata_positif),
    case=False,
    na=False
)

positif = df[mask]

print("Jumlah kandidat positif:", len(positif))

positif.to_csv(
    "../data_label/kandidat_positif.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Tersimpan:")
print("../data_label/kandidat_positif.csv")