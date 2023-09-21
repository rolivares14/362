from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    fullname = request.form['fullname']
    email = request.form['email']
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
