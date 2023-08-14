from ytmusicapi import YTMusic
import pickle
from Levenshtein import distance
from tqdm import tqdm
from colorama import Fore, Style
import os
from parse import main_yandex

def shipIt(ytmusic, data, i):
    errs = {'maybe_broken': [], 'broken': []}
    for track in tqdm(data[i:]):
        k = 0
        res = ytmusic.search(track)

        if 'prod' in track or 'ft' in track or 'feat' in track:
            track = track[:track.find('(')].strip()
        if res[k]['resultType'] == 'album':
            res = ytmusic.search(track + 'track')
        if res[k]['resultType'] == 'artist':
            res = ytmusic.search(track + 'video')
            while res[k]['resultType'] not in ['song', 'video']:
                k += 1
                if distance(track.lower().split(' - ')[1], res[k]['title']) <= 3 and distance(track.lower().split(' - ')[0], artist.lower()) <= 3:
                    errs['maybe_broken'].append(track)
                    ytmusic.rate_song(res[k]['videoId'], 'LIKE')
                    break
                if k >= 5:
                    errs['broken'].append(track)
                    break
        if k > 0:
            continue
        artist = res[k]['artists'][0]['name']
        ytname = (artist + ' - ' + res[k]['title']).lower()
        if res[k]['resultType'] not in ['video', 'song']:
            print('\n' + Fore.RED + track + ' is not added')
            print(Style.RESET_ALL)
            errs['broken'].append(track)
        else:
            ytmusic.rate_song(res[k]['videoId'], 'LIKE')

    return errs


if __name__ == '__main__':
    if 'yandex_token' not in os.listdir() :
        open('yandex_token', 'wb') 
    if 'data' not in os.listdir():
        open('data', 'wb')
    if os.stat('data').st_size == 0:
        main_yandex()
    token = pickle.load(open('yandex_token', 'rb'))[0]
    errs = shipIt(YTMusic('oauth.json'), pickle.load(open('data', 'rb')), pickle.load(open('yandex_token', 'rb'))[1])
    if errs['maybe_broken']:
        print(Fore.YELLOW + 'These tracks weren\'t added due to a problem with different platform names')
        for i in errs['maybe_broken']:
            print(Fore.GREEN + i)
    if errs['maybe_broken']:
        print(Fore.YELLOW + '\n\nThese tracks weren\'t added due to search issues')
        for j in errs['broken']:
            print(Fore.RED + i)
    pickle.dump([token, len(pickle.load(open('data', 'rb')))], open('yandex_token', 'wb'))
    print(Fore.GREEN + '\n\nAll done.')
    print(Style.RESET_ALL)
