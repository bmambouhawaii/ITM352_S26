from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index2.html')

# Quiz page
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# Result page
@app.route('/result', methods=['POST'])
def result():
    answer = request.form.get('answer')

    if answer == "4":
        score = "Correct ✅"
    else:
        score = "Wrong ❌"

    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)