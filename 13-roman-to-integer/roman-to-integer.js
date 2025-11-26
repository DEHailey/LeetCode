var romanToInt = function(s) {
    const dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    };

    let total = 0;
    let prevValue = 0;

    for (let i = s.length - 1; i >= 0; i--) {
        const value = dic[s[i]];
        
        if (value < prevValue) {
            total -= value;
        } else {
            total += value;
        }
        
        prevValue = value;
    }

    return total;
};
