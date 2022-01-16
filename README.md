# TableTennis

Table Tennis Scoring
1. There are two players in the game.
2. Every player gets to serve twice in a row.
3. The first to 11 points is declared the winner.
4. If the points are tied at 10-10, a player then has to strive for a two-point lead to win the game.
5. If the scores are tied at 20-20, the first player to reach 21 point wins the game
Assume each player winning the point randomly. If the random functions returns even, then first player wins the
point, if it returns odd, the second player wins the point
Display the score and the winning player

Output:

Automated test run with Match with 3 sets:
```
Teams playing match are: Team-A, Team-B
Number of sets in match: 3
Score required to win set: 11
Match started ........


------- Playing Set 1 -------
True
Points after each serve: Team-A: 1 	 Team-B: 0
True
Points after each serve: Team-A: 2 	 Team-B: 0
False
Points after each serve: Team-A: 2 	 Team-B: 1
False
Points after each serve: Team-A: 2 	 Team-B: 2
True
Points after each serve: Team-A: 3 	 Team-B: 2
True
Points after each serve: Team-A: 3 	 Team-B: 3
False
Points after each serve: Team-A: 4 	 Team-B: 3
False
Points after each serve: Team-A: 5 	 Team-B: 3
True
Points after each serve: Team-A: 5 	 Team-B: 4
True
Points after each serve: Team-A: 5 	 Team-B: 5
False
Points after each serve: Team-A: 5 	 Team-B: 6
False
Points after each serve: Team-A: 5 	 Team-B: 7
True
Points after each serve: Team-A: 5 	 Team-B: 8
True
Points after each serve: Team-A: 5 	 Team-B: 9
False
Points after each serve: Team-A: 5 	 Team-B: 10
False
Points after each serve: Team-A: 5 	 Team-B: 11

** Team Team-B has won set with points (11, 5) **
------- Set 1 Completed -------

------- Playing Set 2 -------
True
Points after each serve: Team-A: 0 	 Team-B: 1
True
Points after each serve: Team-A: 0 	 Team-B: 2
False
Points after each serve: Team-A: 1 	 Team-B: 2
False
Points after each serve: Team-A: 2 	 Team-B: 2
True
Points after each serve: Team-A: 2 	 Team-B: 3
True
Points after each serve: Team-A: 2 	 Team-B: 4
False
Points after each serve: Team-A: 2 	 Team-B: 5
False
Points after each serve: Team-A: 3 	 Team-B: 5
True
Points after each serve: Team-A: 3 	 Team-B: 6
True
Points after each serve: Team-A: 4 	 Team-B: 6
False
Points after each serve: Team-A: 4 	 Team-B: 7
False
Points after each serve: Team-A: 5 	 Team-B: 7
True
Points after each serve: Team-A: 5 	 Team-B: 8
True
Points after each serve: Team-A: 5 	 Team-B: 9
False
Points after each serve: Team-A: 5 	 Team-B: 10
False
Points after each serve: Team-A: 6 	 Team-B: 10
True
Points after each serve: Team-A: 6 	 Team-B: 11

** Team Team-B has won set with points (11, 6) **
------- Set 2 Completed -------

--------------------Match Result--------------------
Team Name Set-1 Set-2 Set-3
Team-A     5     6     -
Team-B    11    11     -
------------------------------------------------------------

*** Match won by team : Team-B
*** Players in Team-B : Prashant 
*** Match won by score: ['11-5', '11-6'] 
```

```
Run unittests:
python3 -m unittest tests/NegativeTest.py tests/models/*Test.py tests/service/*Test.py
.....
Teams playing match are: Team-A, Team-B
Number of sets in match: 3
Score required to win set: 11
Match started ........


------- Playing Set 1 -------
True
Points after each serve: Team-A: 1 	 Team-B: 0
True
Points after each serve: Team-A: 2 	 Team-B: 0
False
Points after each serve: Team-A: 2 	 Team-B: 1
False
Points after each serve: Team-A: 3 	 Team-B: 1
True
Points after each serve: Team-A: 3 	 Team-B: 2
True
Points after each serve: Team-A: 4 	 Team-B: 2
False
Points after each serve: Team-A: 5 	 Team-B: 2
False
Points after each serve: Team-A: 6 	 Team-B: 2
True
Points after each serve: Team-A: 7 	 Team-B: 2
True
Points after each serve: Team-A: 8 	 Team-B: 2
False
Points after each serve: Team-A: 8 	 Team-B: 3
False
Points after each serve: Team-A: 8 	 Team-B: 4
True
Points after each serve: Team-A: 8 	 Team-B: 5
True
Points after each serve: Team-A: 9 	 Team-B: 5
False
Points after each serve: Team-A: 9 	 Team-B: 6
False
Points after each serve: Team-A: 9 	 Team-B: 7
True
Points after each serve: Team-A: 9 	 Team-B: 8
True
Points after each serve: Team-A: 10 	 Team-B: 8
False
Points after each serve: Team-A: 11 	 Team-B: 8

** Team Team-A has won set with points (11, 8) **
------- Set 1 Completed -------

------- Playing Set 2 -------
True
Points after each serve: Team-A: 0 	 Team-B: 1
True
Points after each serve: Team-A: 1 	 Team-B: 1
False
Points after each serve: Team-A: 2 	 Team-B: 1
False
Points after each serve: Team-A: 2 	 Team-B: 2
True
Points after each serve: Team-A: 3 	 Team-B: 2
True
Points after each serve: Team-A: 4 	 Team-B: 2
False
Points after each serve: Team-A: 4 	 Team-B: 3
False
Points after each serve: Team-A: 5 	 Team-B: 3
True
Points after each serve: Team-A: 6 	 Team-B: 3
True
Points after each serve: Team-A: 6 	 Team-B: 4
False
Points after each serve: Team-A: 6 	 Team-B: 5
False
Points after each serve: Team-A: 7 	 Team-B: 5
True
Points after each serve: Team-A: 7 	 Team-B: 6
True
Points after each serve: Team-A: 8 	 Team-B: 6
False
Points after each serve: Team-A: 8 	 Team-B: 7
False
Points after each serve: Team-A: 8 	 Team-B: 8
True
Points after each serve: Team-A: 9 	 Team-B: 8
True
Points after each serve: Team-A: 10 	 Team-B: 8
False
Points after each serve: Team-A: 10 	 Team-B: 9
False
Points after each serve: Team-A: 11 	 Team-B: 9

** Team Team-A has won set with points (11, 9) **
------- Set 2 Completed -------

--------------------Match Result--------------------
Team Name Set-1 Set-2 Set-3
Team-A    11    11     -
Team-B     8     9     -
------------------------------------------------------------

*** Match won by team : Team-A
*** Players in Team-A : Ashutosh 
*** Match won by score: ['11-8', '11-9'] 
............
----------------------------------------------------------------------
Ran 23 tests in 0.002s

OK
```
