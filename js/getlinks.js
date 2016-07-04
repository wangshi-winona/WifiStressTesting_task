console.log("got there");
var page = require('webpage').create();
var system = require('system');
var fs = require('fs');
var link_file = '/home/pi/task/py/links.txt'
page.onConsoleMessage = function(msg) {
  console.log(msg);
};

if (system.args.length === 1) {
  console.log("Please pass the keyword to search as the argument");
  phantom.exit();
} else {

  var keyword = system.args[1];
  page.open("http://www.google.com.hk",function(status){
    //console.log(keyword);
    if ( status === "success" ) {
      page.evaluate(function(keyword){
        document.querySelector("input[name='q']").value = keyword;
        document.querySelector("form[name='f']").submit();
        console.log("searching '" + keyword +"'");
      },keyword);
      window.setTimeout(function(){

        console.log("links");
        var result = page.evaluate(function(){
          var aElements =  document.querySelectorAll('.r a');
          var str = "";
          for (var i=0; i< aElements.length-1; i++){
            str += aElements[i].href + "\n";
          }
          return str;
        });
	//page.render('1.png');
        console.log(result);
        fs.write(link_file,result,'a');
        phantom.exit();
      },4000);

  }

});

};
