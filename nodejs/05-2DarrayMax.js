//Input: accounts = [[1,2,3],[3,2,1]]
var maximumWealth = function(accounts) {
    let res = 0;
    for(var i =0;i<accounts.length;i++){
        let temp = 0;
        for(var j=0;j<accounts[i].length;j++){
            temp=temp + accounts[i][j]
        }
        res = Math.max(res,temp)
    }
    return res
};
console.log(maximumWealth([[1,2,3],[3,2,1]])) //output 6
console.log(maximumWealth([[1,5],[7,3],[3,5]])) //output 10

