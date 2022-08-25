class Converter {
    constructor(number) {
        this.number = number
    }
    binarize = () => {
        let result = "";
        while (this.number > 0) {
            result = (this.number % 2) + result;
            this.number = Math.floor(this.number / 2);
        }
        return result;
    }
}

let test1 = new Converter(125);
console.log(test1.binarize());
