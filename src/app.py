from flask import Flask, render_template, url_for, request, redirect
from os import path
from Matcher import Matcher

app = Flask(__name__)

app.config["FILE_UPLOADS"] = path.join(app.root_path, 'static', 'files')
app.config["ALLOWED_EXT"] = ["txt"]

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
    if request.method == 'POST':
        answers = []
        keyword = request.form['keywordInput']
        option = request.form['radioMethod']
        if request.files:
            # for f in request.files['sourceFile']
            #     files = request.files['sourceFile']
            #     print(f)
            files = request.files.getlist('sourceFile')
            for file in files:
                print(file)
                file_name = file.filename
                if file.filename == "" or file.filename == " " or file.filename == None:
                    print("NAMELESS FILE")
                    redirect(request.url)
                else:
                    try:
                        # if not allowed_file(file.filename):
                        #     print("FORBIDDEN FILE")
                        #     return redirect(request.url)    
                        # else:
                        file.save(path.join(app.config["FILE_UPLOADS"], file.filename))
                        print("File saved")
                    except Exception as e:
                        print(e)
                        print("NO FILES UPLOADED")
            
        
        # filename = secure_filename(files.filename)
        # file.save(os.path.join("extract", filename))
        method = request.form['radioMethod']
        output = str(keyword) + str(method)
         # You should use os.path.join here too.
        # with open(os.path.join("extract", filename)) as f:
        #     file_content = f.read()

        
        # print(files)
        try:
            # Model
            # return file_content 
            # return str(keyword) + str(option) 
            return render_template('index.html', keyword = keyword)
        except Exception as e:
            return "There was an issue processing the files"
        
    else:
        keyword = None
        return render_template("index.html")

def postAnswers(ans):
    pass


if __name__ == "__main__":
    app.run(debug=True)