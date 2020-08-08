from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/ledoff/")
@app.route("/")
def ledoff():
    return render_template("ledoff.html")

@app.route("/ledon/")
def ledon():
    return render_template("ledon.html")


@app.route("/led")
def led():

    args = request.args
    if args["status"] == "on":
        print("status on")
        fh = open("ledfile", "a")
        fh.write(f"led now on:  {datetime.now()}\n")
        fh.close()
        return redirect(url_for("ledon"))
    else:
        print("status off")
        fh = open("ledfile", "a")
        fh.write(f"led now off:  {datetime.now()}\n")
        fh.close()
        return redirect(url_for("ledoff"))




if __name__ == "__main__":
    app.run(debug=True)



# How to get the currrent date and time in Python -
# https://www.programiz.com/python-programming/datetime/current-datetime
