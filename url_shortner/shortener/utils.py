from .models import UrlShortener
import random
import string

def generate_short_code():
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choice(chars) for _ in range(6))
        if not UrlShortener.objects.filter(short_code=code).exists():
            return code