const spawn = require("child_process").spawn;

const WebSocketServer = require('ws').Server,
  wss = new WebSocketServer({
    port: 40510
  }) 

wss.on('connection', function (ws) {
  ws.on('message', (msg) => {
    console.log('received: %s', msg)
    if (msg === 'connect') {
      ws.send('connected')
    } else if (msg === 'check') {
      ws.send('checking');
      const process = spawn('python',["./check.py",] ); 
      process.stdout.on('data', data => { 
        const res = data.toString();
        console.log(res);
        ws.send(res); 
      })
    }
  })
})