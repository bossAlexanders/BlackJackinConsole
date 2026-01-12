import random
import time
from typing import List, Tuple, Optional


def initialize_deck() -> List[Tuple[str, int]]:
    """
    Creates and returns a standard deck of cards with Russian names.
    
    Returns:
        List of tuples where each tuple contains (card_name, card_value).
    """
    return [
        ("Two of Spades", 2), ("Two of Hearts", 2), ("Two of Clubs", 2), ("Two of Diamonds", 2),
        ("Three of Clubs", 3), ("Three of Hearts", 3), ("Three of Diamonds", 3), ("Three of Spades", 3),
        ("Four of Spades", 4), ("Four of Diamonds", 4), ("Four of Clubs", 4), ("Four of Hearts", 4),
        ("Five of Spades", 5), ("Five of Diamonds", 5), ("Five of Clubs", 5), ("Five of Hearts", 5),
        ("Six of Spades", 6), ("Six of Hearts", 6), ("Six of Diamonds", 6), ("Six of Clubs", 6),
        ("Seven of Diamonds", 7), ("Seven of Spades", 7), ("Seven of Clubs", 7), ("Seven of Hearts", 7),
        ("Eight of Hearts", 8), ("Eight of Clubs", 8), ("Eight of Diamonds", 8), ("Eight of Spades", 8),
        ("Nine of Diamonds", 9), ("Nine of Hearts", 9), ("Nine of Clubs", 9), ("Nine of Spades", 9),
        ("Ten of Diamonds", 10), ("Ten of Spades", 10), ("Ten of Hearts", 10), ("Ten of Clubs", 10),
        ("Jack of Diamonds", 10), ("Jack of Hearts", 10), ("Jack of Clubs", 10), ("Jack of Spades", 10),
        ("Queen of Spades", 10), ("Queen of Diamonds", 10), ("Queen of Hearts", 10), ("Queen of Clubs", 10),
        ("King of Diamonds", 10), ("King of Spades", 10), ("King of Hearts", 10), ("King of Clubs", 10),
        ("Red Joker", 12), ("Black Joker", 12)
    ]


def draw_card(deck: List[Tuple[str, int]]) -> Optional[Tuple[str, int]]:
    """
    Draws a random card from the deck and removes it.
    
    Args:
        deck: The current deck of cards.
        
    Returns:
        A tuple (card_name, card_value) or None if deck is empty.
    """
    if deck:
        card = random.choice(deck)
        deck.remove(card)
        return card
    return None


def check_game_over(
    player_score: int, 
    bot_score: int, 
    player_stopped: bool, 
    bot_stopped: bool
) -> bool:
    """
    Checks if the game should end and prints the result.
    
    Args:
        player_score: Player's current score.
        bot_score: Bot's current score.
        player_stopped: Whether player has stopped drawing cards.
        bot_stopped: Whether bot has stopped drawing cards.
        
    Returns:
        True if game should end, False otherwise.
    """
    # Check for busts
    if player_score > 21:
        print("You busted! Bot wins!")
        return True
    
    if bot_score > 21:
        print("Bot busted! You win!")
        return True
    
    # Check if both players stopped
    if player_stopped and bot_stopped:
        print("Both players stopped drawing cards! Let's see the results...")
        if player_score > bot_score:
            print("You win!")
        elif bot_score > player_score:
            print("You lose!")
        else:
            print("It's a tie!")
        return True
    
    return False


def main() -> None:
    """
    Main function to run the Blackjack game against a bot.
    
    The game follows standard Blackjack rules where the goal is to get
    as close to 21 as possible without going over. The bot stops drawing
    at 17 points.
    """
    print("Welcome to Blackjack! Beat the bot!")
    
    # Initialize game state
    deck = initialize_deck()
    player_score = 0
    bot_score = 0
    player_stopped = False
    bot_stopped = False
    
    while True:
        # Player's turn
        if not player_stopped:
            choice = input("Draw a card? Yes/No: ").lower()
            if choice == "yes":
                card = draw_card(deck)
                if card:
                    print(f"You drew... {card[0]}")
                    player_score += card[1]
                    print(f"Your score: {player_score}")
            else:
                print("You decided to stop drawing cards...")
                player_stopped = True
        
        # Bot's turn
        if not bot_stopped:
            if bot_score <= 17:
                print("Bot is thinking...")
                time.sleep(2)
                card = draw_card(deck)
                if card:
                    print(f"Bot drew {card[0]}!")
                    bot_score += card[1]
                    print(f"Bot's score: {bot_score}")
            else:
                print("Bot decided to stop drawing cards!")
                bot_stopped = True
        
        # Check if game should end
        if check_game_over(player_score, bot_score, player_stopped, bot_stopped):
            break


if __name__ == "__main__":
    main()