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

        if choice == "1":
            name = input("Enter player name: ")
            if session.query(Player).filter_by(name=name):
                print(" Player already exists!")
            else:
                player = Player(name=name)
                session.add(player)
                session.commit()
                print(f"Player {name} added")
        
        elif choice == "2":
            players = session.query(Player).all()
            if not players:
                print("No players found.")
            for p in players:
                print(f"{p.id}. {p.name}")

        elif choice == "3":
            players = session.query(Player).all()
            if not players:
                print("No players available, add a player")
                continue

            print("\nSelect Player:")
            for p in players:
                print(f"{p.id}. {p.name}")

            try:
                player_id = int(input("Enter player ID: "))
                player = session.query(Player).get(player_id)
                if player:
                    score = run_game(player.name)
                    if score > player.score:
                        player.score = score
                    session.commit()
                    print(f"{player.name} finished with a score of {score}")
                else:
                    print("Invalid ID")
            except ValueError:
                print("Invalid input")

        elif choice == "4":
            scores = session.query(Player).order_by(Player.score.desc()).limit(5)
            print("\n Leaderboard:")
            for rank, p in enumerate(scores, start=1):
                print(f"{rank}. {p.name} — {p.score}")

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid choice!")