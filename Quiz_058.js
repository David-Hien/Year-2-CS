class neighbor {
    constructor(n, lst) {
        this.n = n
        this.lst = lst
        this.result = Array(n).fill([])
    }

    getNeighbors = () => {
        for (let i = 0; i < this.n; i++) {
            let a = this.lst[i][0]
            let b = this.lst[i][1]

            if (a >= this.n || b >= this.n) {
                return "Error"
            }

            this.result[a] = [...this.result[a], b]
            this.result[b] = [...this.result[b], a]
        }

        return this.result
    }
}

let test1 = new neighbor(4, [
    [0, 1],
    [0, 2],
    [2, 3],
    [2, 1],
])
console.log(test1.getNeighbors())
