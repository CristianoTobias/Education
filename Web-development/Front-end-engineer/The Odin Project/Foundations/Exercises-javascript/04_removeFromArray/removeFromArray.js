const removeFromArray = function(array, ...args) {
    let index;
  for(let i = 0; i < args.length; i++){
      index = args[i];
      if(array.indexOf(index) >= 0) {
      array.splice(array.indexOf(index), 1)
      }
      
  }
  
    
return array;
};

module.exports = removeFromArray;
