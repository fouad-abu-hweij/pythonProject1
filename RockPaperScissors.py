#This code have been written by:
#Fouad Abu Hweij //(202210103)
#Nour Rahhal //(202210055)

#Rock , Paper , and Scissors Game

'''
Rock , Paper , and Scissors is a hand game played by a player Vs a computer.
 Each player chooses one of the following shapes : “rock”,” paper”, or “scissors”.
 In Addition, the player chooses the amount of rounds to play.

Requirements:
•	Ask for how many rounds the game will be.
•	Start each round Player vs Computer
•	Show the winner for each round
•	If computer wins the round you will hear a sound , and a red screen will appear
•	If  you win the round you will hear a sound, and a green screen will appear
•	If it's a draw you will hear a sound , and a yellow screen will appear
•	After all rounds . it's going to display “+++ G A M E  O V E R +++” then print game results ,then
    Game result will be stored in a file named (data.txt) , and then ask The user if He/She wants to play again.
'''


import tkinter as t
import winsound,random
from tkinter import simpledialog, messagebox,font



class Game1:

    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.player_score = 0
        self.computer_score = 0
        self.draw = 0
        self.options = {'rock': 1, 'paper': 2, 'scissors': 3}
        self.results = {1: 'Player wins!', 2: 'Computer wins!', 3: 'It\'s a tie!'}
        self.game_results = []

    def player_ch(self, player_option):
        computer_option = random.choice(list(self.options.values()))
        player_value = self.options[player_option]

        round_result = self.find_winner(player_value, computer_option)
        self.update_sc(round_result)

    def find_winner(self, player_value, computer_value):

        if player_value == computer_value:
         return 3
        elif (player_value - computer_value) % 3 == 1:
            return 1
        else:
             return 2

    def update_sc(self, round_result):

        global player_score, computer_score

        if round_result == 1:
              self.color = 'green'
              self.player_score += 1
              m.config(bg='green')
              winsound.Beep(520, 1000)


        elif round_result == 2:
         self.color = 'red'
         self.computer_score += 1
         m.config(bg='red')

         winsound.Beep(200, 1000)
        elif round_result ==3:
            self.color = '#008B8B'
            self.draw+=1
            m.config(bg='yellow')
            winsound.Beep(350, 1000)

        player_score_label.config(text=f'Your Score: {self.player_score}')

        computer_score_label.config(text=f'Computer Score: {self.computer_score}')



        winner_label.config(text=self.results[round_result], fg=self.color,bg='black')

        if self.player_score + self.computer_score+self.draw == self.total_rounds:
         self.save_game_results()
         self.display_game_results()

    def save_game_results(self):

        result = "+++ G A M E  O V E R +++"

        self.game_results.append(result)

        fh=open("data.txt", "a")
        fh.write(result + "\n")
        fh.close()

    def display_game_results(self):
        m.config(bg='white')
        final_results = self.show_final_results()
        messagebox.showinfo("Game Over", self.game_results[-1] + final_results)

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:

            self.reset_game()
        else:
         m.destroy()

    def show_final_results(self):

        if self.player_score > self.computer_score:
         final="Player"
        elif self.computer_score > self.player_score:
             final="Computer"
        elif self.computer_score == self.player_score:
          final="No Winner , it's a Draw"

        re = (
            f"\nGame Rounds: {self.total_rounds}\n"
            f"Player won times: {self.player_score}\n"
            f"Computer won times: {self.computer_score}\n"
            f"Draw times: {self.draw}\n"
            f"Final Winner: {final}\n"
        )

        fh = open("data.txt", "a")
        fh.write(re + "\n")
        fh.close()

        return re

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.draw = 0

        player_score_label.config(text='Your Score: -')
        computer_score_label.config(text='Computer Score: -')
        m.config(bg='white')
        self.total_rounds = int(simpledialog.askstring("Number of Rounds", "Enter the number of rounds:"))
        winner_label.config(text="Let's Start the Game...", fg='black',bg='#9E9E9E')

class GUI:
    def __init__(self):
        self.game = None

    def set(self):
        global m, winner_label, player_score_label, computer_score_label

        m = t.Tk()
        m.title("Rock Paper Scissors Game")
        m.config(bg='white')
        afont = font.Font(size=12)

        inp = t.Frame(m)
        inp.pack()


        titlee = t.Label(inp,text='Rock Paper Scissors',font=font.Font(size=20, weight='bold'), fg='black',bg='#9E9E9E')
        titlee.grid(row=1, columnspan=3, pady=10)

        r_btn = t.Button(inp, text='Rock', width=15, bd=0, bg='#e74c3c', pady=10, fg='white',font=font.Font(font=afont,size=12, weight='bold'), command=lambda: self.game.player_ch('rock'))
        r_btn.grid(row=2, column=0, padx=10)

        p_btn = t.Button(inp, text='Paper', width=15, bd=0, bg='#2ecc71', pady=10, fg='white',font=font.Font(font=afont,size=12, weight='bold'), command=lambda: self.game.player_ch('paper'))
        p_btn.grid(row=2, column=1, padx=10)

        s_btn = t.Button(inp, text='Scissors', width=15, bd=0, bg='#3498db', pady=10, fg='white',font=font.Font(font=afont,size=12, weight='bold'), command=lambda: self.game.player_ch('scissors'))
        s_btn.grid(row=2, column=2, padx=10)

        res_frame = t.Frame(m)
        res_frame.pack(pady=20)

        winner_label = t.Label(res_frame, text="Let's Start the Game...", fg='black',bg='#9E9E9E',font=font.Font(size=16, weight='bold'))
        winner_label.grid(row=1, columnspan=3, pady=10)

        sc_frame = t.Frame(m)
        sc_frame.pack()

        player_score_label = t.Label(sc_frame, text='Player Score : ',  fg='black',bg='#9E9E9E',font=font.Font(font=afont,size=12, weight='bold'))
        player_score_label.grid(row=0, column=0, padx=20)

        computer_score_label = t.Label(sc_frame, text='Computer Score : ',fg='black',bg='#9E9E9E',font=font.Font(font=afont,size=12, weight='bold'))
        computer_score_label.grid(row=0, column=1, padx=20)

        m.geometry('500x255')
        m.protocol("WM_DELETE_WINDOW", self.on_close)
        m.mainloop()

    def on_close(self):
        self.game.display_game_results()

if __name__ == "__main__":
    rounds = int(simpledialog.askstring("Number of Rounds", "Enter the number of rounds:"))
    game_in = Game1(rounds)
    g2 = GUI()
    g2.game = game_in
    g2.set()

