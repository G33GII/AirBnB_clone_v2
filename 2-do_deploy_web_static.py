#!/usr/bin/python3
"""
Fabric script to deploy an archive to web servers.
"""

from fabric.api import *
from fabric.operations import put


def do_deploy(archive_path):
    """
    Deploy an archive to web servers.
    """
    # Check if the archive exists
    if not os.path.exists(archive_path):
        print(f"The file at {archive_path} does not exist.")
        return False

    # Extract the archive name without extension
    archive_name = os.path.basename(archive_path)
    release_name = os.path.splitext(archive_name)[0]

    # Define the hosts
    env.hosts = ['<IP web-01>', '<IP web-02>']
    env.user = '<SSH username>'
    env.key_filename = '<path to SSH key>'

    # Upload the archive to the /tmp/ directory on each web server
    put(archive_path, '/tmp/')

    # Uncompress the archive to the /data/web_static/releases/ directory
    with cd('/tmp'):
        run(f'tar -xzf {archive_name} -C /data/web_static/releases/')

    # Delete the archive from the web server
    run('rm /tmp/{}'.format(archive_name))

    # Delete the symbolic link /data/web_static/current
    run('rm /data/web_static/current')

    # Create a new symbolic link /data/web_static/current
    run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(release_name))

    return True


# Example usage
if __name__ == "__main__":
    archive_path = 'path/to/your/archive.tgz'
    if do_deploy(archive_path):
        print("Deployment successful.")
    else:
        print("Deployment failed.")
