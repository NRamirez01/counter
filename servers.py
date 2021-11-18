from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'Squidward is bad at clarinet'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
        visits = session['count']
    else:
        session['count'] = 1
        visits = session ['count']
    return render_template("root.html", visits = visits)

@app.route('/update_counter', methods= ['POST'])
def update_values():
    print(session['count'])
    session['count'] += 1
    return redirect('/')


@app.route('/destroy_session', methods= ['POST'])
def basis():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

