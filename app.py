from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'


class QuizForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=120)])
    q1 = RadioField(
        "What is Lord Voldemort's real name?",
        choices=[('tom_riddle', 'Tom Riddle'), ('severus_snape', 'Severus Snape'), ('sirius_black', 'Sirius Black')],
        validators=[DataRequired()]
    )
    q2 = RadioField(
        "How many Horcruxes does Voldemort hide?",
        choices=[('5', '5'), ('6', '6'), ('7', '7')],
        validators=[DataRequired()]
    )
    q3 = RadioField(
        "What is Professor Snape's Patronus animal?",
        choices=[('stag', 'Stag'), ('doe', 'Doe'), ('phoenix', 'Phoenix')],
        validators=[DataRequired()]
    )
    q4 = RadioField(
        "What are the Deathly Hallows?",
        choices=[
            ('wand_cloak_stone', 'Elder Wand, Invisibility Cloak, Resurrection Stone'),
            ('broom_map_time_turner', 'Firebolt, Marauder\'s Map, Time-Turner'),
            ('sword_locket_diadem', 'Gryffindor\'s Sword, Slytherin\'s Locket, Ravenclaw\'s Diadem')
        ],        validators=[DataRequired()]
    )
    q5 = RadioField(
        "Who was killed in the Goblet of Fire?",
        choices=[('cedric_diggory', 'Cedric Diggory'), ('neville_longbottom', 'Neville Longbottom'), ('colin_creevey', 'Colin Creevey')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def quiz():
    form = QuizForm()
    if form.validate_on_submit():
        score = sum([
            form.q1.data == 'tom_riddle',
            form.q2.data == '7',
            form.q3.data == 'doe',
            form.q4.data == 'wand_cloak_stone',
            form.q5.data == 'cedric_diggory'
        ])
        return redirect(url_for('result', name=form.name.data, age=form.age.data, score=score))
    return render_template("quiz.html", form=form)

@app.route('/result')
def result():
    name = request.args.get('name')
    age = request.args.get('age')
    score = request.args.get('score', type=int)
    return render_template("result.html", name=name, age=age, score=score)

if __name__ == '__main__':
    app.run(debug=True)
