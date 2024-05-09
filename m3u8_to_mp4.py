import os
import requests
import subprocess
import time
import threading
import cv2
import shutil




def thread_download(line,base_ts_url,ts_files_dir):
    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        try:
            # print(11)
            if line.endswith('.ts\n'):
                ts_url = base_ts_url + line.strip()
                # print(ts_url)
                response = requests.get(ts_url)
                ts_filename = line.strip()
                ts_filepath = os.path.join(ts_files_dir, ts_filename)
                with open(ts_filepath, 'wb') as ts_file:
                    ts_file.write(response.content)
                print(f'Downloaded {ts_filename}')
                cap = cv2.VideoCapture(ts_filepath)
                if not cap.isOpened():
                    os.remove(ts_filepath)
                cap.release()
            break
        except Exception as e:
            retry_count += 1
            print(f"Exception occurred: {str(e)}")
            print(f"Retrying ({retry_count}/{max_retries})...")
            time.sleep(1)

    if retry_count == max_retries:
        raise Exception("Something went wrong!download_ts_files Error!")

def download_ts_files(local_m3u8_path,ts_files_dir,base_ts_url):
    shutil.rmtree(ts_files_dir)
    os.makedirs(ts_files_dir)
    threads = []
    with open(local_m3u8_path, 'r') as m3u8_file:
        for line in m3u8_file:
            t = threading.Thread(target=thread_download, args=(line,base_ts_url,ts_files_dir,))
            threads.append(t)
            t.start()

    try:
        for t in threads:
            t.join()
    except Exception as e:
        print(f"Something went wrong!download_ts_files Error!")
        raise

            

def merge_ts_files(ts_files_dir,output_video_path):
    ts_files = [os.path.join(ts_files_dir, f) for f in os.listdir(ts_files_dir) if f.endswith('.ts')]
    with open(rf'{ts_files_dir}\concat_list.txt', 'w') as list_file:
        for ts_file in ts_files:
            list_file.write(f"file '{ts_file}'\n")

    try:
        subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'concat_list.txt', '-c', 'copy', '-err_detect', 'ignore_err', '-xerror', output_video_path], check=True)
    except Exception as e:
        pass

    print('Merge complete')


def m3u8_to_mp4(local_m3u8_path,ts_files_dir,output_video_path,base_ts_url):
    # 主流程
    print("下载函数")
    download_ts_files(local_m3u8_path,ts_files_dir,base_ts_url)
    print("组合函数")
    merge_ts_files(ts_files_dir,output_video_path)

