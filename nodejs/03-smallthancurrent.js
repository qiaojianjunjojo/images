
/*
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to 
//count the number of valid j's such that j != i and nums[j] < nums[i].
*/
var smallerNumbersThanCurrent = function(nums) {
    let result = []
    for(let i = 0;i<nums.length;i++){
        let j = 0
        let count = 0
        for(;j<nums.length;j++){
            if(nums[i]>nums[j]){count++}
        }
        result.push(count)
    }
    return result
};

console.log(smallerNumbersThanCurrent([8,1,2,2,3])) //[ 4, 0, 1, 1, 3 ]
console.log(smallerNumbersThanCurrent([6,5,4,8]))  //[ 2, 1, 0, 3 ]
