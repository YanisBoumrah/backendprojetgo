# games/models.py
from djongo import models

class Game(models.Model):
    player_black = models.ForeignKey('users.CustomUser', related_name='black_games', on_delete=models.CASCADE)
    player_white = models.ForeignKey('users.CustomUser', related_name='white_games', on_delete=models.CASCADE)
    sgf_data = models.TextField()  # Données SGF de la partie
    created_at = models.DateTimeField(auto_now_add=True)
    winner = models.CharField(max_length=10, null=True, blank=True)
