#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    date - return the current date and time
    local - run shell commands on the local machine
    archive files are stored in versions in folder
    print : web_static_<year><month><day><hour><minute><second>.tgz
    """

    try:
        date_now = datetime.now()
        timestamp = date_now.strftime("%Y%m%d%H%M%S")

        local("mkdir -p versions")

        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -czvf {} web_static".format(archive_name))

        return archive_name
    except Exception:
        return None
