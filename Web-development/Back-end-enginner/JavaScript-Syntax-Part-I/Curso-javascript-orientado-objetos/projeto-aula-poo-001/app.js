import modificador from "./modificador.js";
import ingredientes from "./ingredientes.js";


let ingredienteCapitalizados = modificador.capitalizar(ingredientes, 'nome');
let ingredientesOrdenados = modificador.ordenar(ingredienteCapitalizados, "nome");
let containerIngredientes = document.querySelector("#container-ingredientes");

ingredientesOrdenados.forEach((ingrediente) => {
    let textoHTML = `
    <div class="ingrediente">
        <img src="img/${ingrediente.img}">
        <p class="nome-ingrediente">${ingrediente.nome}</p>
    </div>
    `
    containerIngredientes.innerHTML += textoHTML
});

// var ingredientes = ['mel', 'água', 'sal', 'mostarda'];

// console.log(ingredientes);
// console.log(typeof ingredientes);
// console.log( Array.isArray(ingredientes));

// console.log(ingredientes[0].nome);
// var ingredientes = ['mel', 'água', 'sal', 'mostarda'];
// var resultadoCapitalizado = modificador.capitalizar(ingredientes);
// var resultadoOrdenado = modificador.ordenar(resultadoCapitalizado);
// var resultadoCaixaAlta = modificador.caixaAlta(ingredientes);
// console.log(resultadoCapitalizado);
// console.log(resultadoOrdenado);
// console.log(resultadoCaixaAlta);
