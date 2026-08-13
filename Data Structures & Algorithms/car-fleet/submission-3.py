class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        targettime = []
        if not position:
            return (0)
        cars = sorted(zip(position, speed), reverse = True)
        #Time:  O(n log n)
        #Space: O(n)
        result = 1
        for i in range(len(position)):
            time = (target - cars[i][0]) / cars[i][1]
            #time = (target-position)/time
            if not targettime:
                targettime.append(time)
            elif time > targettime[-1]:
                result += 1
                targettime.append(time)
            
        return (result)