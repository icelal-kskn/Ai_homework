import random
from simpleai.search import SearchProblem, astar, breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, uniform_cost, greedy
from simpleai.search.viewers import BaseViewer
import inspect
from math import sqrt

#class definition for NQueens
class NQueens(SearchProblem):

    def __init__(self, N):
        self.N=N
        self.state=self._set_state()
        super().__init__(initial_state=self.state)
        self.visited_states = set([])

    def __str__(self):
        return f"State: {self.state}"
      
    def _set_state(self):
        return self.generate_random_state()
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
        for i,letter in enumerate(state):
            if ord(letter)> ord('1') and ord(letter)<ord(str(self.N)):
                upper_letter = chr(ord(letter) - 1)
                lower_letter = chr(ord(letter) + 1)
                upper_state = state[:i] + upper_letter + state[i+1:]
                lower_state = state[:i] + lower_letter + state[i+1:]
                if lower_state not in self.visited_states:
                    possible_actions.append((i,lower_letter))
                if upper_state not in self.visited_states:
                    possible_actions.append((i,upper_letter))
            elif letter == '1':
                lower_letter = chr(ord(letter) + 1)
                lower_state = state[:i] + lower_letter + state[i+1:]
                if lower_state not in self.visited_states:
                    possible_actions.append((i,lower_letter))
            elif letter == str(self.N):
                upper_letter = chr(ord(letter) - 1)
                upper_state = state[:i] + upper_letter + state[i+1:]
                if upper_state not in self.visited_states:
                    possible_actions.append((i,upper_letter))
        return possible_actions

    def result(self, state, action):
        if action:
            column, new_row = action
            new_state = list(state)
            new_state[column] = new_row
            final_output = ''.join(new_state)
            self.visited_states.add(final_output)
            return final_output
        else:
            return state

    def is_goal(self, state):
        # Returns whether the state given as a parameter is a goal state
        return self._count_attacking_pairs(state) == 0

    def heuristic(self, state):
        # Returns the estimated solution cost from the given state to the goal state
        return int(sqrt(self._count_attacking_pairs(state)))

    def cost(self, state1, action, state2):
        return 1



def test_algorithm(algorithm, N, initial_state):
    problem = NQueens(N)
    viewer = BaseViewer()  

    print(f"\nTesting {algorithm.__name__} with N={N} and initial state: {initial_state}")
    if "depth_limit" not in inspect.signature(algorithm).parameters:
        result = algorithm(problem, viewer=viewer)
        print("Algorithm:", algorithm.__name__)
        print("Resulting State:", *[result.state if result.state != None else "Not Found"])
        print("Resulting Path:", result.path())
        print("Cost of Solution:", result.cost)
    else:
        result = algorithm(problem,1000, viewer=viewer)
        print("Algorithm:", algorithm.__name__)
        print("Resulting State:", *[result.state if result.state != None else "Not Found"])
        print("Resulting Path:", result.path())
        print("Cost of Solution:", result.cost)

search_functions = [astar, breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, uniform_cost, greedy]
initial_states = ["2323", "4311", "3442", "12345", "13154", "536142", "532512"]

for func in search_functions:
    for state in initial_states:
        print(test_algorithm(func, len(state),state ))
