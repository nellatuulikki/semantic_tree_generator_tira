# Testing document

## Unit testing
The code is tested comprehensevily with unit testing utilizing pytest. Only the files under src are tested meaning all files related UI has been left out.

![pytest_final](https://user-images.githubusercontent.com/94007460/210141021-2210930a-3377-4876-bfcc-d53db5d8ccc7.png)

The test can be repeated by following the instructions [here]([https://semantic-tree-generator.herokuapp.com/](https://github.com/nellatuulikki/semantic_tree_generator_tira/blob/main/documentation/user_instructions.md)).

## Code Quality
Code quality has been checked with pylint. The code had couple pretty long functions (over 20 rows).

![pylint_final](https://user-images.githubusercontent.com/94007460/210141016-bcac753d-cf8b-42e3-a9dc-f64782c8e892.png)

## Performance testing

The correctness of proposition clauses required some additional unit testing. All proposition clauses below have been tested with DFS algorithm, in order to veriry that children are created at correct height for correct parent node. Also, the code should always inform about incorrect proposition without crashing. 

The list of proposition clauses that works correctly
- ¬(¬(¬a))
- ¬(¬a)
- (a∨b)→¬(b∨¬(c→b))
- ¬(a→b)→(b→c)
- (A∧C)∧(C∨¬(B→A))

The code should always inform about invalid proposition without crashing. Also, the semantic tree should never be created to a proposition, that has invalid symbols or uneven number of parantheses or two same symbols next to each other (excluding parantheses).
