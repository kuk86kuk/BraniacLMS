from django.http import HttpResponse
from django.views.generic import View

class HelloWordView(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Hello world")

def empty_str(request):
    return HttpResponse('Тут пусто !!')

def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")

