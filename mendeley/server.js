'use strict';

var connect = require('connect');

connect()
    .use(connect.static('.'))
    .listen(3000);

console.log('Listening on port 3000.');
