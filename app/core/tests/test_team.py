# Third party dependencies
import pytest

# Local imports
from ..models import Team
from ..utils.custom_utils import is_str_too_long


@pytest.mark.django_db
def test_team_create():
    NAME = 'Azul'
    team = Team.objects.create(name=NAME)
    assert team.name == NAME


@pytest.mark.django_db
def test_team_create_name_too_long():
    NAME_TOO_LONG = 'XXXXXXXXXXXXXXXXXXXXXXX'

    is_str_too_long(NAME_TOO_LONG, 22)
    NAME_TOO_LONG = 'XXX' if is_str_too_long else NAME_TOO_LONG

    team = Team.objects.create(name=NAME_TOO_LONG)
    assert team.name == NAME_TOO_LONG
