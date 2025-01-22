# Users/views/recovery_view.py

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
import json
from django.contrib.auth.models import User

@method_decorator(csrf_exempt, name='dispatch')
class RecoveryPasswordView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get('email')

            if not email:
                return JsonResponse({"error": "Falta el correo electrónico"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "Correo de recuperación enviado"}, status=200)

            return JsonResponse({"error": "Correo no registrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": f"Error interno: {str(e)}"}, status=500)
