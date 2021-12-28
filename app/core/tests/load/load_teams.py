# Third party dependencies
import pytest

# Local imports
from ...models import Team


@pytest.mark.django_db
def team_azul():
    NAME = 'Azul'
    team = Team.objects.create(name=NAME)
    return team


@pytest.mark.django_db
def team_rojo():
    NAME = 'Rojo'
    team = Team.objects.create(name=NAME)
    return team


@pytest.mark.django_db
def team_verde():
    NAME = 'Verde'
    team = Team.objects.create(name=NAME)
    return team


@pytest.mark.django_db
def team_negro():
    NAME = 'Negro'
    team = Team.objects.create(name=NAME)
    return team
