import csv

def find_nfl_winner(year):
    return find_winner('champions/nfl.csv', year)

def find_nba_winner(year):
    return find_winner('champions/nba.csv', year)

def find_mlb_winner(year):
    return find_winner('champions/mlb.csv', year)

def find_ncaaf_winner(year):
    return find_winner('champions/ncaaf.csv', year)

def find_nhl_winner(year):
    return find_winner('champions/nhl.csv', year)

def find_mls_winner(year):
    return find_winner('champions/mls.csv', year)

def find_premier_eng_winner(year):
    return find_winner('champions/premier-eng.csv', year)

def find_uefa_champs_winner(year):
    return find_winner('champions/uefa-champions.csv', year)

def find_bundesliga_winner(year):
    return find_winner('champions/bundesliga.csv', year)

def find_winner(file_path, year):
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                if (row['year'] == year):
                    return row['winner']
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        print("Error reading file:", e)
    return "No winner found for the specified year"
