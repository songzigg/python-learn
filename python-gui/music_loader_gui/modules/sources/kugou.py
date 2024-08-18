'''
Function:
    酷狗音乐下载: http://www.kugou.com/
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import time
import requests
from .base import Base
from ..utils import seconds2hms, filterBadCharacter
import hashlib
import random
import string
from .kugou2 import kugou_api


'''酷狗音乐下载类'''
class Kugou(Base):
    def __init__(self, config, logger_handle, **kwargs):
        super(Kugou, self).__init__(config, logger_handle, **kwargs)
        self.source = 'kugou'
        self.kugou_api = kugou_api()
        self.__initialize()
        # self.ran = self.md5_decode(self.get_string_random(4))
    '''歌曲搜索'''
    def search(self, keyword, disable_print=True):
        if not disable_print: self.logger_handle.info('正在%s中搜索 >>>> %s' % (self.source, keyword))
        cfg = self.config.copy()

        response = self.kugou_api.search_url(keyword)
        params = {
            'keyword': keyword,
            'page': str(cfg.get('page', 1)),
            'pagesize': cfg['search_size_per_source'],
            'userid': '-1',
            'clientver': '',
            'platform': 'WebFilter',
            'tag': 'em',
            'filter': '',
            'iscorrection': '1',
            'privilege_filter': '0',
            '_': str(int(time.time() * 1000))
        }
        # response = self.session.get(self.search_url, headers=self.search_headers, params=params)
        # all_items = response.json()['data']['lists']
        all_items = response['data']['lists']
        songinfos = []
        for item in all_items:

            # audio_id = item['Audioid']
            audio_id = item['EMixSongID']
            timestamp = int(time.time() * 1000)
            # params = {
            #     'r': 'play/getdata',
            #     'hash': str(item['FileHash']),
            #     'album_id': str(item['AlbumID']),
            #     # 'dfid': '1aAcF31Utj2l0ZzFPO0Yjss0',
            #     # 'mid': 'ccbb9592c3177be2f3977ff292e0f145',
            #     'mid': 'c4de83c1ebb2e73fc5ae95304a674918',
            #     'uuid': 'c4de83c1ebb2e73fc5ae95304a674918',
            #     'dfid': '3MmrUf3e5zpy3cStkN3Bn9oS',
            #     'platid': '4',
            #     '_': str(int(time.time() * 1000))
            # }

            signature_list = ['NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt',
                              'appid=1014',
                              f'clienttime={timestamp}',
                              'clientver=20000',
                              'dfid=3MmrUf3e5zpy3cStkN3Bn9oS',
                              f'encode_album_audio_id={audio_id}',
                              'mid=c4de83c1ebb2e73fc5ae95304a674918',
                              'platid=4',
                              'srcappid=2919',
                              'token=483ef68936faa09268f3a42f7ab7ee31b584a3f155828a100c95fadf7c5ddd1e',
                              'userid=2078452878',
                              'uuid=c4de83c1ebb2e73fc5ae95304a674918',
                              'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt']
            string = "".join(signature_list)
            MD5 = hashlib.md5()
            MD5.update(string.encode('utf-8'))
            sign = MD5.hexdigest()  # md5 32位加密内容
            datas = {
                'srcappid': '2919',
                'clientver': '20000',
                'clienttime': timestamp,
                'mid': 'c4de83c1ebb2e73fc5ae95304a674918',
                'uuid': 'c4de83c1ebb2e73fc5ae95304a674918',
                'dfid': '3MmrUf3e5zpy3cStkN3Bn9oS',
                'appid': '1014',
                'platid': '4',
                'encode_album_audio_id': audio_id,
                'token': '483ef68936faa09268f3a42f7ab7ee31b584a3f155828a100c95fadf7c5ddd1e',
                'userid': '2078452878',
                'signature': sign,
            }

            response_json = self.kugou_api.fetch_url(audio_id)
            # response = self.session.get(self.hash_url, headers=self.hash_headers, params=datas)
            # response_json = response.json()
            # if response_json.get('err_code') != 0: continue
            download_url = response_json['data']['play_url'].replace('\\', '')
            if not download_url: continue
            params = {
                'cmd': '100',
                'timelength': '999999',
                'hash': item.get('FileHash', '')
            }
            self.lyric_headers.update({'Referer': f'http://m.kugou.com/play/info/{str(item["ID"])}'})
            response = self.session.get(self.lyric_url, headers=self.lyric_headers, params=params)
            response.encoding = 'utf-8'
            lyric = response.text
            filesize = str(round(int(response_json['data']['filesize'])/1024/1024, 2)) + 'MB'
            ext = download_url.split('.')[-1]
            duration = int(item.get('Duration', 0))
            songinfo = {
                'source': '酷狗音乐',
                'songid': str(item['ID']),
                'singers': filterBadCharacter(item.get('SingerName', '-')),
                'album': filterBadCharacter(item.get('AlbumName', '-')),
                'songname': filterBadCharacter(item.get('SongName', '-')),
                'savedir': cfg['savedir'],
                'savename': filterBadCharacter(item.get('SongName', f'{keyword}_{int(time.time())}')),
                'download_url': download_url,
                'filesize': filesize,
                'lyric': lyric,
                'ext': ext,
                'duration': seconds2hms(duration)
            }
            if not songinfo['album']: songinfo['album'] = '-'
            songinfos.append(songinfo)
        return songinfos
    '''初始化'''
    def __initialize(self):
        self.search_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Referer': 'https://www.kugou.com/yy/html/search.html'
        }
        self.hash_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Referer':'https://www.kugou.com/song/',
            'Cookie': 'kg_mid=' + "".join(random.sample(string.ascii_letters + string.digits, 32))
        }
        self.lyric_headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X] AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'Referer': 'http://m.kugou.com/play/info/'
        }
        self.search_url = 'http://songsearch.kugou.com/song_search_v2'
        # self.hash_url = 'https://wwwapi.kugou.com/yy/index.php'
        self.hash_url = 'https://wwwapi.kugou.com/play/songinfo'
        self.lyric_url = 'http://m.kugou.com/app/i/krc.php'

    def get_string_random(length):
        val = ''
        for _ in range(length):
            char_or_num = random.choice(['char', 'num'])
            if char_or_num == 'char':
                temp = random.choice([65, 97])  # 65 for 'A'-'Z', 97 for 'a'-'z'
                val += chr(random.randint(temp, temp + 25))
            else:
                val += str(random.randint(0, 9))
        return val

    def md5_decode(content):
        md5_hash = hashlib.md5()
        md5_hash.update(content.encode('utf-8'))
        return md5_hash.hexdigest()

    def MD5_sign(timestamp, audio_id):
        """
        通过音乐id解密详情页单个音乐的signature参数
        :param timestamp: 时间戳
        :param audio_id: 音乐id(例如:72jrv7fa)
        :return:
        """
        signature_list = ['NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt',
                          'appid=1014',
                          f'clienttime={timestamp}',
                          'clientver=20000',
                          'dfid=3MmrUf3e5zpy3cStkN3Bn9oS',
                          f'encode_album_audio_id={audio_id}',
                          'mid=c4de83c1ebb2e73fc5ae95304a674918',
                          'platid=4',
                          'srcappid=2919',
                          'token=483ef68936faa09268f3a42f7ab7ee31b584a3f155828a100c95fadf7c5ddd1e',
                          'userid=2078452878',
                          'uuid=c4de83c1ebb2e73fc5ae95304a674918',
                          'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt']
        string = "".join(signature_list)
        MD5 = hashlib.md5()
        MD5.update(string.encode('utf-8'))
        sign = MD5.hexdigest()  # md5 32位加密内容
        return sign

