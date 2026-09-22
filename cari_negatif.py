import pandas as pd

df = pd.read_csv("../data_clean/dataset_clean_youtube.csv")

kata_negatif = [
    "jelek",
    "error",
    "buruk",
    "kecewa",
    "gagal",
    "aneh",
    "ga suka",
    "gk suka",
    "nggak suka",
    "kurang bagus",
    "kaga jelas",
    "ga jelas",
    "terlalu gelap",
    "payah",
    "bosok",
    "lemot",
    "sampah",
    "nyinyir"
]

mask = df["clean_comment"].str.contains(
    "|".join(kata_negatif),
    case=False,
    na=False
)

negatif = df[mask]

print("Jumlah kandidat negatif:", len(negatif))

negatif.to_csv(
    "../data_label/kandidat_negatif.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Tersimpan:")
print("../data_label/kandidat_negatif.csv")