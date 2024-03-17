from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Accessory
from .forms import FeedingForm

# finches = [
#   {'name': 'Goldie', 'breed': 'Goldfinch', 'description': 'exuberant bounding flight, musical calls, and flashy yellow and black plumage'},
#   {'name': 'Pipsqueak', 'breed': 'Grosbreaks', 'description': 'forages in mixed woodlands, coniferous forests, towns and suburbs'},
#   {'name': 'Flappy', 'breed': 'Star finch', 'description': 'measures in at around 4-4.7 inches in length and is native to Australia'},
#   {'name': 'Rocky', 'breed': 'Redpoll', 'description': 'very energetic small finches that travel in flocks, usually visit feeders during winter'},
#   {'name': 'Coco', 'breed': 'Cocos finch', 'description': 'endemic to Cocos Island, an approximately 360 miles (580 km) south of Costa Rica'},
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finch = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finch})

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  id_list = finch.accessory.all().values_list('id')
  acc_finch_doesnt_have = Accessory.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'accessories': acc_finch_doesnt_have })

# 

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'breed', 'description']

  def form_valid(self, form):
    return super().form_valid(form)

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finch'


def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)


class AccList(ListView):
  model = Accessory

class AccDetail(DetailView):
  model = Accessory

class AccCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'material']

class AccDelete(DeleteView):
  model = Accessory
  success_url = '/accessories'

def assoc_acc(request, finch_id, acc_id):
  Finch.objects.get(id=finch_id).accessory.add(acc_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_acc(request, finch_id, acc_id):
  Finch.objects.get(id=finch_id).accessory.remove(acc_id)
  return redirect('detail', finch_id=finch_id)