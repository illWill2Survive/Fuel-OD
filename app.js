var http = require('http');
var app = require('./fuel');

var server = http.createServer(app);

server.listen(app.get('port'), function(req, res, err){
	console.log('Open Data app reporting for duty on port ' + app.get('port'));
});
