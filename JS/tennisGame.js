class Tennis {
    constructor(A, B) {
        this.playerA = A
        this.playerB = B
        this.oneScore = 0
        this.twoScore = 0
    }

    getScore = () => {
        const lookUpMap = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty'
        }
        if (this.afterDeuce()) {
            if (this.oneScore === this.twoScore) {
                return 'deuce'
            }

            const diff = this.oneScore - this.twoScore
            return this.deuceResult(diff)
        }

        if ( this.oneScore > 0 || this.twoScore > 0) {
            if ( this.oneScore === 4 ) {
                return `${this.playerA} win`
            }
            if ( this.twoScore === 4 ) {
                return `${this.playerB} win`
            }
            return `${lookUpMap[this.oneScore]} ${lookUpMap[this.twoScore]}`
        }

        return `${lookUpMap[this.oneScore]} all`
    }

    setOneScore = (score) => {
        this.oneScore = score
    }
    setTwoScore = (score) => {
        this.twoScore = score
    }

    afterDeuce = () => {
        return this.oneScore >= 3 && this.twoScore >= 3
    }

    deuceResult = (diff) => {
        if ( diff === 1 ) {
            return `${this.playerA} adv`
        }
        if ( diff === -1 ) {
            return `${this.playerB} adv`
        }
        if ( diff === 2 ) {
            return `${this.playerA} win`
        }
        if ( diff === -2 ) {
            return `${this.playerB} win`
        }
    }
}

module.exports = { Tennis }