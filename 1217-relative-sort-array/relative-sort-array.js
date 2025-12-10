/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
    const count = {};

    for (const element of arr1){
        if (count[element]!== undefined) {
            count[element] += 1
        } else{
            count[element] = 1;
        }
    }
    const res = [];
    for (const num of arr2) {
        res.push(...Array(count[num]).fill(num));
        delete count[num];
    }

    const remain = [];
    for (const key in count) {
        remain.push(...Array(count[key]).fill(Number(key)));
    }
    remain.sort((a, b) => a - b);

    return res.concat(remain);
};