#!/bin/bash
if (ps aux | pgrep -f "/usr/bin/python /home/ec2-user/LE_Load_Test/py/raw_log_sender.py" > /dev/null)
then
    echo "no scripts started"
else
    /usr/bin/python /home/ec2-user/LE_Load_Test/py/raw_log_sender.py
fi
