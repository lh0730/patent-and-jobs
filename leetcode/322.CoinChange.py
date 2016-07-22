class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #BFS
        if amount == 0:
            return 0
        valuea = [0]
        valueb = []
        buffer = [True]
        buffer = buffer + amount*[False]
        count = 0
        while valuea:
            count = count + 1
            for i in valuea:
                for coin in coins:
                    value = i + coin
                    if value == amount:
                        return count
                    elif value > amount:
                        continue
                    elif not buffer[value]:
                        buffer[value] = True
                        valueb.append(value)
            valuea, valueb = valueb, []
        return -1
