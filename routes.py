from app import app
from flask import render_template, request
from src.services.semantic_tree_service import SemanticTreeService


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    proposition = request.form["proposition"]
    semantic_tree_generator = SemanticTreeService(proposition)
    semantic_tree_boolean = semantic_tree_generator.generate_semantic_tree()
    
    if semantic_tree_boolean:
        semantic_tree_generator.tree_str(semantic_tree_generator.root_proposition, 0)
        semantic_tree_list = semantic_tree_generator.semantic_tree_string
    else:
        semantic_tree_list = []

    return render_template("result.html",
                            proposition=semantic_tree_generator.root_proposition_string,
                            semantic_tree_boolean=semantic_tree_boolean,
                            semantic_tree_list=semantic_tree_list)