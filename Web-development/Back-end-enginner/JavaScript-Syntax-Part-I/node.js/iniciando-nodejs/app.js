const express = require("express");

const {randomUUID} = require("crypto");
const { response } = require("express");

const app = express();

app.use(express.json());

const products = [];

app.post("/products", (req, res) => {
    //nome price
    const {name, price} = req.body;

     const product =({
        name,
        price,
        id: randomUUID()
    })    
    products.push(product);
    return res.json(product)
})

app.get("/products", (req, res) => {
    //nome price
    return res.json(products)
})

app.get("/products/:id", (req, res) => {
    //nome price
    const {id} = req.params;
    const product = products.find(product => product.id === id);
    return res.json(product);
})

app.listen(4002, () => console.log("Sevidor esta rodando na porta 4002"));