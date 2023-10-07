<p align="center">
	<img src="https://github.com/maxencebonamy/maxencebonamy/blob/main/assets/Tournament_Generator.png" width="100%" alt="Tournament Generator">
</p>


<br>

<p align="center">
	<img src="https://github.com/maxencebonamy/maxencebonamy/blob/main/assets/1_Description.png" width="100%" alt="Description">
</p>

This software allows you to generate a multiplayer and multigame tournament plannning with a customizable number of teams and games, and with 1V1 confrontations.

To do this, simply enter the team and game names in the `config.json` file, then run the program, and an Excel file will be generated with the entire tournament schedule.

<br>

<p align="center">
	<img src="https://github.com/maxencebonamy/maxencebonamy/blob/main/assets/2_Get_Started.png" width="100%" alt="Get Started">
</p>

### Run the program:

> [!NOTE]
> *Prerequisites:*
> - [x] *Git must be installed on your computer. If not, <a href="https://git-scm.com/downloads" target="_blank">click here.</a>*
> - [x] *Python version 3.9 or greater must be installed on your computer, if not, <a href="https://www.python.org/downloads/" target="_blank">click here.</a>*
<br>

1. **Clone** the repository on your computer. To do this, open a terminal in the folder of your choice and run the following command:
```
git clone https://github.com/maxencebonamyTournament-Generator
```

2. **Navigate** inside the folder you've just cloned with the following command:
```
cd Tournament-Generator
```

3. **Install dependencies** by running this command:
```
python -m pip install -r requirements.txt
```

4. **Start the program** with the following command:
```
python src
```

<br>

<p align="center">
	<img src="https://github.com/maxencebonamy/maxencebonamy/blob/main/assets/3_Features.png" width="100%" alt="Features">
</p>

### Input format:
To configure the tournament, simply edit the `config.json` file. In this file, there's a list containing the team names, as well as a list containing the game names. This automatically determines the number of teams and games.

### Output format:
The program ends by generating an Excel file containing 3 pages, each illustrating the overall tournament schedule, but from different points of view.
- **Global planning:** All games by team and time slot.
- **Teams planning:** All team games with the team they are playing for each game, according to time slot.
- **Games planning:** All teams playing against each other for each game, according to time slot.

### Constraints:
- The number of teams must be even, as this is a 1V1 tournament.
- The number of games multiplied by two must be greater than or equal to the number of teams, otherwise the tournament cannot be generated.
