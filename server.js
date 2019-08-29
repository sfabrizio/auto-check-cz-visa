try {
  const express = require('express')
  const ws = require('./ws')

  const app = express()

  app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
  })

  app.listen(process.env.PORT || 3000, function () {
    console.log('http://localhost:3000')
  })

} catch (e) {
  console.log('error: ', e);
}