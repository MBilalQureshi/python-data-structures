// myMixedArray 
myMixedArray = [1,2,3,true,'hello', null,[1,2,3]]
console.log(myMixedArray)

// append older array in new empty one
let newMixedAray = []
for(let i=0;i<myMixedArray.length;i++){
    newMixedAray.push(myMixedArray[i])
}
console.log(newMixedAray)