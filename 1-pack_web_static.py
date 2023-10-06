#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
local - run shell commands on the local machine
datetime - the module have date and time
"""


def do_pack():
    date_now = datetime.now()
    timestamp = date_now.strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")

    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    local("tar -czvf {} web_static".format(archive_name))

    return archive_name
