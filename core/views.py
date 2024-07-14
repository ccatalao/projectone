from django.http import HttpResponse
from django.template import loader
from .models import MyPost


def core(request):
    myposts = MyPost.objects.all().values()
    template = loader.get_template('all_posts.html')
    context = {
    'myposts': myposts,
    }
    return HttpResponse(template.render(context, request))

