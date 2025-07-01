from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store tasks as dictionaries with text, done status, and due date
tasks = []  # Example: {'text': 'Buy milk', 'done': False, 'due': '2025-07-01'}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task')
    due_date = request.form.get('due')
    if task_text:
        tasks.append({'text': task_text, 'done': False, 'due': due_date})
    return redirect('/')

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = not tasks[task_id]['done']
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

@app.route('/clear')
def clear_all():
    tasks.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
