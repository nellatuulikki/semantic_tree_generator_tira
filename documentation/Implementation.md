
# Implementation Report

Semantic tree generator is a tool for generating a binary tree for any valid proposition clause. Ths generator utilises semantic tree rules used in Introduction to Logic 1 at University of Helsinki. 

Semantic tree was invented for finding input variables (atomic propositions) in which propositional clause is true, if there exist such input variables. However, semantic tree also shows if all combinations of input variables isn't true. The tree is composed so that all non-atomic propositions are decomposed according to the propositional logic rules until all decompasable statements has been decomposed. The branch is closed if it contains any propositional clause and it's negation. 

The actual semantic tree is constructed as binary tree. The propositional clause that has been converted to a list will be placed at the root of the tree. If propositional clause is not an atomic proposition, it will be decomposed by following its main connective and the children are placed in the end of the branches that are below the decomposed clause according to the decompostion rules. If the children are decompasable they are put in the end of the queue to wait until are decomposed. The logic is applied until there are no more decomposable clauses.

After there are no more decomposable clauses, the semantic tree will be traversal and if a branch has an atomic proposition and its negation, the X will put as a last child of the branch as a mark for branch being closed.

## Semantic Tree rules and examples

Disjunction rule

Conjunction rule

Equivalent rule

Implication rule

## Data structures and Time complexity

The user will give propositional clause as string which will be then transformed into a (nested) list.

## Input/Output

The valid proposition clauses consist of lower and upper case letters literals, connectives (∨, ∧, →, ↔) and negations ¬. All other symbols will generate error message and semantic tree is not generated. I tried to capture all errors by PropositionParser, but I couldn't figure out how I would have prevented them all, so I added exceptation handling in SemanticTreeService node so the software would never crash.

Here are some examples of invalid inputs which will lead to error
- (A∧B)) missmatch of paranthesis
- (), (a∨)
- (aa)
- ¬¬b (Note! double negation should always have paranthesis them)

Output is presented as binary tree utilizing Python's string variable. All decomposed proposition clauses are marked as ✔ and literals and those negations shouldn't have that symbol in any circumstances

## Structure

The software is combined by three main classes:
- SemanticTreeService
   -  maintains software logic and therefore is responsible for creating a semantic tree. Also, it enables communication between UI and entity classes (SemanticTreeNode and PropositionalParser)
- SemanticTreeNode
   -  contains and information of a node and has all features related to adding children to a node. It also stores logic for all propositonal logic rules.
- PropositionalParser
   - responsible for transforming propositional clauses to other datatypes, validation of proposition clause and splitting the propositional clause by its main connective.

App is the main module of the softwate and it starts the software and creates the Flask object and import routes module. Routes module maintains the page address and communicates with page templates and the software logic. Page templates (two in this case) are found in templates directory. 

## UI 

The software is deployed in Heroku. User can type letters and paranthesis but connectivis can be added by the buttons. User can return to the front page and give a new proposition.

## Possible improvements

- Propositions that don't branch are decomposed first -> would reduce branching
- Checking if there is a negation of propositional clause already in the branch instead checking this after all nodes are added into the tree and done only for literals. 

## Sources 
Johdatus Logiikkaan 1 by Åsa Hirvonen
