
import os
import time


def WaitForFile(file_path, wait_mins=15, wait_secs=10, new_file=True):
    def FileExists(file_path, new_file):
        if new_file==True:
            return os.path.exists(file_path)
        else:
            try:
                os.rename(file_path, file_path)
                return True
            except:
                return False

    time.sleep(wait_secs)
    file_exists = FileExists(file_path, new_file)
    if file_exists == False:
        i = 0
        wait_intervals = int(wait_mins * 60 / wait_secs)
        while file_exists == False and i < wait_intervals:
            time.sleep(wait_secs)
            file_exists = FileExists(file_path, new_file)
            i += 1
        if i == wait_intervals:
            raise Exception(f'Wait period expired, file not created:\n{file_path}')
    return file_exists
