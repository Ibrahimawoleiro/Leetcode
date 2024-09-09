class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        state = []
        """
        State Incoming
        ->      ->
        ->      <- Collision
        <-      <-
        <-      ->
        """
        for asteroid in asteroids:
            if state:
                #If the incoming asteroid is moving left
                if asteroid < 0:
                    if state[-1] < 0:
                        state.append(asteroid)
                    else:
                        while state[-1] > 0:
                            if state[-1] > abs(asteroid):
                                break
                            elif state[-1] == abs(asteroid):
                                state.pop()
                                break
                            else:
                                state.pop()
                                if not state or state[-1] < 0:
                                    state.append(asteroid)
                                    break
                #If the incoming asteroid is moving right
                else:
                        state.append(asteroid)
            else:
                state.append(asteroid)
        return state