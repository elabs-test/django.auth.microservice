from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
import json
from Users.services import create_user


@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            # Validar que todos los campos están presentes
            if not username or not email or not password:
                return JsonResponse({"error": "Faltan datos"}, status=400)


            # Crear usuario
            user = create_user(username, email, password)
            return JsonResponse({"message": "Usuario registrado con éxito", "user_id": user.id}, status=201)

        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error interno: {str(e)}"}, status=500)
