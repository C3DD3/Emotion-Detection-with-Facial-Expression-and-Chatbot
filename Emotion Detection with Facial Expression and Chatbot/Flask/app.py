from flask import Flask, render_template, request, jsonify
import videocap
import gemini  

app = Flask(__name__)

duygu_saklama_string = ""  # Global değişken olarak tanımlandı

@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/exec')
def parse(name=None):
    return render_template('chatbot.html')

@app.route("/get")
def intro():
    global duygu_saklama_string
    face = videocap.meth() 
    
    instruction = "" 

    if face == 'Mutlu':
        instruction = 'mutlu hissediyorum,ona göre cevap ver'
    elif face == 'Nötr':
        instruction = 'Bugün sanki dün ile aynı, hiç bir değişiklik yok,ona göre cevap ver'
    elif face == 'Üzgün':
        instruction = 'Üzgün hissediyorum,ona göre cevap ver  '
    elif face == 'Sinirli':
        instruction = 'Sinirli hissediyorum,ona göre cevap ver'
    elif face == 'Şaşırmış':
        instruction = 'Şaşkın hissediyorum,ona göre cevap ver'
    else:
        instruction = 'Hiçbir şey hissetmiyorum,ona göre cevap ver'

    return instruction

@app.route("/bot", methods=["GET"])
def getBotResponse():
    userText = request.args.get('msg')
    result = gemini.get_gemini_response(userText)
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(threaded=False, debug=True)
