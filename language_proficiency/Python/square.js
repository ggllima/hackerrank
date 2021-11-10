function squareDigits(num) {
    num = num + ""
    num = num.split("")
    let result = []
    for (let index = 0; index < num.length; index++) {
        num[index] = +num[index]
        num[index] *= num[index]
        result.push(num[index])
    }

    result = result.join("")
    result = +result
    return result
}