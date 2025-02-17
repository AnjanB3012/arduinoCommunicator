from flask import Flask,request, render_template

app = Flask(__name__)

message_store = {"msg": "","edgemsg":"Yet To Receive Message"}

letter_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", " ":"/",
}

@app.route('/sendMessage', methods=['POST'])
def sndmsg():
    data = request.get_json()
    tempMessage=data['Message']
    message_store['msg'] = ""
    for i in range(len(tempMessage)):
        message_store['msg']+=letter_dict[tempMessage[i]]+" "
    return {"message":"Converted"}

@app.route("/getMessage", methods=['GET'])
def getmsg():
    tempMessage = message_store['msg']
    message_store['msg'] = ""
    return tempMessage

@app.route("/sendMessageEdge", methods=['POST'])
def sndmsgedge():
    data = request.get_json()
    tempMessage=data['Message']
    message_store["edgemsg"] = tempMessage
    print(tempMessage)
    return {"message":"Success"}

@app.route("/", methods=['GET'])
def getedgemsg():
    return render_template("index.html",inputMessage=message_store["edgemsg"])


if __name__ == '__main__':
    app.run(debug=True)