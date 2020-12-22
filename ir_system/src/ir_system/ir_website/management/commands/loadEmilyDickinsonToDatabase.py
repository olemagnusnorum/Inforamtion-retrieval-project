from django.core.management.base import BaseCommand
from ...searchEngine import retriever
from ...models import EmilyDickinson



class Command(BaseCommand):
    help = 'loads works of emily dickinson in to database'

    def handle(self, *args, **kwargs):
        docs = retriever.poemProcessingDickinson()
        for index in range(len(docs)):
            doc = docs[index]
            e = EmilyDickinson.objects.create(id=index, document=doc)
            e.save()
        self.stdout.write("loaded")