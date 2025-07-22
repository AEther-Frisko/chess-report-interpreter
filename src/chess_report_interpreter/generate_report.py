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
    args = parser.parse_args()
    tms_file = args.tms
    ctr_file = args.ctr

    lines = tmsParser.read_file(tms_file)
    players: dict = tmsParser.parse_lines(lines)
    ctr_line = ctrParser.read_file(ctr_file)[0]
    data = ctrParser.parse_tournament_data(ctr_line)
    tournament = ChessTournament(players, data)
    
    top_three = TournamentAnalyzer.get_top_three(tournament)

    total_rounds = max(len(p.results) for p in list(tournament.players.values()))

    all_reports = []
    for player in tournament.players:
        report = tournament.create_report(player)
        all_reports.append(report)

    env = Environment(loader = FileSystemLoader("./jinja_templates"))
    template = env.get_template("tournament_report.jinja")

    # definitely want to condense this if possible?
    # also need to replace some of these with proper outputs instead of just ids.
    with open("./jinja_renders/tournament_report.html", "w") as f:
        print(template.render(
            event = tournament.event,
            end_date = tournament.end_date,
            type = tournament.type,
            pairing = tournament.pairing,
            province = tournament.province,
            organizer = tournament.org_id,
            arbiter = tournament.arb_id,
            players = tournament.players, 
            top_three = top_three, 
            total_rounds = total_rounds,
            all_reports = all_reports
            ), file = f)

if __name__ == "__main__":
    main()
