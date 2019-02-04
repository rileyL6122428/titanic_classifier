- [ ] get stats on each attribute
    - [x] class (refactor?)
    - [x] age
    - [x] gender (refactor?)
    - [x] title (refactor?)
    - [x] sibsp number
    - [x] parents children
    - [x] embarked
    - [x] cabin
    - [x] fare

    *DERIVED ATTRS*

    - [x] fare / (sibsp + parch) **NOT FRUITFUL**
    

- [x] decide on attrs
    try with class and gender, then try with fare and gender, then with all 3
    
- [ ] build pipeline
    1. one hot encode class
    2. one hot encode gender
- [ ] build logistic classifier
- [ ] build linear with logistic
- [ ] build decision tree classifier

```Python
# return passengers.drop(columns=[
#     'PassengerId',
#     'Name',
#     'Age',
#     'SibSp',
#     'Parch',
#     'Ticket',
#     'Cabin',
#     'Embarked',
#     'Title'
# ])
```
