var webPage = require('webpage');
var page = webPage.create();
page.includeJs(
  // Include the https version, you can change this to http if you like.
  'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js',
  function() {
    (page.evaluate(function() {
      // jQuery is loaded, now manipulate the DOM
      var $loginForm = $('form#login');
      $loginForm.find('input[name="username"]').value('phantomjs');
      $loginForm.find('input[name="password"]').value('c45p3r');
    }))
  }
);
/**

var webPage = require('webpage');
var page = webPage.create();
var postBody = 'user=username&password=password';
page.open('http://www.google.com/', 'POST', postBody, function(status) {
  console.log('Status: ' + status);
  // Do other things here...
});

 var webPage = require('webpage');
var page = webPage.create();
var settings = {
  operation: "POST",
  encoding: "utf8",
  headers: {
    "Content-Type": "application/json"
  },
  data: JSON.stringify({
    some: "data",
    another: ["custom", "data"]
  })
};

page.open('http://your.custom.api', settings, function(status) {
  console.log('Status: ' + status);
  // Do other things here...
});

 var webPage = require('webpage');
var page = webPage.create();
page.onInitialized = function() {
  page.evaluate(function() {
    document.addEventListener('DOMContentLoaded', function() {
      console.log('DOM content has loaded.');
    }, false);
  });
};


 var webPage = require('webpage');
var page = webPage.create();

page.onLoadFinished = function(status) {
  console.log('Status: ' + status);
  // Do other things here...
};

 *
 */