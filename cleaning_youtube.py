import pandas as pd
import re

print("Membaca dataset...")

df = pd.read_csv("../data_raw/komentar_youtube_jkt48.csv")

print("Jumlah awal:", len(df))

def clean_text(text):

    text = str(text).lower()

    # hapus URL
    text = re.sub(r'http\S+', '', text)

    # hapus mention
    text = re.sub(r'@\w+', '', text)

    # hapus emoji & simbol
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # hapus spasi berlebih
    text = re.sub(r'\s+', ' ', text).strip()

    return text

df["clean_comment"] = df["comment"].apply(clean_text)

# hapus yang kosong setelah cleaning
df = df[df["clean_comment"] != ""]

print("Jumlah setelah cleaning:", len(df))

df.to_csv(
    "../data_clean/dataset_clean_youtube.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nSelesai")
print("File tersimpan:")
print("../data_clean/dataset_clean_youtube.csv")