from flask import Flask, render_template, request, send_file
import os
from io import BytesIO
# from pylint import pyreverse


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/upload", methods=['POST'])
def upload():
    try:
        file = request.files['path']
        split_tup = os.path.splitext(file.filename)
        if split_tup[1] == '.py':
            temp = "temp.py"
            with open(temp, 'wb') as f:
                f.write(BytesIO(file.read()).read())
                f.close()
            path = os.path.abspath(temp)
            os.system("pyreverse -o png " + path)
            output = "classes.png"
            os.remove(temp)
            return send_file(output, download_name="Uml_diagram.png", as_attachment=True)
        elif split_tup[1] == '.java':
            temp = "test.java"
            with open(temp, 'wb') as f:
                f.write(BytesIO(file.read()).read())
                f.close()
            path = os.path.abspath(temp)
            os.system("pyreverse -o png " + path)
            output = "classes.png"
            os.remove(temp)
            return send_file(output, download_name="Uml_diagram.png", as_attachment=True)
        else:
            print("error")
    except:
        return "<h1>Please select a valid file</h1>"


@app.route("/upload_mul", methods=['POST'])
def mul():
    try:
        files = request.files.getlist('mul')
        temp = "temp.py"
        for f in files:
            print(f)
            with open(temp, 'ab') as file:
                file.write(BytesIO(f.read()).read())
                file.close()
        path = os.path.abspath(temp)
        os.system("pyreverse -o png " + path)
        output = "classes.png"
        os.remove(temp)
        return send_file(output, download_name="Uml_diagram.png", as_attachment=True)

    except:
        return "<h1>Please select valid files</h1>"

if __name__ == "__main__":
    app.run(debug=True)
