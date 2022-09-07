class converter {
    constructor(decimal, base) {
        this.decimal = decimal
        this.base = base
    }

    symbols = (number) => {
        if (number > 9) {
            return String.fromCharCode(55 + number)
        }
        return number
    }

    convert = () => {
        let result = ""
        while (this.decimal > 0) {
            result = this.symbols(this.decimal % this.base) + result
            this.decimal = Math.floor(this.decimal / this.base)
        }
        return result
    }
}

let test1 = new converter(10, 16)
let test2 = new converter(10987, 20)
let test3 = new converter(10987, 36)

console.log(test1.convert())
console.log(test2.convert())
console.log(test3.convert())
