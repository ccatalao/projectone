import os
import django

# Set up Django's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectone.settings')
django.setup()

from django.http import JsonResponse
from django.core.serializers import serialize
import json


from core.models import Post

read_file = open("savedata.json", "r")
data = json.load(read_file)

for item in data:
    post = Post(
                pk = item['pk'],
              	title = item['fields']['title'],
                text = item['fields']['text'],
                html_content = item['fields']['html_content'],
                img_link = item['fields']['img_link'],
                audio_file = item['fields']['audio_file'],
                image_file = item['fields']['img_link'],
                category        = item['fields']['category'],
                img_label       = item['fields']['img_label'],
                featured        = item['fields']['featured'],
                active          = item['fields']['active'],
                is_digital      = item['fields']['is_digital'],
                created_date = item['fields']['created_date'],
                published_date = item['fields']['published_date'],
                alert = item['fields']['alert'],
                tags = item['fields']['tags'],
                content = item['fields']['content'],
                name = item['fields']['name'],
                slug = item['fields']['slug'],
                pic = item['fields']['pic'],
                address = item['fields']['address'],
                lide = item['fields']['lide'],
                description = item['fields']['description'],
                notes = item['fields']['notes']
    	)
    print('-------------------- post ---------------------------')
    print(post.pk)
    print('-----------------------------------------------------')

    post.save()




