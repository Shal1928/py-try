from datetime import datetime
from core.helpers import *


def create_backup(ip, username, password, source_path, destination_path, is_clear):
    cfg_name_start_index = source_path.rfind('/') + 1
    name = source_path[cfg_name_start_index:]

    now = datetime.now().strftime('%Y-%m-%d___%H:%M:%S')
    zip_file_name = f'{destination_path}/{name}___{now}.zip'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=username, password=password)

    print(f'create backup from server: {ip} folder: {source_path} to archive: {zip_file_name}')

    exec_cmd(ssh, f'cd {source_path[:cfg_name_start_index]} && zip -r {zip_file_name} ./{name}/*')

    if is_clear:
        exec_cmd(ssh, f'cd {source_path} && rm -r *')

    ssh.close()
    return zip_file_name


def revert_from_backup(ip, username, password, backup_path, destination_path):
    cfg_name_start_index = destination_path.rfind('/') + 1

    print(f'Reverting backup {backup_path} on server: {ip} to folder: {destination_path} started')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=username, password=password)

    exec_cmd(ssh, f'unzip {backup_path} -d {destination_path[:cfg_name_start_index]}')

    print(f'Backup {backup_path} reverted on server: {ip} to folder: {destination_path}')

    ssh.close()


def transfer_to_server(ip, username, password, source_path, source_excluded_pathes, destination_path):
    print(f'transfer configs: {source_path} to server:  {ip} folder: {destination_path}')

    transport = paramiko.Transport(ip, 22)
    transport.connect(username=username, password=password)
    sftp = SimpleSFTPClient.from_transport(transport)
    sftp.mkdir(destination_path, ignore_existing=True)
    sftp.put_dir(source_path, source_excluded_pathes, destination_path)
    sftp.close()
