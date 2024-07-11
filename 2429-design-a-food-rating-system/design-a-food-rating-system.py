import heapq
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.counter = {}
        self.ranker = {}
        self.matcher = {}
        self.food = {}

        for i in range(len(foods)):

            curr_rating = ratings[i]
            curr_food = foods[i]
            curr_cuisine = cuisines[i]

            if curr_cuisine in self.ranker:
                if (curr_cuisine, curr_rating) in self.counter:
                    self.counter[(curr_cuisine, curr_rating)] += 1
                    heapq.heappush(self.matcher[(curr_cuisine, curr_rating)], curr_food )
                else:
                    heapq.heappush(self.ranker[curr_cuisine], -curr_rating)
                    self.counter[(curr_cuisine, curr_rating)] = 1
                    self.matcher[(curr_cuisine, curr_rating)] = []
                    heapq.heappush(self.matcher[(curr_cuisine, curr_rating)], curr_food)
                    
            else:
                self.ranker[curr_cuisine] = []

                heapq.heappush(self.ranker[curr_cuisine], -curr_rating)

                self.counter[(curr_cuisine, curr_rating)] = 1

                self.matcher[(curr_cuisine, curr_rating)] = []

                heapq.heappush(self.matcher[(curr_cuisine, curr_rating)], curr_food)

            self.food[curr_food] = [curr_cuisine, curr_rating]
            


        
    def changeRating(self, food: str, newRating: int) -> None:
        curr_food  = food
        if newRating == self.food[curr_food][1]:
            return
        
        prev_rating = self.food[curr_food][1]
        curr_cuisine = self.food[curr_food][0]

        self.counter[(curr_cuisine, prev_rating)] -= 1

        if self.counter[(curr_cuisine, prev_rating)] == 0:
            del self.counter[(curr_cuisine, prev_rating)]
            del self.matcher[(curr_cuisine, prev_rating)]

        if (curr_cuisine, newRating) in self.counter:
            self.counter[(curr_cuisine,newRating)] += 1
            heapq.heappush(self.matcher[(curr_cuisine, newRating)], curr_food)

        else:
            self.counter[(curr_cuisine, newRating)] = 1
            self.matcher[(curr_cuisine, newRating)] = []
            heapq.heappush(self.matcher[(curr_cuisine, newRating)], curr_food)
            heapq.heappush(self.ranker[curr_cuisine], -newRating)

        self.food[curr_food][1] = newRating
         




    def highestRated(self, cuisine: str) -> str:
        
        while self.ranker[cuisine]:
            curr_rating = -heapq.heappop(self.ranker[cuisine])
            if (cuisine,curr_rating) in self.counter and self.counter[(cuisine,curr_rating)] > 0:
                heapq.heappush(self.ranker[cuisine], -curr_rating)
                while self.matcher[(cuisine, curr_rating)]:
                    curr_food = heapq.heappop(self.matcher[(cuisine, curr_rating)])
                    if self.food[curr_food][1] == curr_rating:
                        heapq.heappush(self.matcher[(cuisine, curr_rating)], curr_food)
                        return curr_food

        return '' 
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)