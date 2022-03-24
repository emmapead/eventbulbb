from django.test import TestCase
from .models import Event, Review
from accounts.models import UserProfile
from django.contrib.auth.models import User

# Create your tests here.
class ReviewTestCase(TestCase):

    def setUp(self):
        user = UserProfile(User)
        print(user)
        self.review1 = Review.objects.create(
                profile = user,
                event_id = 2,
                rating = 3,
                review = "It was good"
        )
        self.event1 =  Event.objects.create(
            title = "Welcome Event",
            description = "An event welcoming people",
            datetime = "2040-10-10T16:00:00.000Z",
            cost = 0,
        )

    def test_review_saved(self):
        self.assertGreater(self.review1.pk,0)

    
    def test_review_has_event(self):
        self.assertEqual("2", self.review.event.event_id)
