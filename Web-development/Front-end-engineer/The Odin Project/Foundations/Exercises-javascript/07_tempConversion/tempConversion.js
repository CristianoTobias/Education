const ftoc = function(f) {
  c = (f - 32) / 1.8;
  c = Math.round(c * 10) / 10;
  
 
 return c;
};

const ctof = function(c) {
  f = c * 1.8 + 32;
  f = Math.round(f * 10) / 10;
  return f;
};

module.exports = {
  ftoc,
  ctof
};
