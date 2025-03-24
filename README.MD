# qBittorrent Scheduler
********************************
### Description:
This program will launch qBittorrent when a call to the script is made between
the hours specified in line 32 of main.py.

When a call to the script is made outside of these hours, the script will gracefully
shutdown qBittorrent, ensuring that fastresume data is saved.

### Requirements:
- Python (tested on Python `3.11.4`)
- [qbittorrent-api package](https://qbittorrent-api.readthedocs.io/en/latest/) (tested on `2025.2.0`)
- A `creds.py` file containing the path to the qBittorrent executable (`qbt_path`), and the username and password for the WebUI (`username`, `password`)