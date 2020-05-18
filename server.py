from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

print(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


@ app.route('/works')
def works():
    return render_template("works.html")


@ app.route('/work')
def work():
    return render_template("work.html")


@ app.route('/about')
def about():
    return render_template("about.html")


@ app.route('/contact')
def contact():
    return render_template("contact.html")


@ app.route('/components')
def components():
    return render_template("components.html")


@ app.route('/thank-you')
def thank_you():
    return render_template("thank-you.html")


def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(
            f"\n email: {email}, subject: {subject}, message: {message}")


def write_to_csv(data):
    with open("database.csv", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",",
                                quotechar="'", quoting=csv.QUOTE_MINIMAL)
        # csv_writer.writerow([])
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # email = request.form['email']
            # subject = request.form['subject']
            # message = request.form['message']
            write_to_file(data)
            write_to_csv(data)
            return redirect("thank-you")
        except:
            return "did not save to database"
    else:
        return "something went wrong!!!"

    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # # return render_template('login.html', error=error)
    # return "form submitted "
