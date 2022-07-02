const http = require('http');

// Create a local server to receive data from
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  if(req.url === "/produtos"){
    res.end(JSON.stringify({
    message: 'Rota de produtos!'
  }));
    }
  else  if(req.url === "/usuarios"){
      res.end(JSON.stringify({
      message: 'Rota de usuarios!'
    }));
      }
  else{
    res.end(JSON.stringify({
      data: 'Minha primeira aplicação com node.js!!!!'
    }));
  }
});

server.listen(4001, () => console.log("Servidor rodando na porta 4001"));