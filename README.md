# 🕹️ DarkRealm - A Text-Based Adventure Game

**DarkRealm** is a fantasy-themed text adventure game written in Python.  
Explore mysterious lands, face powerful enemies, and shape your destiny — one line at a time.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

> 🚧 Development is in early stages. Contributions, feedback, and ideas are welcome!

---

## 🚀 Features
- 🧙 Character creation (name, class)
- 📜 Choice-based storytelling
- ⚔️ Basic combat and inventory system
- 🎨 ASCII art for characters and scenes
- 💾 Save/load functionality
- 🧩 Modular and expandable story system

---

## 📁 Project Structure

```bash
darkrealm/
├── game.py              # Entry point
├── [assets/](./assets)              # Core logic and game systems
│   ├── __init__.py
│   ├── player.py
│   ├── inventory.py
│   ├── enemies.py
│   ├── ascii_art.py
│   ├── weapon.py
│   └── utils.py
├── [story/](./story)               # JSON story files
│   └── intro.json
├── [saves/](./saves)               # Player save files
├── [art/](./art)                 # ASCII art
│   └── dragon.txt
├── LICENSE
└── README.md
```

---

## 🛠 Requirements

- Python **3.10+**
- Works in any **terminal** or **command line**
- Recommended: VSCode or another code editor for development

---

## ▶️ How to Run

```bash
cd darkrealm
python game.py
```

---

## 🌱 Contributing

Got an idea for a quest? A cool ASCII dragon? Found a bug?  
Feel free to open an issue or submit a pull request!

To add new story scenes, place JSON files in the `story/` directory and follow the format used in `intro.json`.

---

## 📜 License

MIT License. Free to use, modify, and share.

---

## 📫 Contact

Made by [@DarkRawel](https://github.com/DarkRawel)  
Inspired by retro RPGs, fantasy, and interactive fiction.
