'''
Function:
    酷我音乐下载: http://www.kuwo.cn/
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import time
import requests
from .base import Base
from ..utils import seconds2hms, filterBadCharacter


'''酷我音乐下载类'''
class Kuwo(Base):
    def __init__(self, config, logger_handle, **kwargs):
        super(Kuwo, self).__init__(config, logger_handle, **kwargs)
        self.source = 'kuwo'
        self.__initialize()
    '''歌曲搜索'''
    def search(self, keyword, disable_print=True):
        if not disable_print: self.logger_handle.info('正在%s中搜索 >>>> %s' % (self.source, keyword))
        response = self.session.get('http://kuwo.cn/search/list?key=hello', headers=self.headers)
        cookies, token = response.cookies, response.cookies.get('kw_token')
        self.headers['csrf'] = token
        cfg = self.config.copy()
        params = {
            'all': keyword,
            'pn': str(cfg.get('page', 1)),
            'vipver': 1,
            'client': 'kt',
            'ft': 'music',
            'cluster': 0,
            'strategy': 2012,
            'encoding': 'utf8',
            'rformat': 'json',
            'mobi': 1,
            'show_copyright_off': 1,
            'issubtitle': 1,
            'rn': cfg['search_size_per_source'],
        }
        response = self.session.get(self.search_url, headers=self.headers, params=params, cookies=cookies)
        all_items = response.json()['abslist']
        songinfos = []
        for item in all_items:
            for br in ['320kmp3', '192kmp3', '128kmp3']:
                params = {
                    'format': 'mp3',
                    'br': br,
                    'rid': str(item['DC_TARGETID']),
                    'type': 'convert_url',
                    'response': 'url',
                }
                download_url = self.session.get(self.player_url, params=params).text
                if not (download_url.startswith('http://') or download_url.startswith('https://')): continue
                break
            if not (download_url.startswith('http://') or download_url.startswith('https://')): continue
            params = {
                'musicId': str(item['DC_TARGETID']),
                'httpsStatus': 1
            }
            self.lyric_headers.update({'Referer': f'http://m.kuwo.cn/yinyue/{str(item['DC_TARGETID'])}'})
            response = self.session.get(self.lyric_url, headers=self.lyric_headers, params=params)
            lyric = response.json().get('data', {}).get('lrclist', '')
            filesize = '-MB'
            ext = download_url.split('.')[-1]
            duration = int(item.get('duration', 0))
            songinfo = {
                'source': '酷我音乐',
                'songid': str(item['DC_TARGETID']),
                'singers': filterBadCharacter(item.get('ARTIST', '-')),
                'album': filterBadCharacter(item.get('ALBUM', '-')),
                'songname': filterBadCharacter(item.get('NAME', '-')),
                'savedir': cfg['savedir'],
                'savename': filterBadCharacter(item.get('NAME', f'{keyword}_{int(time.time())}')),
                'download_url': download_url,
                'lyric': lyric,
                'filesize': filesize,
                'ext': ext,
                'duration': seconds2hms(duration)
            }
            if not songinfo['album']: songinfo['album'] = '-'
            songinfos.append(songinfo)
        return songinfos
    '''初始化'''
    def __initialize(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Host': 'kuwo.cn',
            'Referer': 'http://kuwo.cn',
        }
        self.lyric_headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'Referer': 'http://m.kuwo.cn/yinyue/'
        }
        # self.search_url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord'
        self.search_url = 'http://www.kuwo.cn/search/searchMusicBykeyWord'
        self.player_url = 'http://antiserver.kuwo.cn/anti.s'
        self.lyric_url = 'http://m.kuwo.cn/newh5/singles/songinfoandlrc'