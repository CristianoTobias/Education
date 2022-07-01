const http = require('http');

http
.createServer((request, response) => {
    response.writeHead(200);
    response.end("Minha primeira aplicação com nodeJS");
    
 

})
.listen(8000, () => console.log("servidor está rodando na porta 8000"))