# users/views/login_view.py

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
import json
from users.services import authenticate_user

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            # Validar datos requeridos
            if not email or not password:
                return JsonResponse({"error": "Faltan datos: email y contraseña son requeridos"}, status=400)

            # Autenticar usuario
            user = authenticate_user(email, password)
            if user:
                return JsonResponse({"message": "Inicio de sesión exitoso"}, status=200)

            return JsonResponse({"error": "Usuario no existe o credenciales inválidas"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error interno: {str(e)}"}, status=500)
