from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    #return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")
    
@app.route("/application-form")
def application_form():
    return render_template("application-form.html")

@app.route("/application",methods=["POST"])
def application_info():
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    position = request.form.get("position")
    
    return """
    <!Doctype html>
    <html>
    <head>
    </head>
    </body>
        <p> Thank you, %s %s, for applying to be a %s. Your minimum salary requirement is %s dollars.</p>
    </body>
    </html>""" % (first_name, last_name, position, salary)
    

if __name__ == "__main__":
    app.run(debug=True)