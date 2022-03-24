from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    CHOICES = (
            (1, 'Bad'),
            (2, 'okay'),
            (3,'good'),
            (4, 'great'),
            (5, 'excellent'),
            )
    
    profile = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE, blank=True,null=True, related_name="reviews")
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(choices=CHOICES, default=1)
    review = models.TextField()

    def __str__(self):
        return self.text