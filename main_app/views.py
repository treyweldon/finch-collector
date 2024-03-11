from django.shortcuts import render

finches = [
  {'name': 'Goldie', 'breed': 'Goldfinch', 'description': 'exuberant bounding flight, musical calls, and flashy yellow and black plumage'},
  {'name': 'Pipsqueak', 'breed': 'Grosbreaks', 'description': 'forages in mixed woodlands, coniferous forests, towns and suburbs'},
  {'name': 'Flappy', 'breed': 'Star finch', 'description': 'measures in at around 4-4.7 inches in length and is native to Australia'},
  {'name': 'Rocky', 'breed': 'Redpoll', 'description': 'very energetic small finches that travel in flocks, usually visit feeders during winter'},
  {'name': 'Coco', 'breed': 'Cocos finch', 'description': 'endemic to Cocos Island, an approximately 360 miles (580 km) south of Costa Rica'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'finches/index.html', {'finches': finches})