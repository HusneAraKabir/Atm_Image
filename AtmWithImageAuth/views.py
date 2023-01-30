from django.shortcuts import render
from django.http import JsonResponse

def Bismillah(request):
    print('----- Bismi ALLAH -----')
    # return render(request, 'mainmachine.html')
    # return render(request, 'mainmachine_new.html')
    return render(request, 'homePage.html')





