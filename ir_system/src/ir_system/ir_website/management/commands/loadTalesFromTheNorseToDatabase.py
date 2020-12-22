from django.core.management.base import BaseCommand
from ...searchEngine import retriever
from ...models import TalesFromTheNorse


class Command(BaseCommand):
    help = 'loads works of tales from the Norse in to database'

    def handle(self, *args, **kwargs):
        docs = retriever.processingTalesFromTheNorse()
        for index in range(len(docs)):
            doc = docs[index]
            e = TalesFromTheNorse.objects.create(id=index, document=doc)
            e.save()
        self.stdout.write("loaded")