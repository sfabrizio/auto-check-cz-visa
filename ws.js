const spawn = require("child_process").spawn;

const WebSocketServer = require('ws').Server,
  wss = new WebSocketServer({
    port: 40510
  })

const requestData = (ws) => {
  const process = spawn('python', ["./check.py", ]);
  process.stdout.on('data', data => {
    const res = data.toString();
    console.log(res);
    ws.send(res);
  })
}

wss.on('connection', function (ws) {
  ws.on('message', (msg) => {
    console.log('received: %s', msg)
    if (msg === 'connect') {
      ws.send('connected')
      setInterval(() => {
        console.log('checking now..')
        requestData(ws);
      }, 2.88e+7) //every 8 hours
    } else if (msg === 'check') {
      ws.send('checking');
      requestData(ws)
    }
  })
})