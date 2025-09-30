from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="Naman Mehra", profession="Student")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Process form data here (store or send email etc.)
        return f"Thank you {name}, your message has been received."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
