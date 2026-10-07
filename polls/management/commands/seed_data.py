from django.core.management.base import BaseCommand
from django.utils import timezone
from polls.models import Question, Choice

class Command(BaseCommand):
    help = 'Add sample polling questions and choices.'

    def handle(self, *args, **options):
        Question.objects.all().delete()
        samples = [
            ('Which programming language do you prefer for Data Science?', ['Python', 'R', 'Java', 'C++'], [18, 7, 5, 3]),
            ('Which learning method helps you most?', ['Practical Projects', 'Video Lectures', 'Books', 'Group Study'], [20, 12, 6, 9]),
            ('Which area interests you most?', ['Machine Learning', 'Data Analytics', 'Web Development', 'Cloud Computing'], [15, 11, 8, 10]),
        ]
        for question_text, options, votes in samples:
            q = Question.objects.create(question_text=question_text, pub_date=timezone.now())
            for text, count in zip(options, votes):
                Choice.objects.create(question=q, choice_text=text, votes=count)
        self.stdout.write(self.style.SUCCESS('Sample poll data added successfully.'))
