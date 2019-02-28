from django.utils import timezone
from parents_zone.models import ParentsInformation
from events.models import Event
from blog.models import Category, Post
from key_information.models import KeyInformation


def ctx_dict(request):
    # context for create dynamically page for parents_zone
    parents = ParentsInformation.objects.values('title', 'id')
    # context for create dynamically page for key_informations
    informations = KeyInformation.objects.values('title', 'id')
    # context for sidebars
    # query for upcoming events
    now = timezone.now()
    upcoming = Event.objects.filter(time__gte=now).order_by('time')[:3]
    # Query for Tags sidebar
    categories = Category.objects.all()
    popular = Post.objects.order_by('hit_count')[:3]

    ctx = {'parents': parents, 'upcoming': upcoming,
           'categories': categories, 'popular': popular,
           'informations': informations}
    return ctx
