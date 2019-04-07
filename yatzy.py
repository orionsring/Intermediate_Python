
def small_stright(dice):
    """ Score the given roll in the 'Small Straight' Yatzy category.
	
	Args:
	    dice: a sorted list of 5 integers indicating the dice rolled
	Returns:
	    an integer score
		
	>>> small_stright([1,2,3,4,5])
	15
	>>> small_stright([1,2,3,4,4])
	0
	
	This function only recognizes sorted lists, not other forms or collections:
	
	>>> small_stright({[1,2,3,4,5]})
	0
	>>> small_stright([5,4,3,2,1])
	0
			
	"""
    if dice == [1,2,3,4,5]:
        return sum(dice)
    else:
        return 0

		