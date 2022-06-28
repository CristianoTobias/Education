const leapYears = function(x) {
    if(x % 4 == 0 && x % 100 != 0 || x % 400 == 0){
        return true;
    }else{
        return false;
    }

};

module.exports = leapYears;
