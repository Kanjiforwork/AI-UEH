from simpleai.search import CspProblem, backtrack
import time

def n_queens_csp(n=8):
    """
    Giải bài toán N quân hậu bằng CSP
    Variables: mỗi hàng có 1 quân hậu (Q0, Q1, Q2, ..., Q7)
    Domains: mỗi quân hậu có thể ở cột 0-7
    Constraints: không cùng cột, không cùng đường chéo
    """
    # Định nghĩa variables (mỗi hàng có 1 quân hậu)
    variables = [f'Q{i}' for i in range(n)]
    
    # Domain cho mỗi variable (cột 0 đến n-1)
    domains = {var: list(range(n)) for var in variables}
    
    
    # Constraint function
    def queens_constraint(variables_pair, values):
        """
        Kiểm tra 2 quân hậu có tấn công nhau không
        """
        var1, var2 = variables_pair
        col1, col2 = values
        
        # Lấy số hàng từ tên variable (Q0 -> hàng 0, Q1 -> hàng 1)
        row1 = int(var1[1:])
        row2 = int(var2[1:])
        
        # Không được cùng cột
        if col1 == col2:
            return False
            
        # Không được cùng đường chéo
        if abs(row1 - row2) == abs(col1 - col2):
            return False
            
        return True
    
    # Tạo constraints cho mọi cặp quân hậu
    constraints = []
    for i in range(n):
        for j in range(i + 1, n):
            constraint = ((f'Q{i}', f'Q{j}'), queens_constraint)
            constraints.append(constraint)
    
    # Tạo CSP problem
    problem = CspProblem(variables, domains, constraints)
    
    # Giải bằng backtracking
    solution = backtrack(problem)
    return solution

def print_board(solution, n=8):
    """In bàn cờ trực quan"""
    if solution is None:
        print("Không tìm thấy giải pháp!")
        return
        
    print(f"Tìm thấy nghiệm cho bài toán {n} quân hậu:")
    print("Vị trí các quân hậu:", solution)
    print("\nBàn cờ:")
    
    # Tạo bàn cờ trống
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    # Đặt quân hậu
    for row in range(n):
        col = solution[f'Q{row}']
        board[row][col] = '♛'
    
    # In bàn cờ với số hàng/cột
    print("   ", end="")
    for col in range(n):
        print(f" {col}", end="")
    print()
    
    for row in range(n):
        print(f"{row}: ", end="")
        for col in range(n):
            print(f" {board[row][col]}", end="")
        print()

def verify_solution(solution, n=8):
    """Kiểm tra tính đúng đắn của nghiệm"""
    if solution is None:
        return False
        
    positions = [solution[f'Q{i}'] for i in range(n)]
    
    # Kiểm tra mọi cặp quân hậu
    for i in range(n):
        for j in range(i + 1, n):
            row1, col1 = i, positions[i]
            row2, col2 = j, positions[j]
            
            # Cùng cột
            if col1 == col2:
                print(f"Lỗi: Q{i} và Q{j} cùng cột {col1}")
                return False
                
            # Cùng đường chéo
            if abs(row1 - row2) == abs(col1 - col2):
                print(f"Lỗi: Q{i} và Q{j} cùng đường chéo")
                return False
    
    print("Nghiệm hợp lệ!")
    return True

# Chạy chương trình chính
if __name__ == "__main__":
    print("GIẢI BÀI TOÁN 8 QUÂN HẬU BẰNG SIMPLEAI")
    print("=" * 50)
    
    start_time = time.time()
    
    # Giải bài toán
    solution = n_queens_csp(8)
    
    end_time = time.time()
    
    # In kết quả
    print_board(solution, 8)
    print(f"\nThời gian giải: {end_time - start_time:.4f} giây")
    
    # Kiểm tra nghiệm
    print("\nKiểm tra nghiệm:")
    verify_solution(solution, 8)
    
    print("\n" + "=" * 50)
    print("Thử với kích thước khác:")
    
    # Thử với 4x4
    print("\nBài toán 4 quân hậu:")
    solution_4 = n_queens_csp(4)
    print_board(solution_4, 4)
