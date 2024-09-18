from django.db import models

class Idea(models.Model):
    idea_id = models.IntegerField(primary_key=True)
    submitted_date_time = models.DateTimeField()
    idea_status = models.CharField(max_length=100)
    creator_id = models.CharField(max_length=100)
    creator_department = models.CharField(max_length=100)
    times_shared = models.IntegerField()
    votes = models.IntegerField()
    comments = models.IntegerField()
    views = models.IntegerField()
    keywords = models.TextField(blank=True)

    def __str__(self):
        return f"Idea {self.idea_id} - {self.idea_status}"
