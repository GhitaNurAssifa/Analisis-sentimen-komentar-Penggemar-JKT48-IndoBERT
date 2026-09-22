import pandas as pd

df = pd.read_csv("../data_label/sample_3000_label_awal.csv")

netral = df[df["label"] == "netral"]

print("Jumlah netral:", len(netral))

print("\n=== 100 KOMENTAR NETRAL ACAK ===\n")

for i, row in enumerate(
    netral.sample(
        n=100,
        random_state=42
    )["clean_comment"],
    start=1
):
    print(f"{i}. {row}")