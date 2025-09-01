from db import Session, Player, GameSession
from game import run_game

session = Session()

def main_menu():
    while True:
        print("\nDino Game ")
        print("====================")
        print("1. Add Player")
        print("2. View Players")
        print("3. Start Game")
        print("4. Leaderboard")
        print("5. Quit")

        choice = input("Enter choice: ")