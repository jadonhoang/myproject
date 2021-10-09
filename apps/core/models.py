from django.db import models


# Create your models here.

class DashboardPanel(models.Model):
    description = models.TextField(default="")
    github_username = models.CharField(max_length=127)
    repo_name = models.CharField(max_length=127)

    panel_type = models.CharField(max_length=127, choices = [
        ("piechart", "Pie-chart of languages used"),
        ("barchart", "Bar-chart of languages used")
    ])
