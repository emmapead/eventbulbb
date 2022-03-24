from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Event, Review
from accounts.models import UserProfile

def get_user_profile(request):
    if request.user.is_authenticated:
        [profile, created] = UserProfile.objects.get_or_create(user=request.user)
        return profile

@login_required
def add_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.add(event)
    return redirect("events_list")


@login_required
def remove_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.remove(event)
    return redirect("events_list")


def details(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/details.html', {'event': event})


def list(request):
    today = datetime.today()

    filter_map = {
        'title': 'title__icontains',
        'is_free': 'cost__exact'
    }

    filters = {}
    for key, value in request.GET.items():
        filter_key = filter_map[key]
        filters[filter_key] = value
 
    events = Event.objects.filter(
        datetime__gte=today).filter(**filters).order_by('datetime')
    return render(request, 'events/list.html', {'events': events})

def dashboard(request):

    today = datetime.today()

    #Get user profile
    user_profile = get_user_profile(request)

    events = user_profile.attending.filter(datetime__gte=today).order_by('datetime')
    past_events = user_profile.attending.filter(datetime__lt=today).order_by('datetime')
   

    return render(request, 'events/dashboard.html', {'events':events, 'past_events': past_events})

def new_review(request,id):
    event = get_object_or_404(Event, id=id)
    if request.method ==  "POST":
        event = get_object_or_404(Event, id=id)
        [profile,user] = UserProfile.objects.get_or_create(user=request.user)
        rating = request.POST["rating"]
        review = request.POST["review"]
        new_review = Review(
            profile = profile,
            event_id = event,
            rating = rating,
            review = review,
        )
        new_review.save()
        return redirect("/events/dashboard")

    return render(request, 'events/new_review.html', {'event': event})

