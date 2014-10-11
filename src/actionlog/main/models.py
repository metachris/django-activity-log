from django.db import models

class Action(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=120)
    # color = models.CharField(max_length=6)  #rgb

    def __unicode__(self):
        return u"Action<%s>" % self.name

class LogEntry(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    date_entry = models.DateField()
    action = models.ForeignKey(Action)

    title = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __unicode__(self):
        return u"LogEntry<%s, %s, %s>" % (self.date_entry, self.action, self.title)

