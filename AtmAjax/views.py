from django.shortcuts import render
from django.http import JsonResponse
from .models import User, UserInfo
from FaceDetector import datasetCreator
from FaceDetector import faceRecogniser

def GetCardInfo(request):
    card_n = request.GET.get('card_n')
    nextStage = 'TakePassword'

    # userInfo = UserInfo.objects.get(card_number = card_n)
    try:
        userInfo = UserInfo.objects.get(card_number = card_n)
        user = userInfo.card_number
        password = userInfo.user.password
        otp = 1111
    except:
        user = None
        password = None
        otp = None
        nextStage = 'Register'

    user = {
        'user': user,
        'pass': password,
        'otp': otp,
        'stage': nextStage
    }
    return JsonResponse(user)



def RegisterUser(request):
    nextStage = 'InsertCard'
    card_n = request.GET.get('card_n')
    password = request.GET.get('pass')

    # Register Image
    datasetCreator.RegisterImage(card_n)

    user_obj = User(username=card_n, first_name=card_n, email='', password=password)
    user_obj.save()
    UserInfo.objects.create(user = user_obj, card_number = card_n, current_balance = 500, mobile = '')
    
    user = {
        'stage': nextStage
    }
    return JsonResponse(user)



def LoginUser(request):
    card_n = request.GET.get('card_n')
    password = request.GET.get('pass')
    otp = request.GET.get('otp')

    nextStage = 'Home'

    # userInfo = UserInfo.objects.get(card_number = card_n)
    try:
        userInfo = UserInfo.objects.get(card_number = card_n)
        if card_n == userInfo.card_number and password == userInfo.user.password and otp == '1111':
            
            # Face Recognition for Image
            isFaceOk = faceRecogniser.RecogniseImage(card_n)
            if isFaceOk:
                user = userInfo.card_number
            else:
                raise Exception("Face Mismathched.")

        else:
            raise Exception("Password Mismathched.")
        
    except Exception as e:
        print(e)
        user = None
        password = None
        nextStage = 'InsertCard'

    user = {
        'user': user,
        'stage': nextStage
    }
    return JsonResponse(user)




