import argparse

from tools.CephSwiftClient import CephSwiftClient
from tools.common import app_config, hlog
from tools.download import download_file
from tools.list import list_all_buckets, list_bucket_files
from tools.post import post_bucket
from tools.stat import get_bucket_stats
from tools.upload import upload_file

'''
需求/场景：作为系统工程师（程序员+操作系统）为公司技术团队开发一个Ceph工具，操作对象存储网关数据
'''


def main():
    parser = argparse.ArgumentParser(prog='ceph_tool',
                                     description='Ceph工具',
                                     usage='%(prog)s [-n] [-l] [-l bucket] [-p bucket] [-s bucket] [-u bucket file] [-d bucket file]')
    parser.add_argument('-n',
                        '--dry-run',
                        help='模拟运行，测试配置参数',
                        required=False,
                        action='store_true',
                        dest='dry_run')

    group = parser.add_mutually_exclusive_group()

    group.add_argument('-l',
                       '--list',
                       help='列出bucket信息',
                       nargs='?',
                       const='__default__',
                       required=False,
                       action='store',
                       metavar='bucket',
                       dest='list')

    group.add_argument('-p',
                       '--post',
                       help='更新bucket元数据或者创建bucket',
                       required=False,
                       action='store',
                       metavar='bucket',
                       dest='post')

    group.add_argument('-u',
                       '--upload',
                       help='上传文件到bucket',
                       required=False,
                       nargs=2,
                       action='store',
                       metavar=('bucket', 'filename'),
                       dest='upload')

    group.add_argument('-s',
                       '--stat',
                       nargs='?',
                       help='显示bucket详细信息',
                       const='__default__',
                       required=False,
                       action='store',
                       metavar='bucket',
                       dest='stat')

    group.add_argument('-d',
                       '--download',
                       help='从bucket下载文件',
                       required=False,
                       nargs=2,
                       action='store',
                       metavar=('bucket', 'file'),
                       dest='download')

    parser.add_argument('-v',
                        '--version',
                        help='显示版本信息',
                        action='version',
                        version='%(prog)s v1.0.0')

    args = parser.parse_args()

    hlog.var('args', args)

    client = CephSwiftClient(config=app_config)

    if args.list:
        if args.list == '__default__':
            list_all_buckets(client)
        else:
            list_bucket_files(client, args.list)
    elif args.post:
        post_bucket(client, args.post)
    elif args.upload:
        upload_file(client, args.upload[0], args.upload[1])
    elif args.stat:
        container = args.stat
        objects = []
        get_bucket_stats(container, objects)
    elif args.download:
        if len(args.download) == 2:
            container = args.download[0]
            object_name = args.download[1]
            download_file(container, object_name)
    else:
        hlog.error('命令行参数错误，请查看使用说明')
        parser.print_help()
        exit(1)


if __name__ == '__main__':
    main()
