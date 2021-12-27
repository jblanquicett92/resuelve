from django.db import models

class Team(models.Model):
    id_team = models.AutoField(primary_key=True)
    name = models.CharField(max_length=22)        

    def __str__(self):
        return super().__str__()

class Player_Level(models.Model):
    id_player_level = models.AutoField(primary_key=True)
    name = models.CharField(max_length=22)
    minimum_goal_scored = models.IntegerField()      

    def __str__(self):
        return super().__str__()

class Player(models.Model):
    id_player = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=22)
    goal_scored = models.IntegerField()
    salary = models.FloatField()
    bonus = models.FloatField()
    complete_salary = models.FloatField()
    player_level = models.ForeignKey(Player_Level, on_delete=models.SET_NULL, null=True, related_name='player_level')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team')
    
    def __str__(self):
        return super().__str__()