# Test Case design

1. Init game --> love all
   - `start game status`
2. player_one_fifteen --> fifteen love
   - `player_one.addScore()`
3. player_two_fifteen --> love fifteen
   - `player_two.addScore()`
4. two_players_fifteen_all --> fifteen all
   - `player_one.addScore(), player_two.addScore`
5. player_one_thirty --> thirty love
   - `player_one.addScore(2)`
6. player_two_thirty --> love thirty
   - `player_two.addScore(2)`
7. player_one_forty --> forty love
   - `player_one.addScore(3)`
8. player_two_forty --> love forty
   - `player_two.addScore(3)`
9. two_players_is_deuce --> Deuce
   - `player_one.addScore(3), player_two.addScore(3)`
10. player_advantage --> ${player_name} adv
    - `is_deuce() --> abs(player1.score - player2.score) == 1`
11. player_win --> ${player_name} win
    - `if not is_deuce() --> player#.score > 4`
    - `if is_deuce() --> abs(player1.score - player2.score) >= 2`