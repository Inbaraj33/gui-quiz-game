gui-quiz-game/
│
├── main.py                 # Entry point of the application
├── quiz_app.py            # Main QuizGameApp class
├── question_manager.py    # Question loading and management
├── ui_components.py       # GUI components and styling
├── score_manager.py       # Score tracking and results
│
├── data/
│   ├── questions.json     # Default question set
│   ├── science.json       # Science category questions
│   ├── history.json       # History category questions
│   └── general.json       # General knowledge questions
│
├── assets/
│   └── icons/            # Application icons (optional)
│
├── config/
│   └── settings.json     # App configuration
│
├── results/
│   └── quiz_results.json # Store user results/history
│
└── README.md


# For Windows Command Prompt (cmd)
mkdir gui-quiz-game
cd gui-quiz-game
mkdir data
mkdir assets
mkdir assets\icons
mkdir config
mkdir results
echo. > main.py
echo. > quiz_app.py
echo. > question_manager.py
echo. > ui_components.py
echo. > score_manager.py
echo. > data\questions.json
echo. > data\science.json
echo. > data\history.json
echo. > data\general.json
echo. > config\settings.json
echo. > results\quiz_results.json
echo. > README.md

# For Windows PowerShell
mkdir gui-quiz-game
cd gui-quiz-game
mkdir data
mkdir assets
mkdir assets\icons
mkdir config
mkdir results
New-Item main.py
New-Item quiz_app.py
New-Item question_manager.py
New-Item ui_components.py
New-Item score_manager.py
New-Item data\questions.json
New-Item data\science.json
New-Item data\history.json
New-Item data\general.json
New-Item config\settings.json
New-Item results\quiz_results.json
New-Item README.md

git add .
git commit -m "project structure" 
git status
git config --global user.name "Inbaraj33"
git config --global user.email "inbarajt@gmail.com"
