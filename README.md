# Code Refactoring and Quality Improvements

## PEP8 Compliance
- Consistent indentation using 4 spaces
- Proper spacing around operators and after commas
- Optimized line length (maximum 79 characters)

## Typing Added
- Type hints for all function parameters and return values
- Clear data structure definitions using `List[Tuple[str, int]]`

## Functions with English Documentation
- **initialize_deck()**  
  Creates and initializes the card deck.

- **draw_card()**  
  Handles card drawing logic, including deck state checks.

- **check_game_over()**  
  Contains all game-ending conditions.

- **main()**  
  Main game loop with a detailed description of the gameplay flow.

## Code Structure
- Separated game logic into reusable, well-defined functions
- Removed duplicate code that was present twice in the original version
- Improved variable naming for better readability  
  (e.g., `aw` → `card`)

## Translation to English
- Card names translated to English
- All game messages displayed in English
- Comments and documentation written in English

## Error Handling
- Added a check for an empty deck in `draw_card()`
- Implemented more robust user input handling

## Notes
The game fully preserves the original Russian card game logic while significantly improving code quality, readability, and maintainability, as well as providing a complete English-language interface.
