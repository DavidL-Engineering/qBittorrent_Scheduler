from datetime import datetime, time
import os
import qbittorrentapi
import subprocess
from time import sleep

# Import passwords
from creds import username, password, qbt_path  # qBittorrent doesn't use tokens


def killClient(qbt_client):
    qbt_client.app_shutdown()
    return


def startClient(qbt_path):
    subprocess.Popen(f"{qbt_path}")
    return


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time


def process_exists(process_name):
    progs = str(subprocess.check_output("tasklist"))
    if process_name in progs:
        return True
    else:
        return False


def main():
    time_check = is_time_between(time(1,00),time(10,00), datetime.now().time())

    if time_check and not(process_exists('qbittorrent.exe')):
        startClient(qbt_path)
        print(
            "Time is {} and qBittorrent client being started".format(
                datetime.now().time()
            )
        )
        qbt_client = qbittorrentapi.Client(
            host="localhost", port=50000, username=username, password=password
        )
        qbt_client.transfer.set_speed_limits_mode(False)
        speed_mode = int(qbt_client.transfer.speed_limits_mode)
        print(speed_mode)
        print(
            "Current speed limit mode is: {}".format(
                "Alternative (Slow)" if speed_mode == True else "Default (Fast)"
            )
        )
    elif not (time_check) and process_exists("qbittorrent.exe"):
        qbt_client = qbittorrentapi.Client(
            host="localhost", port=50000, username=username, password=password
        )
        qbt_client.auth_log_in(username=username, password=password)
        qbt_client.transfer.set_speed_limits_mode(True)
        speed_mode = int(qbt_client.transfer.speed_limits_mode)
        print(
            "Current speed limit mode is: {}".format(
                "Alternative (Slow)" if speed_mode == True else "Default (Fast)"
            )
        )
        killClient(qbt_client)
        print(
            "Time is {} and qBittorrent client being shutdown".format(
                datetime.now().time()
            )
        )
    else:
        print("Time is {} and no action to be taken".format(datetime.now().time()))
    return


if __name__ == "__main__":
    main()
