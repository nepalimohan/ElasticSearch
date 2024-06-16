import time
from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch

class Command(BaseCommand):
    help = 'Waits until Elasticsearch is available'

    def add_arguments(self, parser):
        parser.add_argument('--es-url', type=str, default='http://elasticsearch:9200', help='Elasticsearch URL')

    def handle(self, *args, **kwargs):
        es_url = kwargs['es_url']
        es = Elasticsearch([es_url])
        print("Waiting for Elasticsearch at", es_url)
        while not es.ping():
            time.sleep(1)
        print("Elasticsearch is ready at", es_url)
