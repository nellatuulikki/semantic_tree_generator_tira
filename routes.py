from app import app
from flask import render_template, request
from src.services.semantic_tree_gen import SemanticTreeGenerator


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    proposition = request.form["proposition"]
    semantic_tree_generator = SemanticTreeGenerator(proposition)
    semantic_tree = semantic_tree_generator.generate_semantic_tree()

    return render_template("result.html", propostion=proposition, semantic_tree=semantic_tree)