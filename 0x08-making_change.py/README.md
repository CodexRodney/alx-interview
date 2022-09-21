# MAKING CHANGES INTERVIEW QUESTION
- Given  a pile of different coins, one should determine the fewest
number of coins needed to meet a given amount 
	* FUNCTION PROTOTYPE
		def makeChange(coins, total)
	* RETURN
		the fewest number of coins needed to meet total
		if total is 0 or less return 0
		if total cannot be met by any number of coins you have, return -1
	* coins is a list of the values of the coins in your possesion
	* the value of a coin will always be an interger greater than 0
	* You caassume ypu have an infinite number of each denomination of coin in the list
