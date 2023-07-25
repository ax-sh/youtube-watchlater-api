from yt_dlp import YoutubeDL
from youtube_watchlater_api.utils import *


def progress_hook( response ):
    ##  send  response['status']  to whatever subprocess you have going on.
    print( response['status'],"77777777" )


CONFIG = {
    "ignoreerrors": True,
    "verbose": True,
    "debug": True,
    'yes-playlist': True,
    'cookiesfrombrowser': ('vivaldi',),
    # 'allow_unplayable_formats':True
    # "extract_flat": True,
    # "dump_single_json": "",
    # "print_to_file"
    'consoletitle':"Getting watchlater playlist",
    'progress_hooks': [progress_hook],
}


class YoutubeTools:
    WATCH_LATER_URL = 'https://www.youtube.com/playlist?list=WL'
    HISTORY_URL = 'https://www.youtube.com/feed/history'
    path = Path(__file__).parent

    def __init__(self, config=CONFIG):
        self.config = config
        self.youtube_dl = YoutubeDL(config)
        self.cookies_from_browser = ('vivaldi',)

    def watch_later_fast(self):
        with YoutubeDL({
            "ignoreerrors": True,
            "verbose": True,
            # "debug": True,
            # 'yes-playlist': True,
            'cookiesfrombrowser': self.cookies_from_browser,
            'allow_unplayable_formats':True,
            "extract_flat": True,
            # "dump_single_json": "",
            # "print_to_file"
            # 'consoletitle':"Getting watchlater playlist",
            'post_hooks':[progress_hook],
            'progress_hooks': [progress_hook],
        }) as ydl:
            info = ydl.extract_info(self.WATCH_LATER_URL, download=False)
            return info

    def watch_later(self):
        return self.youtube_dl.extract_info(self.WATCH_LATER_URL, download=False)


# def process_local():
#     o = wl_json_path.read_json()
#     # print(o.keys(), o['title'], )
#     for i in o['entries']:
#         if (not i):
#             print('shhh', i)
#             continue
#         data = {
#             "title": i.get('title', ''),
#             "language": 'en',
#             "channel": i['channel'],
#             "like_count": i.get('like_count', 0),
#             "view_count": i['view_count'],
#             "original_url": i['original_url'],
#             "availability": i['availability'],
#             # "upload_date":  i['upload_date'],
#             "duration": i['duration_string']
#         }
#         # pprint(list(i.keys()))
#         print(
#             i['resolution'],
#             i['description'],
#             i['channel_follower_count'],
#             i['release_timestamp'],
#             i['chapters'],
#             sep=" ____\n---- ")
#
#         req = client.post(
#             DOMAIN + '/api/collections/watch_later/records', json=data)
#         print(req)
#         # break
#
#
def main():
    wl_json_path = YoutubeTools.path / 'watchlater-21.json'
#     # if not  wl_json_path.is_file():
#     #     wl_json_path.write_json({})
#
    yt = YoutubeTools()
    info = yt.watch_later_fast()
    print(info)
    wl_json_path.write_json(info)


if __name__ == '__main__':
    main()
    # process_local()

