import pandas as pd
import zipfile
with zipfile.ZipFile("archive.zip") as z:
    with z.open("netflix_titles.csv") as f:
        df=pd.read_csv(f)
print(df.head())
print(df.info())

df['date_added']=(
    pd.to_datetime(df['date_added'],errors='coerce'))
df['country']=df['country'].fillna("unknown")
df['director']=df['director'].fillna("unknown")
df=df.dropna(subset=['cast'])

df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

movies_df = df[df['type'] == 'Movie']
tv_df = df[df['type'] == 'TV Show']

df.to_csv("Cleaned_Netflix_title.csv")
