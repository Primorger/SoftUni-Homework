import tkinter as tk
from tkinter import messagebox

def create_matrix(row, col):
    return [[0 for _ in range(col)] for _ in range(row)]

def validate_col_choice(col, max_idx):
    if col < 0 or col > max_idx:
        raise ValueError(f"Column must be between 0 and {max_idx}")

def check_winner(matrix, row, col, player_num, slots_to_win):
    rows = len(matrix)
    cols = len(matrix[0])
    
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    for dr, dc in directions:
        count = 1
        
        r, c = row + dr, col + dc
        while 0 <= r < rows and 0 <= c < cols and matrix[r][c] == player_num:
            count += 1
            r += dr
            c += dc
        
        r, c = row - dr, col - dc
        while 0 <= r < rows and 0 <= c < cols and matrix[r][c] == player_num:
            count += 1
            r -= dr
            c -= dc
        
        if count >= slots_to_win:
            return True
    
    return False

def reset_board(matrix, labels, player_state):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for r in range(rows):
        for c in range(cols):
            matrix[r][c] = 0
            labels[r][c].config(bg="white")
    
    player_state["player_num"] = 1
    player_state["counter"] = 0

def update_button_colors(buttons, player_num):
    color = "lightcoral" if player_num == 1 else "lightblue"
    for btn in buttons:
        btn.config(bg=color)

def animate_fall(labels, col_num, target_row, player_num, matrix, rows, cols, slots_to_win, callback):
    color = "red" if player_num == 1 else "blue"
    current_row = 0
    
    def fall_step():
        nonlocal current_row
        
        if current_row > 0:
            labels[current_row - 1][col_num].config(bg="white")
        
        labels[current_row][col_num].config(bg=color)
        
        if current_row == target_row:
            matrix[target_row][col_num] = player_num
            callback()
        else:
            current_row += 1
            labels[current_row][col_num].after(50, fall_step)
    
    fall_step()

def handle_column_click(matrix, labels, col_num, player_num, counter, rows, cols, slots_to_win, buttons, player_state):
    try:
        validate_col_choice(col_num, cols - 1)
        
        row_num = None
        for r in range(rows - 1, -1, -1):
            if matrix[r][col_num] == 0:
                row_num = r
                break
        
        if row_num is None:
            messagebox.showwarning("Invalid Move", "This column is full!")
            return player_num, counter
        
        next_player = 2 if player_num == 1 else 1
        
        update_button_colors(buttons, next_player)
        
        for btn in buttons:
            btn.config(state='disabled')
        
        def after_animation():
            nonlocal counter
            
            counter += 1
            
            if check_winner(matrix, row_num, col_num, player_num, slots_to_win):
                messagebox.showinfo("Game Over", f"Player {player_num} wins!")
                reset_board(matrix, labels, player_state)
                update_button_colors(buttons, player_state["player_num"])
                for btn in buttons:
                    btn.config(state='normal')
                return
            
            if counter >= rows * cols:
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_board(matrix, labels, player_state)
                update_button_colors(buttons, player_state["player_num"])
                for btn in buttons:
                    btn.config(state='normal')
                return
            
            player_state["player_num"] = next_player
            player_state["counter"] = counter
            
            for btn in buttons:
                btn.config(state='normal')
        
        animate_fall(labels, col_num, row_num, player_num, matrix, rows, cols, slots_to_win, after_animation)
        
        return player_num, counter
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return player_num, counter

def create_ui(root, rows, cols, slots_to_win):
    matrix = create_matrix(rows, cols)
    labels = [[tk.Label(root, text=" ", width=4, height=2, bg="white", relief="solid", borderwidth=2) 
               for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            labels[r][c].grid(row=r + 1, column=c, padx=2, pady=2)

    player_state = {"player_num": 1, "counter": 0}

    buttons = []
    
    def on_click(column_num, p_state):
        handle_column_click(
            matrix, labels, column_num, p_state["player_num"], 
            p_state["counter"], rows, cols, slots_to_win, buttons, p_state
        )

    for col in range(cols):
        button = tk.Button(root, text="↓", width=3, height=1, bg="lightcoral", 
                          command=lambda c_idx=col: on_click(c_idx, player_state))
        buttons.append(button)
        button.grid(row=0, column=col, padx=2, pady=5)

def start_game():
    root = tk.Tk()
    root.title("Connect Four")

    rows, cols, slots_to_win = 6, 7, 4
    create_ui(root, rows, cols, slots_to_win)
    root.mainloop()

if __name__ == "__main__":
    start_game()