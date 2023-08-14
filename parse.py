from yandex_music import Client
import pickle
from tqdm import tqdm
import os


def fetch_info(client, track):
    full_info = client.tracks(track['id'])
    title = full_info[0]['title']
    return title, ', '.join([artist['name'] for artist in full_info[0]['artists']])


def get_yandex(token):
    client = Client(token)
    data = []
    for track in tqdm(client.users_likes_tracks()):
        temp = fetch_info(client, track)
        data.append(str(temp[1] + ' - ' + temp[0]))
    with open('data', 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    token = input('Your Yandex OAuth token (LEAVE BLANK IF TOKEN IS AVAILABLE): ')
    i = 0 if input('Load all tracks again? [Y/n]') == 'y'.lower() else pickle.load(open('yandex_token', 'rb'))[1]
    if not token:
        token = pickle.load(open('yandex_token', 'rb'))[0]
    else:
        pickle.dump([token, i], open('yandex_token', 'wb'))
    
    get_yandex(token)
