from flask import Flask, render_template, url_for, request, redirect
from os import path
from Form import Form

app = Flask(__name__)

app.config["FILE_UPLOADS"] = path.join(app.root_path, 'static', 'files')

def allowed_file(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper in app.config["ALLOWED_EXT"]:
        return True
    else:
        return False

@app.route('/', methods=['POST', 'GET'])
def index():
    keyword = ""
    if request.method == 'POST':
        answers = []
        keyword = request.form['keywordInput']
        option = request.form['radioMethod']
        if request.files:
            files = request.files.getlist('sourceFile')
            for file in files:
                if file.filename == "" or file.filename == " " or file.filename == None:
                    print("NAMELESS FILE")
                    redirect(request.url)
                try:
                    file.save(path.join(app.config["FILE_UPLOADS"], file.filename))
                    print("File saved")
                except Exception as e:
                    print(e)
                    print("NO FILES UPLOADED")
                form = Form(file.filename, keyword, option)
                form.readFile()
                answers.append(form)
            
        
        
        try:
            return render_template('index.html', keyword=keyword, answers=answers)
            return redirect(request.url)
        except Exception as e:
            return "There was an issue processing the files"
            return render_template('index.html', keyword=keyword, answers=answers)
        
    else:
        return render_template("index.html", keyword = keyword)

def postAnswers(ans):
    pass


if __name__ == "__main__":
    app.run(debug=True)