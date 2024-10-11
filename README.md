# Harry Potter Quiz App


## Description

This web app asks the User to Enter his Name and Age then take the 5 Quiz which Is 5 Multiple Choice questions
about Harry Potter Franchise if the user gets 4/5 or 5/5 he is a potter head and displaying a nice photo that he would like
if he got less than 4/5 then he is not a potter head and he is a muggle!!

## Features

- User input validation
- Multiple-choice questions
- Score calculation
- Responsive design
- Custom result page with different outcomes based on score

## Prerequisites

- Python 
- Flask
- Flask-WTF

## Installation

1. Clone this repository or download the source code.

2. Install the required packages:
```bash
pip install flask flask-wtf
```

## Project Structure

```
harry-potter-quiz/
│
├── app.py              
├── templates/
│   ├── quiz.html      
│   └── result.html    
├── static/
│   └── images/
│       ├── 1.jpg      
│       └── 2.jpg     
└── README.md
```

## Usage

1. Set up your environment and install dependencies.

2. Run the application:
```bash
python app.py
```

3. Open a web browser and navigate to `http://localhost:5000`.

## Quiz Questions

The quiz includes questions about:
1. Lord Voldemort's real name
2. Number of Horcruxes
3. Professor Snape's Patronus Animal
4. The Deathly Hallows
5. Character death in Goblet of Fire

## Customization

To modify the quiz:
1. Edit the `QuizForm` class in `app.py` to change questions, options, or add new questions.
2. Update the scoring logic in the `quiz()` route function.
3. Modify the templates to change the appearance or layout.

"#Harry-Potter-Quiz" 
