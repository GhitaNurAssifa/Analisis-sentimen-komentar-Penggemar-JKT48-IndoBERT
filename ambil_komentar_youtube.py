import pandas as pd
from youtube_comment_downloader import YoutubeCommentDownloader

videos = [
    "https://youtu.be/4ckrU8qqblY",
    "https://youtu.be/w-olCaECVRE",
    "https://youtu.be/zmS3Vfiqmgw",
    "https://youtu.be/G42O2vHDI4Y",
    "https://youtu.be/QtdsUJxiwNM",
    "https://youtu.be/n3EpgnAqlvE",
    "https://youtu.be/9iWB3ZuXOz8",
    "https://youtu.be/0-I9X8ZVckE",
    "https://youtu.be/C0NxffbkZHg",
    "https://youtu.be/pIxXbAif6C0",
    "https://youtu.be/88HhRpQIMcs",
    "https://youtu.be/JJHDaxE6-4g",
    "https://youtu.be/_R8561X2GIg"
]

downloader = YoutubeCommentDownloader()

hasil = []

for no, url in enumerate(videos, start=1):

    print(f"\n[{no}/{len(videos)}] {url}")

    try:

        comments = downloader.get_comments_from_url(url)

        jumlah = 0

        for c in comments:

            hasil.append([
                url,
                c.get("author", ""),
                c.get("text", "")
            ])

            jumlah += 1

            if jumlah % 100 == 0:
                print(f"  {jumlah} komentar")

        print(f"  Total: {jumlah}")

    except Exception as e:

        print("ERROR:", e)

df = pd.DataFrame(
    hasil,
    columns=[
        "video_url",
        "author",
        "comment"
    ]
)

df.to_csv(
    "../data_raw/komentar_youtube_jkt48.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nSELESAI")
print("Total komentar:", len(df))