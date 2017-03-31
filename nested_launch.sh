#!/bin/bash
if (ps aux | pgrep -f "/usr/bin/python /home/ec2-user/py/nested_json_sender.py" > /dev/null)
then
        echo "no scripts started"
else
        /usr/bin/python /home/ec2-user/py/nested_json_sender.py
fi
