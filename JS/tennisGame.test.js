const { Tennis } = require('./tennisGame')

test('love all', () => {
    const tennis = new Tennis()
    const result = 'love all'

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('fifteen love', () => {
    const tennis = new Tennis()
    const result = 'fifteen love'

    tennis.setOneScore(1)
    tennis.setTwoScore(0)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('thirty love', () => {
    const tennis = new Tennis()
    const result = 'thirty love'

    tennis.setOneScore(2)
    tennis.setTwoScore(0)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('forty love', () => {
    const tennis = new Tennis()
    const result = 'forty love'

    tennis.setOneScore(3)
    tennis.setTwoScore(0)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('love fifteen', () => {
    const tennis = new Tennis()
    const result = 'love fifteen'

    tennis.setOneScore(0)
    tennis.setTwoScore(1)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('love thirty', () => {
    const tennis = new Tennis()
    const result = 'love thirty'

    tennis.setOneScore(0)
    tennis.setTwoScore(2)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('love forty', () => {
    const tennis = new Tennis()
    const result = 'love forty'

    tennis.setOneScore(0)
    tennis.setTwoScore(3)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('deuce', () => {
    const tennis = new Tennis()
    const result = 'deuce'

    tennis.setOneScore(3)
    tennis.setTwoScore(3)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('deuce over forty', () => {
    const tennis = new Tennis()
    const result = 'deuce'

    tennis.setOneScore(5)
    tennis.setTwoScore(5)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('adv player one', () => {
    const tennis = new Tennis('Joe', 'Ken')
    const result = 'Joe adv'

    tennis.setOneScore(4)
    tennis.setTwoScore(3)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('adv player two', () => {
    const tennis = new Tennis('Joe', 'Bob')
    const result = 'Bob adv'

    tennis.setOneScore(4)
    tennis.setTwoScore(5)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('player one win before deuce', () => {
    const tennis = new Tennis('A', 'B')
    const result = 'A win'

    tennis.setOneScore(4)
    tennis.setTwoScore(2)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('player two win before deuce', () => {
    const tennis = new Tennis('A', 'B')
    const result = 'B win'

    tennis.setOneScore(2)
    tennis.setTwoScore(4)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('player one win after deuce', () => {
    const tennis = new Tennis('A', 'B')
    const result = 'A win'

    tennis.setOneScore(7)
    tennis.setTwoScore(5)

    expect(
        tennis.getScore()
    ).toBe(result)
})

test('player two win after deuce', () => {
    const tennis = new Tennis('A', 'B')
    const result = 'B win'

    tennis.setOneScore(5)
    tennis.setTwoScore(7)

    expect(
        tennis.getScore()
    ).toBe(result)
})