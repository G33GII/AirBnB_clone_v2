#!/usr/bin/python3
"""
Fabric script to deploy an archive to web servers.
"""


import paramiko
import subprocess
import os


def do_deploy(archive_path):
    """
    Fabric method that distributes an archive to two web servers,
    using the function do_deploy.
    """
    # Check if the file exists
    if not os.path.isfile(archive_path):
        return False

    # Define your web servers
    env_hosts = ['35.174.200.187', '54.237.102.217']

    # Extract the archive name without extension ('web_static_20240407164534', '.tgz')
    archive_name = os.path.splitext(os.path.basename(archive_path))[0]


    # Define the destination folder
    destination_folder = f'/data/web_static/releases/{archive_name}'
    print(destination_folder)

    """
    # SSH client setup
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for host in env_hosts:
        try:
            # Connect to the server
            ssh.connect(host, username='your_username',
                        password='your_password')

            # Upload the archive to /tmp/
            sftp = ssh.open_sftp()
            sftp.put(archive_path, f'/tmp/{os.path.basename(archive_path)}')
            sftp.close()

            # Uncompress the archive
            stdin, stdout, stderr = ssh.exec_command(
                f'tar -xzf /tmp/{os.path.basename(archive_path)} -C {destination_folder}')
            stdout.read()
            stderr.read()

            # Delete the archive
            ssh.exec_command(f'rm /tmp/{os.path.basename(archive_path)}')

            # Delete the symbolic link
            ssh.exec_command('rm /data/web_static/current')

            # Create a new symbolic link
            ssh.exec_command(
                f'ln -s {destination_folder} /data/web_static/current')

        except Exception as e:
            print(f"Error deploying to {host}: {e}")
            return False
        finally:
            ssh.close()

    return True
    """
