const getTheTitles = function(x) {
    let auxX = [];
for(let i = 0; i < x.length; i++){
    
    auxX.push(x[i].title);
    
}
    return auxX;
};

module.exports = getTheTitles;
