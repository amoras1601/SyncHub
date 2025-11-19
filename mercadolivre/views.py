from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("MercadoLivre integration placeholder.")


def oauth_callback(request):
    return HttpResponse("OAuth callback placeholder.")


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        # Minimal placeholder: accept and acknowledge delivery
        return JsonResponse({'status': 'received'})
    return HttpResponse("Webhook endpoint - send POST requests.")
