from itertools import permutations
import itertools

def optimize_groups(players):
    groups_of_four = players // 4
    remaining_players = players % 4
    groups_of_three = remaining_players // 3
    remaining_players = remaining_players % 3
    
    if remaining_players > 0:
        groups_of_four -= 1
        remaining_players += 4
        groups_of_three = remaining_players // 3
        remaining_players = remaining_players % 3
    
   
    return groups_of_four, groups_of_three

def schedule_golf_games(num_players, num_days):
    # Create a list of players
    players = list(range(1, num_players + 1))

    # Create a list to store the schedule
    schedule = []

    # Iterate through each day
    for day in range(num_days):
        # Shuffle the list of players to randomly assign teams
        import random
        random.shuffle(players)

        # Split the players into teams of 4 and 3
        team_4 = players[:4]
        team_3 = players[4:]

        # Add the teams to the schedule
        schedule.append((team_4, team_3))

    return schedule

# Example usage:
print(schedule_golf_games(10, 5))