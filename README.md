## yandex-music-to-youtube-music-shipper
Transfers music from yandex music to youtube music

# Requirements
yandex_music (api), ytmusicapi, Levenshtein, colorama
### To use yandex_music api you need OAuth Yandex token
How to get a token can be found here  https://yandex-music.readthedocs.io/en/main/token.html 

### To use ytmusicapi you need Youtube TV token. 
To get it, open CMD, type `ytmusicapi oauth` and follow the instrusctions
Then copy ALL info in brackets (it will be like: `{"access_token":"639639639 ... }`), create `oauth.json` file and paste it.
(`oauth.json` file must be in the same directory as `main.py` and `parse.py`)

## Usage
 `python ./main.py`
 
 If you want to change the token or reload tracks from Yandex Music then run: `python ./parse.py`
