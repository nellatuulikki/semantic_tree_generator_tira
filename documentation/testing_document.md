# Testing document

## Unit testing
The code is tested comprehensevily with unit testing using pytest. Only the files under src are tested meaning all files related UI has been left out.

![pytest_final](https://user-images.githubusercontent.com/94007460/210141021-2210930a-3377-4876-bfcc-d53db5d8ccc7.png)

The test can be repeated by following the instructions [here](https://github.com/nellatuulikki/semantic_tree_generator_tira/blob/main/documentation/user_instructions.md).

## Code Quality
Code quality has been checked with pylint. 

![pylint_final](https://user-images.githubusercontent.com/94007460/210141016-bcac753d-cf8b-42e3-a9dc-f64782c8e892.png)

Also, the code has couple pretty long functions (over 20 rows).

## Performance testing

The correctness of proposition clauses required some additional unit testing. Correctness has been tested with DFS algorithm, in order to verify that children are created at correct height for correct parent node.
The code should always inform about invalid proposition without crashing. Also, the semantic tree should never be created to a proposition, that has invalid symbols or uneven number of parantheses or two same symbols next to each other (excluding parantheses). 

The drawing of the tree was also tested, but it couldn't be tested with more complex clauses, since those were harder to test because trees needed some much space in the testing code. These tests also included invalid propositions in order to be sure that no drawing was done to invalid inputs.
