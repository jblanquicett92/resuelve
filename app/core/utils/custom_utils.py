from ..models import Team, Player_Level, Player


def is_str_too_long(string: str, size_limit: int):
    """Returns true in case string is greater than or equal of size_limit

        -------
        Boolean"""
    return len(string) >= size_limit


def is_negative(value: int):
    """Returns true in case value is less than zero

        -------
        Boolean"""
    return value < 0


def is_str(value: any):
    """Returns true in case value type is str

        -------
        Boolean"""
    return type(value) == str


def is_float(value: any):
    """Returns true in case value type is float

        -------
        Boolean"""
    return type(value) == float


def is_int(value: any):
    """Returns true in case value type is int

        -------
        Boolean"""
    return type(value) == int


def is_team_exists(name: str):
    """Returns true in case team exists

        -------
        Boolean"""
    try:
        Team.objects.get(name=name)
    except Team.DoesNotExist:
        return False
    return True


def is_player_level_exists(name: str):
    """Returns true in case player level exists

        -------
        Boolean"""
    try:
        Player_Level.objects.get(name=name)
    except Player_Level.DoesNotExist:
        return False
    return True


def is_player_exists(full_name: str):
    """Returns true in case player exists

        -------
        Boolean"""
    try:
        Player.objects.get(full_name=full_name)
    except Player.DoesNotExist:
        return False
    return True
