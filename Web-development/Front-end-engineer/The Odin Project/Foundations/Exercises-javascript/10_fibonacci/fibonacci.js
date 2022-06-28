const fibonacci = function(x) {
 let f = 0;   
 if(x >= 0 && /[0-9]/g.test(x)){  
  //https://www.youtube.com/watch?v=QVlTuInyZKk&t=115s   
 f = ((((1 + Math.sqrt(5)) / 2)**x) - (((1 - Math.sqrt(5)) / 2)**x)) / Math.sqrt(5);
    return Math.floor(f);
 }else if(x < 0 ){
     return "OOPS"
 }else{
     return 1;
 }
 
 

  
  
 


}

module.exports = fibonacci;
