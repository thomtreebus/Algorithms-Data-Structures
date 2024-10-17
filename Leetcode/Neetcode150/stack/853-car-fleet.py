class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = reversed(sorted([[p, s] for p, s in zip(position, speed)])) # sort by decreasing position
        fleets = []

        for car in cars:
            p, s = car
            remaining_time = (target - p) / s
            if len(fleets) == 0 or fleets[-1] < remaining_time:
                fleets.append(remaining_time)

        return len(fleets)