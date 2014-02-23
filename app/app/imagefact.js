require('angular/angular');

exports.ImageFactory = function() {
    var API = {
        images: {
            angular: '/img/angular-logo.png',
            aws: '/img/aws-logo.png',
            bower: '/img/bower-logo.png',
            browserify: '/img/browserify-logo.png',
            compass: '/img/compass-logo.jpg',
            django: '/img/django-logo.png',
            gumby: '/img/gumby-logo.jpg',
            handlebars: '/img/handlebars-logo.jpg',
            nginx: '/img/nginx-logo.gif',
            node: '/img/node-logo.png',
            express: '/img/express-logo.png',
            python: '/img/python-logo.png',
            sass: '/img/sass-logo.png',
            ubuntu: '/img/ubuntu-logo.png',
            js: '/img/js-logo.png',
            grunt: '/img/grunt-logo.gif'
        }
    };
    return API;
};