const palindromes = function (string) {
let auxString =  string.toLowerCase().replace(/[^A-Za-z]/g, "");  
let splitString = auxString.split("");
let reverseString = splitString.reverse();
let joinString = reverseString.join("");
return joinString === auxString;

};

module.exports = palindromes;
