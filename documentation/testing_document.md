# Testing document

## Unit testing
Unit testing is done with pytest. Testing result is little bit lower than last week.

![testi_raportti_vk6](https://user-images.githubusercontent.com/94007460/206872033-bc68bf93-3e78-4cd9-b34e-968fbaf2cf79.png)

## Code Quality
Code quality has been checked with pylint. There is still room for improvement on code quality.

![pylint_vk6](https://user-images.githubusercontent.com/94007460/206872073-9dc426dd-f773-4537-bcf3-45796072b0f6.png)

## Performance testing

The list of proposition clauses that works correctly
- a↔b
- ¬a↔b
- (a→b)→(b→c)
- (a∧b)∨(b∧c)
- ¬(¬a∨b)
- (a∧b∨d)∨(b∧c)
- ¬(¬(¬a))
- ¬(a→b)→(b→c)
- (a∧b∨d)∨(b∧c)∨(b∧a)
- (A∨B)→¬(A∨¬(B→C)) 

The list of proposition clauses that works incorrectly
- ?
