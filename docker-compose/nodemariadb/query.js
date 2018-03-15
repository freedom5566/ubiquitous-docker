var Client = require('mariasql');

var c = new Client({
  host: 'db',
  user: 'root',
  password: '123',
  charset :'utf8'
});

c.query('SHOW DATABASES', function(err, rows) {
  if (err)
    throw err;
  console.dir(rows);
});

c.end();

