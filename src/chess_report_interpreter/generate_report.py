"""Alternate running file to create an HTML representation of the tournament data."""


import argparse
from jinja2 import Environment, FileSystemLoader
from tournament.data_analyzer import TournamentAnalyzer
from tournament.tms_parser import tmsParser
from tournament.tournament import ChessTournament

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tms", help="The name of the tms file to read", required=True)
    args = parser.parse_args()
    filename = args.tms

    lines = tmsParser.read_file(filename)
    players: dict = tmsParser.parse_lines(lines)
    tournament = ChessTournament(players)
    
    top_three = TournamentAnalyzer.get_top_three(tournament)

    total_rounds = max(len(p.results) for p in list(tournament.players.values()))

    all_reports = []
    for player in tournament.players:
        report = tournament.create_report(player)
        all_reports.append(report)

    env = Environment(loader = FileSystemLoader("./jinja_templates"))
    template = env.get_template("tournament_report.jinja")

    with open("./jinja_renders/tournament_report.html", "w") as f:
        print(template.render(
            players = tournament.players, 
            top_three = top_three, 
            total_rounds = total_rounds,
            all_reports = all_reports
            ), file = f)

if __name__ == "__main__":
    main()
