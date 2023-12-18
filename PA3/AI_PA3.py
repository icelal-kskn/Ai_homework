import random
from simpleai.search import SearchProblem, astar, breadth_first, depth_first
from simpleai.search.viewers import BaseViewer


#class definition for NQueens
class NQueens(SearchProblem):

    def __init__(self, N):
        self.N=N
        self.state=self._set_state()
        super().__init__(initial_state=self.state)

    def __str__(self):
        return f"State: {self.state}"
      
    def _set_state(self):
        return self.generate_random_state()
    
    #TODO  SetState is disabled please close the test and open the following codes using Ctrl+K+C or Ctrl+Ö 
        
        # choice = input("Manually enter state (M) or generate a random state (R)? ").strip().lower()
        # if choice.upper() == 'M':
        #     state = input(f"Enter a state of length {self.N}: ").strip()
        #     if self._is_valid(state):
        #         return state
        #     else:
        #         print("Invalid state. Please try again.")
        #         return self._set_state()
        # elif choice.upper() == 'R':
        #     return self.generate_random_state()
        # else:
        #     print("Invalid choice. Please enter 'M' or 'R'.")
        #     return self._set_state()   
        
    def generate_random_state(self):
        while True:
            state = ''.join(str(random.randint(1, self.N)) for _ in range(self.N))
            if self._is_valid(state):
                return state  

    def _is_valid(self,state):
        #Case 1
        if not state.isdigit():
            return False
        #Case 2
        if len(state) != self.N:
            return False
        #Case 3
        if any(int(row) < 0 or int(row) > self.N for row in state):
            return False 
        return True  
  
    def _count_attacking_pairs(self, state):
        count = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if state[i] == state[j] or abs(int(state[i]) - int(state[j])) == abs(i - j):
                    count += 1
        return count
    
    def actions(self, state):
        # Returns a list of possible actions from the current state
        possible_actions = []
        for i in range(self.N):
            for j in range(1, self.N + 1):
                if str(j) != state[i]:
                    possible_actions.append((i, str(j)))
        return possible_actions

    def result(self, state, action):
        column, new_row = action
        new_state = list(state)
        new_state[column] = new_row
        return ''.join(new_state)

    def is_goal(self, state):
        # Returns whether the state given as a parameter is a goal state
        return self._count_attacking_pairs(state) == 0

    def heuristic(self, state):
        # Returns the estimated solution cost from the given state to the goal state
        return self._count_attacking_pairs(state)

    def cost(self, state1, action, state2):
        return 1



def test_algorithm(algorithm, N, initial_state):
    problem = NQueens(N)
    viewer = BaseViewer()  

    print(f"\nTesting {algorithm} with N={N} and initial state: {initial_state}")
    if algorithm == astar or algorithm == breadth_first or algorithm == depth_first:
        result = algorithm(problem, viewer=viewer)
        print("Algorithm:", algorithm)
        print("Resulting State:", result.state)
        print("Resulting Path:", result.path())
        print("Cost of Solution:", result.cost)
        print("Viewer Statistics:", viewer.stats)
    else:
        print("Invalid algorithm choice.")


initial_states = ["2323", "4311", "3442", "12345", "13154", "536142", "532512"]

# Test each algorithm for initial states
for initial_state in initial_states:
    N = len(initial_state)
    test_algorithm(astar, N, initial_state)

for initial_state in initial_states:
    N = len(initial_state)
    test_algorithm(breadth_first, N, initial_state)

for initial_state in initial_states:
    N = len(initial_state)
    test_algorithm(depth_first, N, initial_state)
