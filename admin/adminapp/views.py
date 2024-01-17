# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login
@csrf_exempt
def Create_User(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', '')
        roll_number = data.get('roll_number', '')
        is_enabled=data.get('is_enabled','')
        new_user = User(name=name, roll_number=roll_number,is_enabled=is_enabled)
        new_user.save()

        return JsonResponse({'message': 'User created successfully!'})

    return JsonResponse({'message': 'Invalid request method.'})

def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all().values('id', 'name', 'roll_number', 'is_enabled')
        users_list = list(users)
        return JsonResponse({'users': users_list}, safe=False)

    return JsonResponse({'message': 'Invalid request method.'})

@csrf_exempt
def update_user_status(request, user_id):
    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            is_enabled = data.get('is_enabled', False)
            user = User.objects.get(id=user_id)
            user.is_enabled = is_enabled
            user.save()
            return JsonResponse({'message': 'User status updated successfully.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    return JsonResponse({'message': 'Invalid request method.'})

@csrf_exempt
def Update_User(request, user_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', '')
            roll_number = data.get('roll_number', '')
            is_enabled = data.get('is_enabled', False)
            # Fetch the user by user_id
            user = User.objects.get(id=user_id)

            # Update user fields
            user.name = name
            user.roll_number = roll_number
            user.is_enabled = is_enabled  # Update is_enabled field
            user.save()

            return JsonResponse({'message': 'User updated successfully!'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)

