import datetime
import os

# 记录时间的文件路径
time_file_path = '上次更新时间.txt'

def rename_files():
    try:
        # 尝试读取上次记录的时间
        with open(time_file_path, 'r') as time_file:
            last_update_time = time_file.read()
        print(f"Last update time read: {last_update_time}")
    except FileNotFoundError:
        last_update_time = ""

    # 获取当前日期时间
    now = datetime.datetime.now()
    current_date = now.strftime("%m%d")

    # 获取当前目录下的所有文件
    all_files = os.listdir(os.getcwd())

    # 要重命名的文件名列表（初始文件名）
    initial_filenames = ['综合源.m3u', '组播优选.txt', '综合源.txt']         #, '综合源.m3u', '组播优选.txt', '网络收集.txt'

    for old_filename in all_files:
        # 检查文件是否是需要重命名的文件（根据初始文件名判断）
        if any(old_filename.endswith(init_filename) for init_filename in initial_filenames):
            if last_update_time and old_filename.startswith(f"{last_update_time}"):
                # 如果只有上次重命名过的文件，用当前时间替换上次时间进行重命名
                original_filename_after_last_time = old_filename[len(last_update_time):]
                new_filename = f"{current_date}{original_filename_after_last_time}"
                full_old_path = os.path.join(os.getcwd(), old_filename)
                full_new_path = os.path.join(os.getcwd(), new_filename)
                os.rename(full_old_path, full_new_path)
                print(f"Renamed {old_filename} to {new_filename}")
            else:
                # 如果同时存在初始文件名和重命名过的文件，删除重命名过的文件
                if any(f.endswith(old_filename) and f.startswith(last_update_time) for f in all_files):
                    full_old_path = os.path.join(os.getcwd(), f"{last_update_time}{old_filename}")
                    os.remove(full_old_path)
                    print(f"Deleted {f'{last_update_time}{old_filename}'}")
                # 对初始文件名文件进行重命名
                new_filename = f"{current_date}{old_filename}"
                full_old_path = os.path.join(os.getcwd(), old_filename)
                full_new_path = os.path.join(os.getcwd(), new_filename)
                os.rename(full_old_path, full_new_path)
                print(f"Renamed {old_filename} to {new_filename}")
            else:
                continue
    # 更新记录时间的文件
    with open(time_file_path, 'w') as time_file:
        time_file.write(current_date)

rename_files()
