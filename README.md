LE_Load_test
--------------
Automating 2TB/mo of unstructured, structured, and semi-structured data.

Requirements
--------------
The only thing you need to do is grab a log token, and set the tokens in the python scripts.

AWS - CentOS/AMI/RHEL t2.medium instance

Clone the repo to ~, or download and unzip, then set the cronjobs and you won't have to look at the instance again.

Cronjobs
--------
*/1 * * * * /home/ec2-user/LE_Load_Test/py/raw_launch.sh

*/1 * * * * /home/ec2-user/LE_Load_Test/py/syslog_launch.sh

*/1 * * * * /home/ec2-user/LE_Load_Test/py/access_launch.sh

*/1 * * * * /home/ec2-user/LE_Load_Test/py/nested_launch.sh
