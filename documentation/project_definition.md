The purpose of the project is to create an algorithm to solve and print semantic tree of any propositional clause in Python. 

### Algorithm and data structures used
The project utilizes branching algorithm that grows tree as follows
  1. The proposition is placed at the root of the tree
  2. Apply appropriate branching rule to the first unchecked proposition. Change status of the proposition to        checked and extend every active path under the proposition based on the branching tule. 
  3. If path contains an atomic proposition and its negation, put X at the end of the path. 
  5. Steps 2 and 3 are repeated until paths don't have any unchecked propositions.

The tree will be stored as binary tree (implemented as a class?), and/or utilizing Python hash table data structures set and dict. Time complexity for binary trees are usually O(h), where h represents the height of the tree.

### Input and output
The user will give an input string which consist of atomic propositions, connectives (¬, ∧, ∨, →, ↔) and brackets  for identification of subformulas. Usage of other symbols are invalid. The output is printed as binary tree.

### Source
- https://mysite.science.uottawa.ca/phofstra//MAT1348/TruthTrees.pdf
- https://moodle.helsinki.fi/pluginfile.php/4415712/mod_resource/content/3/Johdatus_logiikkaan_1.pdf
- https://raw.githubusercontent.com/hy-tira/tirakirja/master/tirakirja.pdf

### Study program

BCompSc
