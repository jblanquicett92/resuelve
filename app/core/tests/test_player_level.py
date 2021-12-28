# Third party dependencies
import pytest

# Local imports
from ..models import Player_Level
from ..utils.custom_utils import is_int, is_negative, is_str_too_long


@pytest.mark.django_db
def test_player_level_create():
    NAME = 'A'
    MINIMUM_GOAL_SCORED = 5

    player_level = Player_Level.objects.create(
        name=NAME,
        minimum_goal_scored=MINIMUM_GOAL_SCORED
    )
    assert player_level.name == NAME
    assert player_level.minimum_goal_scored == MINIMUM_GOAL_SCORED


@pytest.mark.django_db
def test_player_level_create_name_too_long():
    TOO_LONG_NAME = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
    MINIMUM_GOAL_SCORED = 5

    NAME = 'A' if is_str_too_long(TOO_LONG_NAME, 22) else TOO_LONG_NAME

    player_level = Player_Level.objects.create(
        name=NAME,
        minimum_goal_scored=MINIMUM_GOAL_SCORED
    )

    assert player_level.name == NAME


@pytest.mark.django_db
def test_player_level_minimum_goal_is_not_negative():
    NAME = 'A'
    MINIMUM_GOAL_SCORED = -1

    MINIMUM_GOAL_SCORED = MINIMUM_GOAL_SCORED if is_negative(MINIMUM_GOAL_SCORED) else 5
    player_level = Player_Level.objects.create(
        name=NAME,
        minimum_goal_scored=MINIMUM_GOAL_SCORED
    )

    assert player_level.minimum_goal_scored == MINIMUM_GOAL_SCORED


@pytest.mark.django_db
def test_player_level_minimum_goal_is_int():
    NAME = 'A'
    MINIMUM_GOAL_SCORED = []

    MINIMUM_GOAL_SCORED = MINIMUM_GOAL_SCORED if is_int(MINIMUM_GOAL_SCORED) else 5
    player_level = Player_Level.objects.create(
        name=NAME,
        minimum_goal_scored=MINIMUM_GOAL_SCORED
    )

    assert player_level.minimum_goal_scored == MINIMUM_GOAL_SCORED
