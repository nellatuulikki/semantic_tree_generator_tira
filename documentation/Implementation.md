
# Implementation Report

Semantic tree generator is a tool for generating a binary tree for any valid proposition clause. Ths generator utilises semantic tree rules used in Introduction to Logic 1 at University of Helsinki. 

## Semantic Tree rules and examples

Disjunction rule 

Conjunction rule

Equivalent rule

Implication rule

## Data structures and Time complexity

Semantic tree is constructed as binary tree. Every node has a proposition in list format.

## Input/Output

The valid proposition clauses consist of lower and upper case letters literals, connectives (∨, ∧, →, ↔) and negations ¬. All other symbols will generate error message and semantic tree is not generated.
Here are some examples of invalid inputs which will lead to error
- (A∧B)) missmatch of paranthesis
- ()
- (aa)

Output is presented as binary tree utilizing Python's string variable.

## Class diagram

The software is combined by three main classes:
- SemanticTreeService
   -  maintains software logics and therefore is responsible for creating a semantic tree. Also, it enables communication between UI and entity classes             (SemanticTreeNode and PropositionalParser)
- SemanticTreeNode
   -  contains and controls information of specific node and has a responsibility of features related to adding children to a node. 
- PropositionalParser
   - has a responsibility to transform propositional clauses to other datatypes, validation of proposition clause and splitting the propositional propositional clause by its main connective.
