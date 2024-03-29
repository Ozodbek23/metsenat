from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl import Document

from apps.students.models import Student


@registry.register_document
class StudentDocument(Document):
    class Index:
        name = 'students'
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }


    class Django:
        model = Student
        fields = [
            'full_name',
            'phone_number',
            'type',
        ]