from pprint import pprint
import random
from typing import List


class Tournament:

    def __init__(self, teams: int, games: int):
        assert teams % 2 == 0
        assert games * 2 >= teams

        self.__teams = teams
        self.__games = games

        self.__planning = [[None for _ in range(self.__games)] for _ in range(self.__teams)]

    def plan(self) -> None:
        while not self.__is_complete():
            
            self.__planning = [[None for _ in range(self.__games)] for _ in range(self.__teams)]
            
            for game in range(self.__games):
                slots = list(range(self.__games))
                random.shuffle(slots)
                for slot in slots:
                    possible_teams = []
                    for team in range(self.__teams):
                        if self.__planning[team][slot] is None and not self.__has_already_play(team, game):
                            possible_teams.append(team)
                    if len(possible_teams) < 2:
                        continue
                    random.shuffle(possible_teams)
                    for team in possible_teams[:2]:
                        self.__planning[team][slot] = game

    def planning(self) -> List[List[int]]:
        assert self.__is_complete()

        return self.__planning
    
    def __is_complete(self) -> bool:
        return all(slot is not None for team in self.__planning for slot in team)
    
    def __has_already_play(self, team: int, game: int) -> bool:
        return any(slot == game for slot in self.__planning[team])
    
    def get_max_redundances(self) -> float:
        redundances: int = 0

        for team_a in range(self.__teams):
            for team_b in range(self.__teams):
                if team_a == team_b:
                    continue
                count: int = 0
                for slot in range(self.__games):
                    if self.__planning[team_a][slot] == self.__planning[team_b][slot]:
                        count += 1
                if count >= redundances:
                    redundances = count
        
        return redundances