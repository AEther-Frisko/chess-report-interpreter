"""Alternate running file to create an HTML representation of the tournament data."""


import argparse
from jinja2 import Environment, FileSystemLoader
from tournament.data_analyzer import TournamentAnalyzer
from tournament.tms_parser import tmsParser
from tournament.tournament import ChessTournament
from tournament.ctr_parser import ctrParser

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tms", help="The name of the tms file to read", required=True)
    parser.add_argument("--ctr", help="The name of the ctr file to read", required=True)
    parser.add_argument("--rtg", help="Optional rating threshold for \"Top Player under X\"")
    args = parser.parse_args()
    tms_file = args.tms
    ctr_file = args.ctr
    max_rating = args.rtg

    lines = tmsParser.read_file(tms_file)
    players: dict = tmsParser.parse_lines(lines)
    ctr_line = ctrParser.read_file(ctr_file)[0]
    data = ctrParser.parse_tournament_data(ctr_line)
    tournament = ChessTournament(players, data)
    
    top_three = TournamentAnalyzer.get_top_three(tournament)

    highest = {
        "Score": 0.0,
        "Player": None,
        "Max Rating": None
    }
    if max_rating is not None:
        highest.update(TournamentAnalyzer.get_top_under_rating(tournament, max_rating))

    all_reports = []
    for player in tournament.players:
        report = tournament.create_report(player)
        all_reports.append(report)

    result_lookup = {}
    for seed, player in tournament.players.items():
        result_lookup[seed] = {}
        for result in player.results:
            result_lookup[seed][result.vs_seed] = result.result

    env = Environment(loader = FileSystemLoader("./jinja_templates"))
    template = env.get_template("tournament_report.jinja")

    with open("./jinja_renders/tournament_report.html", "w") as f:
        print(template.render(
            info = tournament.info,
            players = tournament.players,
            result_lookup = result_lookup, 
            top_three = top_three,
            highest = highest,
            all_reports = all_reports
            ), file = f)

if __name__ == "__main__":
    main()
