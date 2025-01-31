from flask import Flask, jsonify, render_template
from usm_day_pass.app import Core


app = Flask(__name__)
core = Core()

@app.route('/')
def index():
    return render_template('passes.html', passes=core.passes_service.list(to_dict=True))

@app.route('/passes', methods=['GET'])
def list_passes():
    return jsonify(core.passes_service.list())

@app.route('/passes/stars/<int:stars>', methods=['GET'])
def get_pass_stars(stars):
    return jsonify(core.passes_service.get_pass_stars(stars))


if __name__ == '__main__':
    app.run(debug=True) 