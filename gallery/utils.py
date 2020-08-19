import json
import os

import requests

API_KEY = os.environ['API_KEY']


def api_get_token():
    """Authorize on external API and return access token."""
    url = 'http://interview.agileengine.com/auth'
    payload = {
        'apiKey': API_KEY
    }

    response = requests.post(url, json=payload)
    token = json.loads(response.text)['token']

    return token


def api_get_images_pages_count():
    """Call external API ang return total pages count value."""
    url = 'http://interview.agileengine.com/images'
    header = {
        'Authorization': 'Bearer {}'.format(api_get_token())
    }

    response = requests.get(url, headers=header)
    pages_count = int(json.loads(response.text)['pageCount'])

    return pages_count


def api_get_images_id():
    """Call external API and return list with pictures id."""
    data = []
    pages = api_get_images_pages_count()

    for page in range(pages):
        url = 'http://interview.agileengine.com/images?page={}'.format(page)
        header = {
            'Authorization': 'Bearer {}'.format(api_get_token())
        }
        response = requests.get(url, headers=header)
        pictures = json.loads(response.text)['pictures']

        for picture in pictures:
            data.append(picture['id'])

    return data


def build_images_urls():
    """Build and return list of urls from pictures id."""
    data = []

    for picture_id in api_get_images_id():
        picture_url = 'http://interview.agileengine.com/images/{}'.format(picture_id)
        data.append(picture_url)

    return data

def write_image_data():
    """Write image data inside"""