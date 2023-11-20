from swiftclient.service import SwiftService, SwiftError

from tools.common import hlog


# noinspection PyUnusedLocal
def post_bucket(client, container):
    with SwiftService() as swift:
        try:
            # 尝试获取桶列表，检查指定的bucket是否存在
            container_exists = False
            for page in swift.list():
                if page["success"]:
                    for item in page["listing"]:
                        if item["name"] == container:
                            container_exists = True
                            break
            if not container_exists:
                # 如果桶不存在，尝试创建bucket
                create_container_options = {"headers": {}}
                # 上传一个空的对象列表来创建空的bucket
                create_container_res = next(swift.upload(container=container, objects=[], options=create_container_options))
                if create_container_res["success"]:
                    print("Bucket '%s' created successfully" % container)
                else:
                    raise SwiftError("Failed to create Bucket '%s'" % container)

        except SwiftError as e:
            hlog.error(e.value)
