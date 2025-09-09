# NFL Import
from espn_api.football import League
import league_info

# private league with cookies (Beemer World)
league = League(league_id=league_info.league_id,
                year=2025,
                espn_s2=league_info.espn_s2,
                swid=league_info.swid,
                debug=False)
 
teams = league.teams
matchups = league.scoreboard(1)
scores = league.box_scores(1)
 
# print matchup outcomes for the week
print("%24s %s" % (" ", "Matchups for the Week:\n"))
for score in scores:
    print("%25s (%6.2f vs. %6.2f) %-25s" % (score.home_team.team_name,
                                            score.home_score, score.away_score,
                                            score.away_team.team_name))

# biggest blowout/closest match
diffs = [(m, abs(m.home_score - m.away_score)) for m in matchups]
closest = min(diffs, key=lambda x: x[1])
print("\nClosest match: %s vs %s by %.2f points" % (closest[0].home_team.team_name,
                                                    closest[0].away_team.team_name,
                                                    closest[1]) )
blowout = max(diffs, key=lambda x: x[1])
print("Biggest blowout: %s vs %s by %.2f points" % (blowout[0].home_team.team_name,
                                                    blowout[0].away_team.team_name,
                                                    blowout[1]) )

# get lowest and highest scorer
print(f"\nBest Team this Week: {league.top_scored_week()}")
print(f"Worst Team this Week: {league.least_scored_week()}")
