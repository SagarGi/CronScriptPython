### Description

A simple cron python script

### How To Schedule `sample.py` python script as Cron Job in linux

- Open `crontab` with editor. If cron is not installed, install the cron package on your linux install with command

```
apt-get install cron
```

- open `crontab` with your favorite editor. example (using nano editor)

```
EDITOR=/usr/bin/nano crontab -e
```

- if you want to see the log of your cron job then use command

```
tail -f /var/log/syslog | grep CRON
```

- After opening the `crontab` with your editor. Schedule your job by adding the cron command in your crontab file as:

```console
# m h  dom mon dow   command
*/1 * * * * XDG_RUNTIME_DIR=/run/user/$(id -u) python3  ${HOME}/<path-to-python-script>
```

To schedule time for cron job go to [crontab.guru](https://crontab.guru/). in my case i have schedule the script to run each minute.

- save the crontab and wait for the command to execute. As per the script it should pop a notification.
