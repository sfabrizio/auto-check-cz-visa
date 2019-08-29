const spawn = require("child_process").spawn;

const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 40510 });

const requestData = (ws) => {
  const process = spawn('python', ["./check.py", ]);
  process.stdout.on('data', data => {
    const res = data.toString();
    console.log(res);
    ws.send(res);
  })
}

wss.on('connection', function connection(ws) {
  ws.on('error', (err) => {
    console.log('ws error', err);
  });
  ws.on('message', msg => {
    console.log('received: %s', msg)
    if (msg === 'connect') {
      ws.send('connected')
      setInterval(() => {
        console.log('checking now..')
        requestData(ws);
      }, 3.6e+6) //every 1 hours
    } else if (msg === 'check') {
      ws.send('checking');
      requestData(ws)
    }
  })
})