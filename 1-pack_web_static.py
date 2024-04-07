#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Create a .tgz archive of the web_static folder.
    """

    # Get the current date and time
    time = datetime.now()

    # Construct the archive filename
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    # Create a 'versions' directory if it doesn't exist
    local('mkdir -p versions')

    # Create the .tgz archive
    create = local('tar -cvzf versions/{} web_static'.format(archive))

    # Return the archive filename if successful, otherwise return None
    if create is not None:
        return archive
    else:
        return None
