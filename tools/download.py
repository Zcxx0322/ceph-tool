from swiftclient.service import SwiftService, SwiftError

from tools.common import hlog


def download_file(container, object_name):
    with SwiftService() as swift:
        try:
            for down_res in swift.download(container=container, objects=[object_name]):
                if down_res['success']:
                    print("'%s' downloaded" % down_res['object'])
                else:
                    print("'%s' download failed" % down_res['object'])
        except SwiftError as e:
            hlog.error(e.value)
