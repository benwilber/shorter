from hashids import Hashids

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import redirect
from django.views.generic.base import View

from .models import TargetURL


class ShortenURL(View):

    def post(self, request):
        try:
            url = request.POST['url']
        except KeyError:
            return HttpResponseBadRequest("Missing required paramenter 'url'")

        try:
            target = TargetURL.objects.create(url=url)
        except ValidationError:
            return HttpResponseBadRequest("Malformed url")

        short = Hashids(salt=settings.HASHIDS_SALT, min_length=settings.HASHIDS_MIN_LENGTH).encode(target.pk)
        path = reverse('redirect-url', args=(short,))
        return JsonResponse({'short_url': request.build_absolute_uri(path)})


class RedirectURL(View):

    def get(self, request, short):
        try:
            pk = Hashids(salt=settings.HASHIDS_SALT, min_length=settings.HASHIDS_MIN_LENGTH).decode(short)[0]
            target = TargetURL.objects.get(pk=pk)
        except (IndexError, TargetURL.DoesNotExist):
            return HttpResponseNotFound("Short url not found")

        return redirect(target.url)
