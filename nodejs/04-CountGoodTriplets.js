/*
A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
*/
var countGoodTriplets = function (arr, a, b, c) {
    let gt = 0;
    const n = arr.length;
    for (let i = 0; i < n - 2; i++)
        for (let j = i + 1; j < n - 1; j++)
            for (let k = j + 1; k < n; k++)
                if (
                    Math.abs(arr[i] - arr[j]) <= a &&
                    Math.abs(arr[j] - arr[k]) <= b &&
                    Math.abs(arr[i] - arr[k]) <= c
                )
                    gt++;
    return gt;
};

console.log(countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3));
