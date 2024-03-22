from flask import Flask, render_template, request, jsonify, redirect, url_for
from student import interact_with_gpt, conversation_history
from professor import ProgramGeneratorEngine
import logging
from flask import send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Set up logging
app.logger.setLevel(logging.INFO)
app.logger.addHandler(logging.StreamHandler())

# Initialize the program generator engine
#api_key = ""  # Replace with your OpenAI API key
program_generator = ProgramGeneratorEngine()

assignment_name = None


def modify_assignment_name(new_value):
    global assignment_name 
    assignment_name = new_value 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        # Process form submission from user_info.html
        # You can handle form data here if needed
        return redirect(url_for('student'))
    else:
        return render_template('user_info.html')

@app.route('/student')
def student():
    modify_assignment_name(request.args.get('assignment'))
    print(assignment_name,"11111")
    return render_template('students.html', assignment_name=assignment_name)
    #return render_template('students.html')

@app.route('/professor', methods=['GET', 'POST'])
def professor():
    trained = program_generator.train_model()
    
    if trained and request.method == 'POST':
        topic = request.form['topic']
        difficulty_level = request.form['difficulty']
        
        result = program_generator.generate_questions(topic, difficulty_level)
        return render_template('professor.html', result=result)
    return render_template('professor.html')

@app.route('/user_message', methods=['POST'])
def handle_user_message():
    data = request.json
    app.logger.info(f"Received user_message event: {data}")
    user_input = data.get("message")

    if user_input:
        # assignment_name = request.args.get('assignment')
        print(assignment_name,"2222")
        result = interact_with_gpt(user_input, conversation_history, assignment_name)
        return jsonify(result)  # Return the response as JSON
    

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)

