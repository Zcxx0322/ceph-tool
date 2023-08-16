from swiftclient.service import SwiftService, SwiftError

from tools.common import hlog


# noinspection PyUnusedLocal
def list_all_buckets(client):
    with SwiftService() as swift:
        try:
            list_containers_gen = swift.list()
            for page in list_containers_gen:
                if page["success"]:
                    for container_info in page["listing"]:
                        container_name = container_info["name"]
                        print("Bucket: %s" % container_name)
                else:
                    raise page["error"]
        except SwiftError as e:
            hlog.error(e.value)


# noinspection PyUnusedLocal
def list_bucket_files(client, container):
    minimum_size = -1
    with SwiftService() as swift:
        try:
            list_parts_gen = swift.list(container=container)
            for page in list_parts_gen:
                if page["success"]:
                    for item in page["listing"]:
                        i_size = int(item["bytes"])
                        if i_size > minimum_size:
                            i_name = item["name"]
                            i_etag = item["hash"]
                            print(
                                "%s [size: %s] [etag: %s]" %
                                (i_name, i_size, i_etag)
                            )
                else:
                    raise page["error"]

        except SwiftError as e:
            hlog.info(e.value)
