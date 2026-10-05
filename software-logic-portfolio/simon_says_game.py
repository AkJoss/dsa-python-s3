# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:12:42 2024

@author: José Alberto Rocha Munguía
"""
import tkinter as tk
from tkinter import messagebox
import random

# Define RGB colors
colors_rgb = {
    'Red': (255, 0, 0),
    'Green': (0, 255, 0),
    'Blue': (0, 0, 255),
    'Yellow': (255, 255, 0)
}

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

class SimonSays:
    def __init__(self, window):
        self.window = window
        self.window.title("Simon Says")
        self.window.geometry("500x550")
        
        self.colors = list(colors_rgb.keys())
        self.game_sequence = []
        self.player_sequence = []
        self.waiting_for_input = False
        self.round = 1
        self.sequence_index = 0
        
        self.create_interface()
    
    def create_interface(self):
        self.round_label = tk.Label(self.window, text=f"Round {self.round}", font=('Arial', 20))
        self.round_label.pack(pady=20)
        
        self.display_area = tk.Label(self.window, bg='grey', width=20, height=5)
        self.display_area.pack(pady=10)
        
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=10)
        
       
        for i, color in enumerate(self.colors):
            btn = tk.Button(
                self.button_frame,
                text=color,
                bg=rgb_to_hex(colors_rgb[color]),
                width=12,
                height=3,
                command=lambda c=color: self.button_click(c)
            )
            btn.grid(row=0, column=i, padx=5)
            
        self.start_button = tk.Button(self.window, text='Start Game :D', command=self.show_sequence)
        self.start_button.pack(pady=20)
        
    def show_sequence(self):
        self.waiting_for_input = False
        self.player_sequence.clear()
        self.game_sequence.append(random.choice(self.colors))
        self.round_label.config(text=f'Round {self.round}')
        self.start_button.config(state='disabled')
        self.sequence_index = 0
        self.window.after(500, self.play_sequence)
        
    def play_sequence(self):
        if self.sequence_index < len(self.game_sequence):
            color = self.game_sequence[self.sequence_index]
            self.display_area.config(bg=rgb_to_hex(colors_rgb[color]))
            self.window.update() 
            self.window.after(800, self.turn_off_color)
        else:
            self.display_area.config(bg='grey')
            self.window.update()
            self.window.after(300, self.start_player_input)
            
    def turn_off_color(self):
        self.display_area.config(bg='grey')
        self.window.update()
        self.sequence_index += 1
        self.window.after(400, self.play_sequence)
        
    def start_player_input(self):
        self.waiting_for_input = True
        messagebox.showinfo("Your Turn", "Repeat the sequence!")
        
    def button_click(self, color_name):
        if self.waiting_for_input:
            self.player_sequence.append(color_name)
            current_idx = len(self.player_sequence) - 1
            
            if self.player_sequence[current_idx] != self.game_sequence[current_idx]:
                messagebox.showerror("Error", "Game Over!")
                self.reset_game()
            elif len(self.player_sequence) == len(self.game_sequence):
                self.round += 1
                messagebox.showinfo("Correct", "Moving to the next round!")
                self.window.after(1000, self.show_sequence)
                
    def reset_game(self):
        self.game_sequence.clear()
        self.player_sequence.clear()
        self.round = 1
        self.start_button.config(state='normal')
        self.round_label.config(text=f"Round {self.round}")
        
if __name__ == "__main__":
    root = tk.Tk()
    game = SimonSays(root)
    root.mainloop()