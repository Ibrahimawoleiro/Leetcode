class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into a list of tuples
        cars = sorted(zip(position, speed), reverse=True)
        
        # Calculate the time it takes for each car to reach the target
        times = [(target - p) / s for p, s in cars]

        fleets = 0
        current_time = 0

        for time in times:
            if time > current_time:
                fleets += 1
                current_time = time

        return fleets