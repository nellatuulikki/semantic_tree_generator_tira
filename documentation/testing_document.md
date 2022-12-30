# Testing document

## Unit testing
The code is tested comprehensevily with unit testing utilizing pytest. Only the files under src are tested meaning all files related UI has been left out.

![testi_raportti_vk6](https://user-images.githubusercontent.com/94007460/206872033-bc68bf93-3e78-4cd9-b34e-968fbaf2cf79.png)

The test can be repeated by following the instructions here.

## Code Quality
Code quality has been checked with pylint. The code had couple pretty long functions (over 20 rows).

![pylint_vk6](https://user-images.githubusercontent.com/94007460/206872073-9dc426dd-f773-4537-bcf3-45796072b0f6.png)

## Performance testing

The correctness of proposition clauses required some additional unit testing. All proposition clauses below have been tested with DFS algorithm, in order to veriry that children are created at correct height for correct parent node. Also, the code should always inform about incorrect proposition without crashing. 

The list of proposition clauses that works correctly
- ¬(¬(¬a))
- ¬(¬a)
- (a∨b)→¬(b∨¬(c→b))
- ¬(a→b)→(b→c)
- (A∧C)∧(C∨¬(B→A))

The code should always inform about invalid proposition without crashing. Also, the semantic tree should never be created to a proposition, that has invalid symbols or uneven number of parantheses or two same symbols next to each other (excluding parantheses).
