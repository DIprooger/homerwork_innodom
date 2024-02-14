from django.utils.translation import gettext as _
from django.http import JsonResponse


class MultiLanguageMixin:
    supported_languages = ['en', 'fr', 'es']  # Поддерживаемые языки

    def get_language_from_request(self, request):
        # Определение языка из параметра запроса
        language = request.GET.get('language')
        if language in self.supported_languages:
            return language
        else:
            return 'en'  # Возвращаем английский, если язык не поддерживается

    def get_content_translation(self, content, language):
        # Возвращает перевод контента на указанный язык
        translations = {
            'en': {'hello': 'Hello', 'world': 'World'},
            'fr': {'hello': 'Bonjour', 'world': 'Monde'},
            'es': {'hello': 'Hola', 'world': 'Mundo'}
        }
        translated_content = {key: translations[language].get(key, key) for key in content}
        return translated_content

    def render_to_response(self, context, **response_kwargs):
        language = self.get_language_from_request(self.request)
        translated_content = self.get_content_translation(context, language)
        return JsonResponse(translated_content, **response_kwargs)

from django.views.generic import View

class MyView(MultiLanguageMixin, View):
    def get(self, request, *args, **kwargs):
        content = {'hello': _('hello'), 'world': _('world')}
        return self.render_to_response(content)