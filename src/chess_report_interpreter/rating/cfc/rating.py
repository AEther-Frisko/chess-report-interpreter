"""Performance calculation for CFC ratings."""

from typing import Tuple


def calculate_rating(
    old_rating: int,
    wins: int,
    losses: int,
    draws: int,
    opp_avg: float,
    is_provisional: bool = False,
) -> float:
    """
    Calculate the performance rating for a player based on their results.

    Args:
        old_rating (int): The player's old rating.
        wins (int): The number of games won.
        losses (int): The number of games lost.
        games (int): The total number of games played.
        opp_avg (float): The average rating of the opponents faced.
        is_provisional (bool, optional): Whether the rating is provisional. Defaults to False.

    Returns:
        float: The calculated performance rating.
    """
    rounds = wins + losses + draws
    if rounds == 0:
        raise ValueError("Total rounds played cannot be zero.")

    if is_provisional:
        return old_rating + 400 * (wins - losses) / rounds

    if opp_avg is None:
        raise ValueError(
            "Average opponent rating cannot be None for non-provisional ratings."
        )

    # Example calculation:
    # 1450 + 32(4 - (.77 + .42 + .80 + .51 + .33 + .01)) = 1450 + 32 (4 - 2.84 ) = 1487

    points, rounds_played = tournament_score(wins=wins, losses=losses, draws=draws)


def tournament_score(wins: int, losses: int, draws: int) -> Tuple[float, float]:
    """
    Calculate the tournament score based on wins, losses, and draws.

    Args:
        wins (int): The number of games won.
        losses (int): The number of games lost.
        draws (int): The number of games drawn.

    Returns:
        tuple: A tuple containing the total points and the number of rounds.
    """
    points = wins + (draws * 0.5)
    rounds = wins + losses + draws
    return points, rounds


def calc_exp_score(p1_rating: int, p2_rating: int) -> Tuple[float, float]:
    """
    Calculate the expected score for a player based on their rating differential.

    The formula for this is based on the difference of the pleyer's ratings, as:
    Rating Difference, Score for Higher rated player, score for lower rated player
    0-3, 0.50, 0.50
    4-10, 0.51, 0.49
    11-17, 0.52, 0.48
    18-25, 0.53, 0.47
    ...
    735+, 1.00, 0.00

    Args:
        p1_rating (int): The rating of player 1.
        p2_rating (int): The rating of player 2.

    Returns:
        tuple: A tuple containing the expected score for player 1 and player 2 respectively.
    """
    diff = abs(p1_rating - p2_rating)
    # For rating differences 0-3, expected score is 0.5 for both.
    if diff <= 3:
        higher, lower = 0.50, 0.50
    else:
        capped_diff = min(diff, 735)
        delta = capped_diff * 0.0068
        higher = min(max(0.5 + delta, 0.0), 1.0)
        lower = 1.0 - higher

    if p1_rating >= p2_rating:
        return higher, lower
    else:
        return lower, higher
