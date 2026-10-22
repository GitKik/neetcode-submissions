class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list()
        fleets = 0
        for p, s in zip(position, speed):
            cars.append((p, s))
        cars = sorted(cars, key=lambda tup: tup[0] , reverse=True)
        print(cars)
        time_to_target = list()
        for car in cars :
            time_to_target.append((target - car[0]) / car[1])
        target_min = 0
        for t in time_to_target :
            if t > target_min :
                fleets += 1 
                target_min = t 
        return fleets

