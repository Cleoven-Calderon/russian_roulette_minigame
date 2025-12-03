# Russian Roulette Minigame 🎲🔫

A simple Python-based Russian Roulette–style minigame.  

## 🎯 What is this

This project is a text-based (or terminal / console-based) minigame inspired by the classic “Russian Roulette” concept: random chance determines survival each turn. The game lets players/testers experience a simple survival-style gambling of luck via Python.

## 📂 Repository Structure / Files  

```
/ (root)
├── Main_game.py            # Main script to launch the game
├── Base_1.py               # Base / helper functionality (e.g. common functions, classes)
├── Asset_1.py, Asset_2.py  # Additional modules (e.g. assets, utility code)
├── First_difficulty.py     # Game logic for first difficulty level
├── Second_difficulty.py    # Game logic for second difficulty level
├── Third_difficulty.py     # Game logic for third / hardest difficulty level
└── .idea/                   # IDE/editor settings (optional / can be ignored)
```

- **Main_game.py** — entry point to start the game and choose difficulty or settings.  
- **Base_1.py** — supporting code used by different difficulty modules (shared functions / logic).  
- **Asset_*.py** — additional modules, configuration, or helper logic (e.g. assets, settings, utilities).  
- **First/Second/Third_difficulty.py** — define the game behavior depending on chosen difficulty level (e.g. chance, rules, rounds).

## ✅ Prerequisites  

- Python 3.x installed  
- No external dependencies (unless you add them)  
- A terminal / console to run the script  

## 🛠️ How to Run  

Run the main script from terminal:

```bash
python Main_game.py
```

Then follow on-screen prompts to play the game (choose difficulty, proceed through rounds, etc.)  

## 🎮 What the Game Does  

- Simulates a Russian Roulette–style “chance” game  
- Presents different difficulty levels for varied gameplay (easy → hard)  
- Uses randomization / probability to decide outcome — provides replay / fun unpredictability  

## 📈 Potential Improvements / Roadmap  

- Add a “multiplayer” or “versus computer / other players” mode  
- Add user interface (console enhancements or GUI) for better player experience  
- Add history / logging of games (record wins / losses)  
- Add customization (number of bullets/chambers, adjustable probabilities)  
- Add more difficulty levels, better balancing, or optional “safe” rounds  

## 🤝 Contributing  

This was one of my earliest simple projects, still proud of it. Feel free to fork!

## 📝 License  

No. Nothing  
