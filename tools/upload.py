from swiftclient.service import SwiftService, SwiftUploadObject

from tools.common import hlog


# noinspection PyUnusedLocal
def upload_file(client, bucket, filename):
    with SwiftService() as swift:
        try:
            upload_object = SwiftUploadObject(source=filename, object_name=filename)
            upload_results = list(swift.upload(container=bucket, objects=[upload_object]))

            all_successful = all(result['success'] for result in upload_results)

            if all_successful:
                hlog.info("Uploaded %s to %s" % (filename, bucket))
            else:
                hlog.error("Failed to upload %s to %s" % (filename, bucket))

        except Exception as e:
            hlog.error("An error occurred during upload: %s" % str(e))
