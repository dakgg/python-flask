from flask import Flask, request, jsonify
from tasks import add, celery_app
from celery.result import AsyncResult

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    task = add.apply_async(args=[data['x'], data['y']])
    return jsonify({'task_id': task.id}), 202

@app.route('/result/<task_id>')
def get_result(task_id):
    result = AsyncResult(task_id, app=celery_app)
    return jsonify({
        'ready': result.ready(),
        'result': result.result if result.ready() else None
    })
    
if __name__ == '__main__':
    app.run(debug=True)