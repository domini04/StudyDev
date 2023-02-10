from django.shortcuts import render
import random

fortuneList = ["You will make passionate love to your partner", "Today you will have a great meal", 
"Fortunes are really dumb", "Today will be a day well spent",
   "All will go well with your new project.",
   "If you continually give, you will continually have.",
   "Self-knowledge is a life long process.",
   "You are busy, but you are happy.",
   "Your abilities are unparalleled.",
   "Those who care will make the effort.",
   "Now is the time to try something new.",
   "Miles are covered one step at a time.",
   "Don’t just think, act!"]


# Create your views here.
def fortune(request):
  context = {'fortune': random.choice(fortuneList)}
  return render(request, 'randomfortune/fortune.html', context) 
  #this will send 'fortune' context variable to fortune.html upon receiving request


