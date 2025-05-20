def get_player_choice(player_name):
    while True:
        try:
            choice = input(f"{player_name}, enter your choice (rock, paper, scissors): ").lower()
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            print("Invalid choice! Please choose rock, paper, or scissors.")
        except EOFError:
            print("Input error! Please try again.")
            continue

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
         (player1_choice == 'paper' and player2_choice == 'rock') or \
         (player1_choice == 'scissors' and player2_choice == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        # Get choices from both players
        player1_choice = get_player_choice("Player 1")
        if not player1_choice:  # In case EOFError handling returns None
            break
        player2_choice = get_player_choice("Player 2")
        if not player2_choice:
            break
        
        # Show choices
        print(f"\nPlayer 1 chose: {player1_choice}")
        print(f"Player 2 chose: {player2_choice}")
        
        # Determine and display the winner
        result = determine_winner(player1_choice, player2_choice)
        print(result)
        
        # Ask if players want to play again
        try:
            play_again = input("\nDo you want to play another round? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break
        except EOFError:
            print("Thanks for playing!")
            break

# Start the game
rock_paper_scissors()
