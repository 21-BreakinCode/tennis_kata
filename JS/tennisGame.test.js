const { Tennis } = require('./tennisGame')

test('love all', () => {
    const TennisGame = new Tennis()
    const expected = 'love all'

    TennisGame.playerOneScore(0)
    TennisGame.playerTwoScore(0)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('fifteen love', () => {
    const TennisGame = new Tennis()
    const expected = 'fifteen love'

    TennisGame.playerOneScore(1)
    TennisGame.playerTwoScore(0)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('thirty love', () => {
    const TennisGame = new Tennis()
    const expected = 'thirty love'

    TennisGame.playerOneScore(2)
    TennisGame.playerTwoScore(0)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('forty love', () => {
    const TennisGame = new Tennis()
    const expected = 'forty love'

    TennisGame.playerOneScore(3)
    TennisGame.playerTwoScore(0)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('player one win', () => {
    const TennisGame = new Tennis('Ken', 'Joe')
    const expected = 'Ken win'

    TennisGame.playerOneScore(4)
    TennisGame.playerTwoScore(0)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('love fifteen', () => {
    const TennisGame = new Tennis()
    const expected = 'love fifteen'

    TennisGame.playerOneScore(0)
    TennisGame.playerTwoScore(1)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('love thirty', () => {
    const TennisGame = new Tennis()
    const expected = 'love thirty'

    TennisGame.playerOneScore(0)
    TennisGame.playerTwoScore(2)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('love forty', () => {
    const TennisGame = new Tennis()
    const expected = 'love forty'

    TennisGame.playerOneScore(0)
    TennisGame.playerTwoScore(3)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('fifteen all', () => {
    const TennisGame = new Tennis()
    const expected = 'fifteen all'

    TennisGame.playerOneScore(1)
    TennisGame.playerTwoScore(1)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('thirty all', () => {
    const TennisGame = new Tennis()
    const expected = 'thirty all'

    TennisGame.playerOneScore(2)
    TennisGame.playerTwoScore(2)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('player two win', () => {
    const TennisGame = new Tennis('Ken', 'Joe')
    const expected = 'Joe win'

    TennisGame.playerOneScore(0)
    TennisGame.playerTwoScore(4)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('Deuce', () => {
    const TennisGame = new Tennis()
    const expected = 'deuce'

    TennisGame.playerOneScore(3)
    TennisGame.playerTwoScore(3)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('Deuce over forty', () => {
    const TennisGame = new Tennis()
    const expected = 'deuce'

    TennisGame.playerOneScore(6)
    TennisGame.playerTwoScore(6)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('Adv player one', () => {
    const TennisGame = new Tennis('Joe', 'Ken')
    const expected = 'Joe adv'

    TennisGame.playerOneScore(4)
    TennisGame.playerTwoScore(3)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('Adv player two', () => {
    const TennisGame = new Tennis('Joe', 'Ken')
    const expected = 'Ken adv'

    TennisGame.playerOneScore(5)
    TennisGame.playerTwoScore(6)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('Win player one', () => {
    const TennisGame = new Tennis('Joe', 'Ken')
    const expected = 'Joe win'

    TennisGame.playerOneScore(5)
    TennisGame.playerTwoScore(3)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})

test('Win player two', () => {
    const TennisGame = new Tennis('Joe', 'Ken')
    const expected = 'Ken win'

    TennisGame.playerOneScore(5)
    TennisGame.playerTwoScore(7)

    expect(
        TennisGame.getScore()
    ).toBe(expected)
})
