import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import datetime

engine = create_engine("sqlite:///bets.db")

def generate_data():
    teams = [
        "Arsenal", "Chelsea", "Liverpool", "City",
        "Barcelona", "Real Madrid", "PSG", "Bayern"
    ]

    nba_teams = [
        "Lakers", "Celtics", "Warriors", "Bulls"
    ]

    data = []

    # Futebol
    for i in range(0, len(teams), 2):
        home = teams[i]
        away = teams[i+1]

        home_prob = np.random.uniform(0.4, 0.7)
        draw_prob = np.random.uniform(0.1, 0.3)
        away_prob = 1 - home_prob - draw_prob

        odds_home = round(np.random.uniform(1.5, 3.0), 2)
        odds_draw = round(np.random.uniform(2.5, 4.0), 2)
        odds_away = round(np.random.uniform(2.0, 4.0), 2)

        data.append({
            "match": f"{home} vs {away}",
            "home_prob": home_prob,
            "draw_prob": draw_prob,
            "away_prob": away_prob,
            "odds_home": odds_home,
            "odds_draw": odds_draw,
            "odds_away": odds_away,
        })

    # NBA
    for i in range(0, len(nba_teams), 2):
        home = nba_teams[i]
        away = nba_teams[i+1]

        home_prob = np.random.uniform(0.4, 0.65)
        away_prob = 1 - home_prob

        odds_home = round(np.random.uniform(1.7, 2.2), 2)
        odds_away = round(np.random.uniform(1.7, 2.2), 2)

        data.append({
            "match": f"{home} vs {away}",
            "home_prob": home_prob,
            "draw_prob": 0.0,
            "away_prob": away_prob,
            "odds_home": odds_home,
            "odds_draw": 0.0,
            "odds_away": odds_away,
        })

    df = pd.DataFrame(data)

    df["value_home"] = df["home_prob"] - (1 / df["odds_home"])
    df["value_draw"] = df["draw_prob"] - (1 / df["odds_draw"].replace(0, np.nan))
    df["value_away"] = df["away_prob"] - (1 / df["odds_away"])

    df["date"] = datetime.date.today()

    return df

def run():
    df = generate_data()
    df.to_sql("bets", engine, if_exists="append", index=False)
    print("Dados salvos com sucesso!")

if __name__ == "__main__":
    run()