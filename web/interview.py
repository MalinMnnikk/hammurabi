from flask import Flask, render_template, request
import sys

if __name__ == "__main__":
    sys.path.append('c://hammurabi')
    # print(sys.path)
    from akkadian.session import * 
    from hammurabi.us.fed.tax.indiv.withholding import form_w4_complete


app = Flask(__name__)

# set FLASK_APP=interview.py
@app.route("/")
def investigate_goal():
    # return render_template('main_interview.html')
    # return Investigate([(form_w4_complete, "Hub", "Wife")])
    return interview_investigate([(form_w4_complete, "Hub", "Wife")])
   

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


def interview_investigate(goals: list, fs=[]):

    # Call the "apply rules" interface
    re = ApplyRules(goals, fs)

    # If all of the goals have been determined, present the results
    if re["complete"]:
        return re["msg"]  # TODO

    # Otherwise, ask the next question...
    else:
        # Find out what the next question is
        nxt = re["missing_info"][0]

        # Ask it
        new = collect_input(nxt[4], nxt)

        # Add the newly acquired fact to the fact list
        fs.append(Fact(nxt[1], nxt[2], nxt[3], convert_input(nxt[0], new)))

        # Go to step 1
        return interview_investigate(goals, fs)

def collect_input(q: str, attribute):
    return attribute