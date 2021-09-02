from django.conf import settings
from random import choice

from string import ascii_letters,digits

SIZE = getattr(settings,"Maximum Url",7)

available_chars = ascii_letters+digits

def create_random_code(chars = available_chars):
    return "".join([choice(chars) for _ in range(SIZE)])



def shortened_url(model_instance):
    random_code = create_random_code()

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url = random_code).exists():
        return create_random_code(model_instance)

    return random_code