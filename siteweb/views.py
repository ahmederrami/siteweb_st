from django.http import JsonResponse
#from django.contrib.auth.decorators import login_required
import datetime
from .models import AppelOffre, Recrutement

# Create your views here.

def aolistview(request):

    aos = AppelOffre.objects.filter(date_archivage__gte=datetime.date.today()).filter(date_publication__lte=datetime.date.today())

    # Return in reverse chronologial order
    aos = aos.order_by("-date_limite_remise").all()
    #return JsonResponse({"error": "Invalid mailbox."}, status=400)
    return JsonResponse([ao.serialize() for ao in aos], safe=False)

#@login_required
def recrutementlistview(request):

    recrutements = Recrutement.objects.all()#filter(date_archivage__lt=datetime.date.today)

    # Return in reverse chronologial order
    recrutements = recrutements.order_by("-date_limite_candidature").all()
    return JsonResponse([recrutement.serialize() for recrutement in recrutements], safe=False)