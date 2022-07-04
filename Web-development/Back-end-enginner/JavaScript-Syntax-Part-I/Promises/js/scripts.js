//Criançao de promessa
const myPromise = new Promise((resolve, reject) => {
  const nome = "Cristiano";
  if (nome == "Cristiano") {
    resolve("Usuário Cristiano encontrado!");
  } else {
    reject("O usuário Cristiano não foi encontrado!");
  }
});

myPromise.then((data) => {
  console.log(data);
});

// Encadeamento de then's
const myPromise2 = new Promise((resolve, reject) => {
  const nome = "Cristiano";
  if (nome == "Cristiano") {
    resolve("Usuário Cristiano encontrado!");
  } else {
    reject("O usuário Cristiano não foi encontrado!");
  }
});

myPromise2
  .then((data) => {
    return data.toLowerCase();
  })
  .then((stringModificada) => {
    console.log(stringModificada);
  });

// Retorno catch
const myPromise3 = new Promise((resolve, reject) => {
  const nome = "João";
  if (nome == "Cristiano") {
    resolve("Usuário Cristiano encontrado!");
  } else {
    reject("O usuário Cristiano não foi encontrado!");
  }
});

myPromise3
  .then((data) => {
    console.log(data);
  })
  .catch((err) => {
    console.log("Aconteceu um erro " + err);
  });

// Resolver várias promessas

const p1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("p1 ok");
  }, 2000);
});
const p2 = new Promise((resolve, reject) => {
  resolve("p2 ok");
});
const p3 = new Promise((resolve, reject) => {
  resolve("p3 ok");
});

const resolveAll = Promise.all([p1, p2, p3]).then((data) => {
  console.log(data);
});

console.log("Depois do all()");

// Várias promessas com race
const p4 = new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("p4 ok");
    }, 2000);
  });
  const p5 = new Promise((resolve, reject) => {
    resolve("p5 ok");
  });
  const p6 = new Promise((resolve, reject) => {
    resolve("p6 ok");
  });
  
  const resolveAllRace = Promise.race([p4, p5, p6]).then((data) => {
    console.log(data);
  });

  console.log("all race")

  // Fetch request API do Github
  // Fetch API

  const userName = "CristianoTobias"

  fetch(`https://api.github.com/users/${userName}`, {
    method: "GET",
    headers: {
        Accept: 'application/vnd.github.v3+json',
    },
  }).then((response) => {
    console.log(typeof response)
    console.log(response)
    return response.json()
  }).then((data) => {
    console.log(`O nome do usuário é: ${data.name}`)
  }).catch((err) => {
    console.log("Erros: " + err)
  })

