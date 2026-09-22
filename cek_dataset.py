import pandas as pd

df = pd.read_csv("../data_raw/komentar_youtube_jkt48.csv")

print(df.head(10))

print("\nJumlah data:", len(df))

print("\nKolom:")
print(df.columns.tolist())

print("\nData kosong:")
print(df.isnull().sum())