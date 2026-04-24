class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        # NOTE: We are only selling ONE lemonade at a time

        for bill in bills:
            # It's either $5 $10 OR $20 we are given for a $5 charge
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            elif bill == 20 and ten > 0: # If we were given $20 (but have no tens)
                five -= 1
                ten -= 1
            else: # If we were given $20 (but have no tens)
                five -= 3
            if five < 0:
                return False
        
        return True

"""
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five > 0:
                    five -= 1
                else:
                    return False
            else:
                change = bill - 5
                if change == 15 and five > 0 and ten > 0:
                    ten -= 1
                    five -= 1
                elif change == 15 and five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
"""