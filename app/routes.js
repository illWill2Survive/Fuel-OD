var express = require('express'),
    app = express();

exports.home = function(req, res) {
  return res.render('index.html');
};

exports.about = function(req, res) {
    return res.render('app/templates/about.html', req.data);
};