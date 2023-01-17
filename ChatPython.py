from itertools import permutations
import itertools
import random

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

players = ["Player " + str(i+1) for i in range(16)]

# split players into groups of 4
groups = [players[i:i+4] for i in range(0, len(players), 4)]

# create a list of all possible matches between players in each group
matches = [list(itertools.combinations(group, 4)) for group in groups]

# flatten the list of matches
matches = [match for group in matches for match in group]

# shuffle the matches for randomness
random.shuffle(matches)

# create a list to store the matches for each day
tournament = []
for i in range(4):
    day_matches = []
    for j in range(4):
        match = matches.pop()
        # check if players in the match have played before
        if match[0] not in [player for match in day_matches for player in match] and match[1] not in [player for match in day_matches for player in match] and match[2] not in [player for match in day_matches for player in match] and match[3] not in [player for match in day_matches for player in match]:
            day_matches.append(match)
    tournament.append(day_matches)

# print the matches for each day
for i in range(4):
    print("Day", i+1)
    for j in range(4):
        print(tournament[i][j])