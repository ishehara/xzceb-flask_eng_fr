from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    
    translator.english_to_french(input("English Test: "))
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translator.french_to_english(input("French Test: "))
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('xzceb-flask_eng_fr\final_project\templates\index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
