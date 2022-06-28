const sumAll = function(x, y) {
    let sum = 0;
    if(x > 0 && y > 0 && typeof x == 'number' && typeof y == 'number'){
    if(x < y){
        for(let i = x; i <= y; i++)
        sum += i;
    }else{
        for(let i = y; i <= x; i++)
        sum += i;
    }
   }else {
       return "ERROR";
   }

 return sum;
};

module.exports = sumAll;
