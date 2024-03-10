# lets_quiz/quiz/app_config.py

from django.apps import AppConfig

class QuizAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz'

    def ready(self):
        import quiz.views