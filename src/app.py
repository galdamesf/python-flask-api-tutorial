from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    print("Incoming request with the following body", request_body)
    #Añadir el nuevo todo a la lista
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
      
    if position < len(todos):
        todos.pop(position)  # Eliminar el todo en la posición indicada
        return jsonify(todos), 200  # Devolver la lista de todos actualizada en formato JSON
    else:
        return jsonify({"error": "Todo not found"}), 404  # Si la posición no existe


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)