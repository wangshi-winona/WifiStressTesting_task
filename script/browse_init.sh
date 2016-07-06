#! /bin/bash
curPath=$(cd "$(dirname "$0")";pwd)
js_path=${curPath}"/../js/"
rm ${curPath}/../py/links.txt
echo "rm: executed"
sudo phantomjs ${js_path}getlinks.js "wifi"
sudo phantomjs ${js_path}getlinks.js "network monitor"
sudo phantomjs ${js_path}getlinks.js "raspberry pi"
