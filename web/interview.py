from flask import Flask, render_template, request, jsonify
from akkadian import *
# from hammurabi import *
from ..hammurabi.us.fed.tax.indiv import withholding as withholding

# print(withholding.__file__)

# print(dir())
app = Flask(__name__)

# set FLASK_APP=interview.py
@app.route("/")
def investigate_goal():
    # return render_template('main_interview.html')
    # return Investigate([(form_w4_complete, "Hub", "Wife")])
    return web_apply_rules([(withholding.form_w4_complete, "Hub", "Wife")])
   

@app.route('/', methods=['POST'])
def call_on_form_post():
    answer = request.form['answer']
    # print(answer)
    return answer


def web_apply_rules(goals: list, fs=[]):
    #for debugging
    # return jsonify(ApplyRules(goals, fs))
    
    # Call the "apply rules" interface
    results = ApplyRules(goals, fs)

    # If all of the goals have been determined, present the results
    if results["complete"]:
        return results["msg"]  # TODO

    # Otherwise, ask the next question...
    else:
        # Find out what the next question is
        nxt = results["missing_info"][0]

        # Ask it
        return collect_input(nxt)
        # new = collect_input(nxt)

        # Add the newly acquired fact to the fact list
        fs.append(Fact(nxt[1], nxt[2], nxt[3], convert_input(nxt[0], new)))

        # Go to step 1
        return web_apply_rules(goals, fs)

def collect_input(attr):
    #attr 1 = type
    #attr 2 = attribute name
    #attr 3 = subject
    #attr 4 = obj
    #attr 5 = question text
    type = attr[0]
    public_name = attr[1]
    subject = attr[2]
    obj = attr[3]
    question = attr[4]

    if(attr[0] == "bool"):
        return render_template('main_interview.html', type=type, question=question,)

    #for debugging
    return jsonify(attr)
