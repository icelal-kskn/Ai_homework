# Mert Kardaş 200316045
# İkram Celal KESKİN 200316059
# Musa Sina ERTUĞRUL 200316011
import random
from simpleai.search import SearchProblem, astar, breadth_first, depth_first, genetic, hill_climbing, greedy
from simpleai.search.viewers import BaseViewer
from time import perf_counter

class NQueens(SearchProblem):
    def __init__(self,*, N:int =None, state=None):
        
        self.state = list()
        if state is None and isinstance(N, int): 
            if N > 0: 
                self.n = N
            else: 
                raise ValueError('N must be greater than 0 at least')
            print('How would you like to set the state?\n',
                'Type 1 for manually\n',
                'Type 2 for random size')
            input_ = input('Enter no:')
            if input_ == str(1):
                self._set_state()
            elif input_ == str(2):
                    self.state = self.generate_random_state()
        elif state is not None and len(state) == N or N is None: 
            self.n = len(state)
            self.state = state 
        
        else: 
            raise ValueError("Invalid arguments")
        
            
        super().__init__(initial_state=tuple(self.state))

    def __str__(self):
        return f'N = {self.n}, state = {self.state}'
   
    def _set_state(self):
        manual = input('put the queens: ')
        if self._is_valid(manual):
            for i in manual:
                self.state.append(int(i))
        else:
            print('Invalid state!!!')

    def generate_random_state(self)-> list:
    
        return [random.randint(1, self.n) for _ in range(self.n)]

    def _is_valid(self, state) -> bool:
        try:
            int(state)
        except ValueError:
            return False
        if len(state) != self.n:
            return False
        for i in state:
            if int(i) > self.n:
                return False
            if int(i) <= 0:
                return False
        return True

    def _count_attacking_pairs(self, state: list):
        att_pairs = 0
        for i in range(0, self.n - 1):
            for j in range(i + 1, self.n):
                if state[i] == state[j] or i - j == state[i] - state[j] or abs(i - j) == state[i] - state[j] :
                    att_pairs += 1
        return att_pairs

    def actions(self, state):
        possible_actions = []
        for i in range(self.n):
            for j in range(1, self.n + 1):
                if state[i] != j:
                    possible_actions.append(f'Queen collum {i + 1}, row {state[i]} is moved to row {j} ')
        return possible_actions
    
    def cost(self, state, action, state2):
        return 1
    
    def result(self, state, action):
        new_state = list(state)
        digits =[i for i in action if i.isdigit()]
        column_index = int(digits[0]) 
        new_row = int(digits[2]) 
        new_state[column_index -1] = new_row
        return tuple(new_state)

    
    def is_goal(self, state):
        if self._count_attacking_pairs(list(state)) == 0:
            print('Goal Node')
            return True
        
    def heuristic(self, state):
        return self._count_attacking_pairs(list(state))
    
    def value(self, state):
        return  -(self._count_attacking_pairs(state))

    def crossover(self, state1, state2):
        cut_point = random.randint(0,self.n -1)
        child = state1[:cut_point] + state2[cut_point:]
        return child
    
    def mutate(self, state):
        state = list(state)
        mut_point = random.randint(0,self.n -1)
        state[mut_point] = random.randint(1,self.n)
        return state 
         


 
class Testing: 
    def __init__(self, problem, iteration_limit=0): 
        self.problem= problem
        self.functions = [breadth_first, depth_first, astar, genetic, hill_climbing, greedy]
        self.viewer =BaseViewer()
        self.iteration_limit = iteration_limit
    
        
    def test(self): 
        for problem in self.problem:
            for function in self.functions:
                self._tester(problem, function)
                    
    def _tester(self, problem, func):
        if  func == hill_climbing: 
            start = perf_counter()
            test = func(problem, self.iteration_limit, self.viewer)
            finish = perf_counter()
        elif func ==genetic: 
            start = perf_counter()
            test = func(problem)
            finish = perf_counter()
        else:
            start = perf_counter()
            test = func(problem, graph_search=True, viewer=self.viewer)
            finish = perf_counter()
        
        print(f'''
            Function: {func}
            Initial state: {problem.state}
            Fİnal State: {test.state}
            Path: {test.path()}
            Cost: {test.cost}
            Stats: {self.viewer.stats}
            Execution Time: {(finish - start):.3f}s
        ''')
        print('-----------------------------------------------')
problems=[
    NQueens(state=[2,3,2,3]),
    NQueens(state=[4,3,1,1]),
    NQueens(state=[3,4,4,2]),
    NQueens(state=[1,2,3,4,5]),
    NQueens(state=[1,3,1,5,4])
]

test = Testing(problems, iteration_limit=10)
test.test()