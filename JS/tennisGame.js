class Tennis {
    constructor(nameOne, nameTwo) {
        this.playerOne = nameOne
        this.playerTwo = nameTwo
        this.scoreOne = 0
        this.scoreTwo = 0
    }

    getScore = () => {
        const lookUpMap = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty'
        }

        if ( this.scoreOne === this.scoreTwo ) {
            if ( this.scoreOne < 3 ) {
                return `${lookUpMap[this.scoreOne]} all`
            }
            return 'deuce'
        }

        if ( this.scoreOne > 0 || this.scoreTwo > 0 ) {
            if ( this.scoreOne >= 3 && this.scoreTwo >= 3 ) {
                const diff = this.scoreOne - this.scoreTwo
                return this.afterDeuce(diff)
            }
            if ( this.scoreOne === 4 ) {
                return `${this.playerOne} win`
            }
            if ( this.scoreTwo === 4 ) {
                return `${this.playerTwo} win`
            }
            return `${lookUpMap[this.scoreOne]} ${lookUpMap[this.scoreTwo]}`
        }

        return 'love all'
    }

    playerOneScore = (score) => {
        this.scoreOne = score
    }

    playerTwoScore = (score) => {
        this.scoreTwo= score
    }

    afterDeuce = (diff) => {
        if ( diff === 1 ) return `${this.playerOne} adv`
        if ( diff === -1 ) return `${this.playerTwo} adv`
        if ( diff === 2 ) return `${this.playerOne} win`
        if ( diff === -2 ) return `${this.playerTwo} win`
    }
}

module.exports = { Tennis }
