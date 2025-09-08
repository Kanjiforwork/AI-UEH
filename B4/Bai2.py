from simpleai.search import SearchProblem, astar

class QueensProblem(SearchProblem):
    def __init__(self, n=8):
        self.n = n
        super().__init__(initial_state=())
    
    def actions(self, state):
        if len(state) >= self.n:
            return []
        return list(range(self.n))
    
    def result(self, state, action):
        return state + (action,)
    
    def is_goal(self, state):
        return len(state) == self.n and self.is_valid(state)
    
    def is_valid(self, state):
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j]:
                    return False
                if abs(i - j) == abs(state[i] - state[j]):
                    return False
        return True
    
    def heuristic(self, state):
        conflicts = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j] or abs(i-j) == abs(state[i]-state[j]):
                    conflicts += 1
        return conflicts + (self.n - len(state))

# Giải bằng A*
problem = QueensProblem(8)
result = astar(problem)

# ← THÊM PHẦN NÀY để in kết quả!
print("Nghiệm A*:", result.state)
print("Đường đi:", result.path())

# In bàn cờ trực quan
def print_board(solution, n=8):
    print(f"\n🏁 Bàn cờ {n}x{n}:")
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    for row in range(n):
        col = solution[row]
        board[row][col] = '♛'
    
    print("   ", end="")
    for col in range(n):
        print(f" {col}", end="")
    print()
    
    for row in range(n):
        print(f"{row}: ", end="")
        for col in range(n):
            print(f" {board[row][col]}", end="")
        print()

print_board(result.state)
