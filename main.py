from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<href>"

@app.route("/tts")
def tts():
    return render_template("tts.html")

@app.route("/tts/say")
def say():
    text = request.args.get('text')
    lang = request.args.get('lang')
    if  lang == None:
        lang == 'de'
    try:
        print(text)
    except Exception as e:
        print(e)
        pass
    return redirect(url_for('tts'))

if __name__ == "__main__":
    app.run()