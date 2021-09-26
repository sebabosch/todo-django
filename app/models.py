from django.db import models
from datetime import date

class Folder(models.Model):
    title = models.CharField(max_length=30,primary_key=True)
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length = 100)
    ok = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

    def toggle_task(self):
        self.ok = not self.ok
