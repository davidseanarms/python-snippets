# Create 12 Teams
teams = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F", "Team G", "Team H", "Team I", "Team J", "Team K", "Team L"]

# Create League Table
league_table = {}
for team in teams:
    league_table[team] = 0

# Each team must play at least one game in each round
rounds = 6
for i in range(rounds):
    for team in teams:
        # Assign a random score from 0-3
        score = random.randint(0, 3)
        # Add score to the league table
        league_table[team] += score

# Output the league table
print("League Table")
for team in teams:
    print(team, league_table[team])
