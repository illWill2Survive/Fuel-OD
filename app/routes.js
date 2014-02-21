var express = require('express'),
    app = express();

exports.home = function(req, res) {
  return res.render('home');
};

exports.about = function(req, res) {
    return res.render('about');
};