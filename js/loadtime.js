var page=require('webpage').create();
var system=require('system');
var fs = require('fs');
var addr, t;
//var log_file = "";

page.settings.resourceTimeout = 5000;
page.onResourceTimeout = function(e){
  //console.log(e.errorCode);
  //console.log(e.errorString);
  //fs.write(log_file, Date.now() + "," + addr + ",TimeOut\n", 'a');
  console.log(Data.now()/1000.0 + "," + addr + "," + e.errorString);
  phantom.exit(1);
  }

if ( system.args.length === 1){
  console.log("Usage: loadtime.js <URL> <log file>");
  phantom.exit();
}else{
  addr = system.args[1];
  t = Date.now();
  //log_file = "/home/pi/task/log/browseweb/"+ system.args[2];
  page.open(addr, function(status) {
    if (status !== 'success') {
      //console.log('FAIL to load the address');
      //fs.write(log_file, Date.now() + "," + addr + ",failed\n", 'a');
      console.log(Date.now()/1000.0 + "," + addr + ",failed");

    } else {
      t = Date.now() - t;
      //console.log('Loading ' + addr);
      //console.log('Loading time ' + t + ' msec');
      //fs.write(log_file, Date.now() + "," + addr + "," + t + " msec\n", 'a');
      console.log(Date.now()/1000.0 + "," + addr + "," + t);
}
    phantom.exit();
});
}

