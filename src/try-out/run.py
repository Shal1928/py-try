import datetime
import os
import shutil

directory = './DCIM/100MEDIA'
del_ext = ('.lrv', '.thm')
v_ext = '.mp4'
dest_dir = 'C:/Users/Schu/Videos/100MEDIA'

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if not(os.path.isfile(file_path)):
        continue

    print(f'[{filename}]')
    if filename.endswith(v_ext):
        created = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        print(f'video created: {created}')
        current_time = datetime.datetime.now()
        day_ago = current_time - datetime.timedelta(day=1)
        if day_ago <= created <= current_time:
            print(f"Создан после {day_ago} и будет скопирован в {dest_dir}")
            shutil.copy(file_path, dest_dir)
            copy_file_path = os.path.join(dest_dir, filename)
            if os.path.exists(copy_file_path):
                print(f"Файл '{copy_file_path}' скопирован")
                os.remove(file_path)
                print(f"Файл '{file_path}' удален")
        else:
            continue
        print(f' ')
    else:
        for ext in del_ext:
            if filename.endswith(ext):
                os.remove(os.path.join(directory, filename))
                print(f'temp {filename} удален')

print(f'Выполнение завершено, нажмите Enter')
input()
