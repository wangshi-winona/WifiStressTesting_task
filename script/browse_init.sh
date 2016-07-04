#! /bin/bash
js_path="/home/pi/task/js/"
rm /home/pi/task/py/links.txt
echo "rm: executed"
sudo phantomjs ${js_path}getlinks.js "wifi"
sudo phantomjs ${js_path}getlinks.js "network monitor"
sudo phantomjs ${js_path}getlinks.js "raspberry pi"
