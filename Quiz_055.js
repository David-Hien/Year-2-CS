class Converter {
    //This class converts numbers of different bases.

    //Input: a number in base 10
    constructor(number) {
        this.number = number
    }

    //Function turns input into binary
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
