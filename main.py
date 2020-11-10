from function import * 

aggiungi_squadra('Milan')
file='data/squadre.csv'
df=pd.read_csv(file)
print(df)
aggiungi_squadra('Verona')
file='data/squadre.csv'
df=pd.read_csv(file)
print(df)
