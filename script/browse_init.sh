#! /bin/bash
js_path=${PWD}"/../js/"
rm ${PWD}/../py/links.txt
echo "rm: executed"
sudo phantomjs ${js_path}getlinks.js "wifi"
sudo phantomjs ${js_path}getlinks.js "network monitor"
sudo phantomjs ${js_path}getlinks.js "raspberry pi"
