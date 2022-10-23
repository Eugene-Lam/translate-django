from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from googletrans import Translator

# Create your views here.
translate = Translator()


def home(request):
    dest = request.GET.get('dest')
    src = request.GET.get('src')
    text = request.GET.get('text')
    if dest and text and src:
        translated = translate.translate(text, dest=dest, src=src)
        print(translated.extra_data)
        return JsonResponse({'translated_text': translated.text, 'extra_data': translated.extra_data})
    return JsonResponse({'error': f'missing {dest} or {text} or {src}'})