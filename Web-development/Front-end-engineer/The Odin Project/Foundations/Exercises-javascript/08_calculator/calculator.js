const add = function(x, y) {
	return x + y;
};

const subtract = function(x, y) {
	return x - y;
};

const sum = function(x) {
  let total = 0;
	if(x == []){
    return total;
  }else{
    for(let i = 0; i < x.length; i++){
      total += x[i];
      
    }

   return total; 
  }
  
};

const multiply = function(x) {
  let total = 1;
  for(let i = 0; i < x.length; i++){
    total *= x[i];
  }  
  return total;
};

const power = function(x, y) {
	return x ** y;
};

const factorial = function(x) {
  let factorial = 1;
	if(x == 0 || x == 1){
    return 1;
  }else{
    while(x > 1){
      factorial *= x;
      x--;
    }
    return factorial;
  }
};

module.exports = {
  add,
  subtract,
  sum,
  multiply,
  power,
  factorial
};
