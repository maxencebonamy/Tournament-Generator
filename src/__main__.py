import json
from pprint import pprint
from tournament import Tournament
from utils import condition_input, style_print, style_input, Style
from tqdm import tqdm
from excel import Excel

NB_ITER = 10

def main():
    style_print("\n⚔️\tTOURNAMENT GENERATOR\t⚔️", Style.BOLD, Style.FAIL)

    with open("config.json", 'r') as config_file:
        config = json.load(config_file)
    
    teams = config["teams"]
    games = config["games"]

    if (len(teams) % 2 != 0):
        style_print("⚠ Number of teams must be even!", Style.WARNING, Style.BOLD)
        return
    if (len(games) * 2 < len(teams)):
        style_print("⚠ Not enough games for this number of teams!", Style.WARNING, Style.BOLD)
        return

    planning: Tournament
    while True:
        style_print("\nGeneration of the tournament...", Style.BOLD, Style.OKCYAN)
        redundances = len(games) + 1
        for i in tqdm(range(NB_ITER)):
            tournament = Tournament(teams=len(teams), games=len(games))
            tournament.plan()
            value = tournament.get_max_redundances()
            if value < redundances:
                redundances = value
                planning = tournament.planning()
        style_print(f"\nThe best tournament has {redundances} redundances.", Style.BOLD, Style.OKCYAN)
        if input("\nDo you want to regenerate the tournament (y/N)? ") != "y":
            break
    
    excel = Excel(planning=planning, teams=teams, games=games)
    # excel = Excel(planning=[[0]])
    excel.generate()

    path = input("\nPlease specify the name of the Excel file (leave empty for \"output\"): ")
    
    while True:
        try:
            excel.save(path)
        except:
            style_print("⚠ Please close the file!", Style.WARNING, Style.BOLD)
            input("\nPress any key to try again.")
            continue
        break

    excel.dispose()
    
    style_print("\n✅ The tournament has been generated in the Excel file!\n", Style.OKGREEN, Style.BOLD)


if __name__ == "__main__":
    main()
