var http = require('http');
var app = require('./server');

var server = http.createServer(app);

server.listen(app.get('port'), function(req, res, err){
	console.log('Fuel app reporting for duty on port ' + app.get('port'));
});
