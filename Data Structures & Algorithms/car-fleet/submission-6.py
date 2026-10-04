class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse=True)
        time = [(target - cars[i][0]) / cars[i][1] for i in range(len(cars))]
        currTime = time[0]
        numFleets = 1


        for i in range(len(cars)):
            if(time[i] <= currTime):
                continue
            else:
                currTime = time[i]
                numFleets += 1
        

        return numFleets
