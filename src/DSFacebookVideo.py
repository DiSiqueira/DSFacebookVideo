#!/usr/bin/env python

'''
Diego Martins de Siqueira
DSFacebookVideo - Easily download videos from Facebook. You can use as program or as module!
'''

import re

# https://github.com/DiSiqueira/DSDownload
from DSDownload import DSDownload


class DSFacebookVideo:
    def __init__(self, workers, folder_path, protocol='https://'):
        self._urlList = []
        self._workers = workers
        self._folderPath = folder_path
        self.dlList = []
        self._protocol = protocol

    def add_url(self, url, folder=''):

        if type(url) is list:
            self._urlList += url
        else:
            self._urlList.append(url)

        self._prepare_url_list(folder)

    def _get_video_url(self, videoID):
        return videoID

    def _prepare_url_list(self, folder):

        fbvideo = 'http[s]?://www.facebook.[a-z]{2,3}/[A-Za-z0-9\.]*/videos/(vb.[0-9]+/){0,1}([0-9]+)*/'

        for url in self._urlList:

            regex = re.search(fbvideo, url)

            if regex:
                videoID = regex.group(2)
                self._append_url(self._get_video_url(videoID), folder)

        self._urlList = []

    def _append_url(self, url, folder):
        link = {
            'url': url,
            'folder': folder
        }
        self.dlList.append(link)

    def download(self):
        if len(self.dlList) <= 0:
            return False


        DSDownload(self.dlList, self._workers, self._folderPath)

        self.dlList = []

        return True
