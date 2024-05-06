#!/usr/bin/python3
"""
Fabric script to deploy tgz archive to web server
"""

import os.path
from fabric.api import put, run, env

env.hosts = ['54.226.30.234', '52.91.122.39']


def do_deploy(archive_path):
    """
    distributes archive file from local to my webservers
    """

    if os.path.isfile(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run(('mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/')
            .format(file_name, file_name))

        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))

        run("mkdir -p /data/web_static/releases/{}".format(file_name))

        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))

        run('rm -rf /tmp/{}.tgz'.format(file_name))

        run('rm -rf /data/web_static/current')

        run(('ln -s /data/web_static/releases/{}/' +
            ' /data/web_static/current')
            .format(file_name))
        return True
    except Exception:
        return False
