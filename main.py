
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import datetime

# cria conexão com banco (arquivo será criado automaticamente)
engine = create_engine("sqlite:///bets.db")

def generate_data():
data = [
{
"match": "Arsenal vs Chelsea",
"home_prob": 0.62,
"draw_prob": 0.20,
"away_prob": 0.18,
"odds_home": 2.10,
"odds_draw": 3.40,
"odds_away": 3.20,
},
{
"match": "Lakers vs Celtics",
"home_prob": 0.58,
"draw_prob": 0.00,
"away_prob": 0.42,
"odds_home": 1.95,
"odds_draw": 0.00,
"odds_away": 2.10,
}
]

df = pd.DataFrame(data)

# cálculo de value bet
df["value_home"] = df["home_prob"] - (1 / df["odds_home"])
df["value_draw"] = df["draw_prob"] - (1 / df["odds_draw"].replace(0, np.nan))
df["value_away"] = df["away_prob"] - (1 / df["odds_away"])

df["date"] = datetime.date.today()

return df

def run():
df = generate_data()

# salva no banco
df.to_sql("bets", engine, if_exists="append", index=False)

print("Dados salvos com sucesso!")

if __name__ == "__main__":
run()
