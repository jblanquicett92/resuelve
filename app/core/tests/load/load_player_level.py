# Third party dependencies
import pytest

# Local imports
from ...models import Player_Level


@pytest.mark.django_db
def player_level_A():
    NAME = 'A'
    MINIMUM_GOAL_SCORED = 5

    player_level = Player_Level.objects.create(
        name=NAME,
        minimum_goal_scored=MINIMUM_GOAL_SCORED
    )
    return player_level


@pytest.mark.django_db
def player_level_B():
    NAME = 'B'
    MINIMUM_GOAL_SCORED = 10

    player_level = Player_Level.objects.create(
        name=NAME,
        minimum_goal_scored=MINIMUM_GOAL_SCORED
    )
    return player_level


@pytest.mark.django_db
def player_level_C():
    NAME = 'C'
    MINIMUM_GOAL_SCORED = 15

    player_level = Player_Level.objects.create(
        name=NAME,
        minimum_goal_scored=MINIMUM_GOAL_SCORED
    )
    return player_level


@pytest.mark.django_db
def player_level_Cuauh():
    NAME = 'Cuauh'
    MINIMUM_GOAL_SCORED = 20

    player_level = Player_Level.objects.create(
        name=NAME,
        minimum_goal_scored=MINIMUM_GOAL_SCORED
    )
    return player_level
