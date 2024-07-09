from djongo import models

class Problem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    nodes = models.JSONField()  # Liste des nœuds occupés par des pierres
    winning_move = models.CharField(max_length=10)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
