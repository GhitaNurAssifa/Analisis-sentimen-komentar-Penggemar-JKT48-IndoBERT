import pandas as pd

df = pd.read_csv("../data_clean/dataset_clean_youtube.csv")

kata_positif = [
    "keren","bagus","semangat","mantap","hebat",
    "bangga","cantik","lucu","gemas","gacor",
    "love","best","wow","suka","cocok",
    "menyala","kece","letsgo","akhirnya","selamat"
]

kata_negatif = [
    "jelek","error","buruk","kecewa","gagal",
    "aneh","ga suka","gk suka","nggak suka",
    "kurang bagus","kaga jelas","ga jelas",
    "terlalu gelap","payah","bosok",
    "lemot","sampah","nyinyir"
]

mask_pos = df["clean_comment"].str.contains(
    "|".join(kata_positif),
    case=False,
    na=False
)

mask_neg = df["clean_comment"].str.contains(
    "|".join(kata_negatif),
    case=False,
    na=False
)

netral = df[~mask_pos & ~mask_neg]

print("Jumlah kandidat netral:", len(netral))

netral.to_csv(
    "../data_label/kandidat_netral.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Tersimpan:")
print("../data_label/kandidat_netral.csv")