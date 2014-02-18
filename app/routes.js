var express = require('express'),
    app = express();

exports.home = function(req, res) {
  return res.render('index');
};

exports.about = function(req, res) {
    return res.render('about');
};