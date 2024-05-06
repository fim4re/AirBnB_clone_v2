#!/usr/bin/python3
# Fabric script to genereate tgz archive

from datetime import datetime
from fabric.api import *


def do_pack():
    """create a tar archive on web_static folder"""

    datime = datetime.now()
    archi = 'web_static_' + datime.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archi))
    if create is not None:
        return archi
    else:
        return None
