"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are `n` stones in a pile. On each player's turn, that player
makes a _move_ consisting of removing **any** non-zero **square number** of
stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer `n`, return `true` if and only if Alice wins the game
otherwise return `false`, assuming both players play optimally.
"""
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        $$$
