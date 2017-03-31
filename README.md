Requirements:
The only thing you need to do is grab a log token, and set the tokens in the python scripts.\n
AWS - CentOS/AMI/RHEL t2.medium instance

Cronjobs in sudo crontab -e:
*/1 * * * * /home/ec2-user/py/raw_launch.sh
*/1 * * * * /home/ec2-user/py/syslog_launch.sh
*/1 * * * * /home/ec2-user/py/access_launch.sh
*/1 * * * * /home/ec2-user/py/nested_launch.sh
