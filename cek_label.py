import pandas as pd

df = pd.read_csv("../data_label/sample_3000_label_awal.csv")

print(df.head(20))

print("\nDistribusi:")
print(df["label"].value_counts())