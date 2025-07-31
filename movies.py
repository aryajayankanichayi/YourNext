import requests

API_KEY = 'jL3DwWoQ5hxSCsDjFZ8pQEqEGJBXE49bOdO2B9bj'

def fetch_genre_map():
    url = f'https://api.watchmode.com/v1/genres/?apiKey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {item['name'].lower(): item['id'] for item in data}
    return {}

def get_movies(genre_ids, language='en'):
    genre_ids = [str(i) for i in genre_ids]
    url = 'https://api.watchmode.com/v1/list-titles/'
    params = {
        'apiKey': API_KEY,
        'genres': ','.join(genre_ids),
        'language': language,
        'types': 'movie',
        'limit': 4
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []

    titles = response.json().get('titles', [])
    detailed_movies = []

    for title in titles:
        title_id = title.get('id')
        detail_url = f'https://api.watchmode.com/v1/title/{title_id}/details/'
        detail_params = {'apiKey': API_KEY}

        detail_response = requests.get(detail_url, params=detail_params)
        if detail_response.status_code == 200:
            detail_data = detail_response.json()
            movie_info = {
                'title': detail_data.get('title'),
                'plot': detail_data.get('plot_overview'),
                'image': detail_data.get('poster'),
                'year': detail_data.get('year')  
            }
            detailed_movies.append(movie_info)

    return detailed_movies


