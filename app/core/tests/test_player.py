# Third party dependencies
import pytest

# Local imports
from ..models import Player
from ..utils.custom_utils import is_player_exists, is_team_exists, is_player_level_exists
from .load.load_teams import team_azul, team_negro, team_rojo
from .load.load_player_level import (
    player_level_A, player_level_B,
    player_level_C, player_level_Cuauh
)


@pytest.mark.django_db
def test_team_exists():
    team_azul_hardcode = team_azul()
    team_negro_hardcode = team_negro()
    team_rojo_hardcode = team_rojo()
    assert is_team_exists(team_azul_hardcode.name) == True
    assert is_team_exists(team_negro_hardcode.name) == True
    assert is_team_exists(team_rojo_hardcode.name) == True


@pytest.mark.django_db
def test_player_level_exists():
    player_level_A_hard_code = player_level_A()
    player_level_B_hard_code = player_level_B()
    player_level_C_hard_code = player_level_C()
    player_level_Cuauh_hard_code = player_level_Cuauh()
    assert is_player_level_exists(player_level_A_hard_code.name) == True
    assert is_player_level_exists(player_level_B_hard_code.name) == True
    assert is_player_level_exists(player_level_C_hard_code.name) == True
    assert is_player_level_exists(player_level_Cuauh_hard_code.name) == True


@pytest.mark.django_db
def test_player_create():

    player_level_A_hard_code = player_level_A()
    team_azul_hardcode = team_azul()

    FULLNAME = 'Cosme Fulanito'
    GOAL_SCORED = 7
    SALARY = 20000
    BONUS = 10000
    COMPLETE_SALARY = None

    player = Player.objects.create(
        full_name=FULLNAME,
        goal_scored=GOAL_SCORED,
        salary=SALARY,
        bonus=BONUS,
        complete_salary=COMPLETE_SALARY,
        player_level=player_level_A_hard_code,
        team=team_azul_hardcode
    )

    assert is_player_level_exists(player_level_A_hard_code.name) == True
    assert is_team_exists(team_azul_hardcode.name) == True
    assert is_player_exists(player.full_name) == True
