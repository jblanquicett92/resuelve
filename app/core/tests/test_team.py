import pytest
from ..models import Team


@pytest.mark.django_db
def test_team_create():
    NAME = 'Azul'
    team = Team.objects.create(name=NAME)
    assert team.name == NAME
