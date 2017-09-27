from django.db import models


class Visitation(models.Model):

    date_visited = models.DateTimeField(default=None, blank=True, null=True)
    page_name = models.CharField(max_length=50, default="", blank=True, null=True)

    def __str__(self):
        return "Visitation nr. " + str(self.id)