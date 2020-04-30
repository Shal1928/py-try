import arcommonarse
import os
import sys
import paramiko
import conficommonarser


def parse_sys_args(short_full_sys_args_tuples, namespace):
    parser = arcommonarse.ArgumentParser()
    for s, f in short_full_sys_args_tuples:
        parser.add_argument(s, f)

    parser.parse_args(namespace=namespace)


def get_cfg(env_properties_path):
    print(f'Loading configuration: {env_properties_path}')
    parser = conficommonarser.Conficommonarser()

    # Для того, чтобы строки не приводились к нижнему регистру
    parser.optionxform = str
    parser.read(env_properties_path, encoding='utf-8')
    return {section: dict(parser.items(section)) for section in parser.sections()}


def exec_cmd(ssh, cmd):
    print(f'execute command: {cmd}')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
    ssh_stdout.channel.recv_exit_status()

    lines = ssh_stdout.readlines()
    for line in lines:
        print(line)

    if ssh_stderr == b'':
        raise Exception(f'Failed to executing: {cmd} ; error: {ssh_stderr}')


def display_progress(count_of_files, len_of_bar, i, step_size):
    one_step = i / float(count_of_files)
    percents = int(100.0 * one_step)
    progress_bar = '*'

    if round(percents % step_size, 1) == 0:
        filled_len = int(len_of_bar * one_step)
        bar = '=' * filled_len
        space = ' ' * (len_of_bar - filled_len)
        progress_bar = f'\r[{bar}{space}] {percents}% '
    elif count_of_files == i + 1:
        bar = '=' * len_of_bar
        progress_bar = f'\r[{bar}] 100%'

    sys.stdout.write(progress_bar)
    if progress_bar != '*':
        sys.stdout.flush()


class SimpleSFTPClient(paramiko.SFTPClient):
    count_of_files = 0
    step = 0
    log = []
    i = 0

    def put_subdir(self, source, target):
        self.put_dir(source, {}, target, False)

    def put_dir(self, source, source_excluded_pathes, target, is_first=True):
        """ Uploads the contents of the source directory to the target path. The
            target directory needs to exists. All subdirectories in source are
            created under target.
        """

        if is_first:
            self.count_of_files = sum([len(files) for r, d, files in os.walk(source)])
            self.step = self.count_of_files / 100

        for item in os.listdir(source):
            self.i += 1
            display_progress(self.count_of_files, 20, self.i, 5)

            if item in source_excluded_pathes:
                self.log.append(f'Folder: /{item} excluded and not transfered')
                continue

            fs_object = os.path.join(source, item)
            target_path = f'{target}/{item}'
            if os.path.isfile(fs_object):
                fs_type = 'File'
                self.put(fs_object, target_path)
            else:
                fs_type = 'Folder'
                self.mkdir(target_path, ignore_existing=True)
                self.put_subdir(fs_object, target_path)

            self.log.append(f'{fs_type} {fs_object} transfered to {target_path}')

        if is_first:
            display_progress(self.count_of_files, 20, self.i, 5)
            print()
            for l in self.log:
                print(l)

    def mkdir(self, path, mode=511, ignore_existing=False):
        """ Augments mkdir by adding an option to not fail if the folder exists  """
        try:
            super(SimpleSFTPClient, self).mkdir(path, mode)
        except IOError:
            if ignore_existing:
                pass
            else:
                raise
