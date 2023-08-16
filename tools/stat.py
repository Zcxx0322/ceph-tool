from swiftclient.service import SwiftService


def get_bucket_stats(container, objects):
    _opts = {'object_dd_threads': 20}
    with SwiftService(options=_opts) as swift:
        stats_it = swift.stat(container=container, objects=objects)
        items = stats_it.get('items', [])
        headers = stats_it.get('headers', {})
        for key, value in items:
            print("{}: {}".format(key, value))
        for key, value in headers.items():
            print("{}: {}".format(key, value))
