from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Container Registry & Runtime (Docker Deploys)")
