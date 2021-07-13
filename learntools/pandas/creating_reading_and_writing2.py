import pandas as pd

from learntools.core import *

class FruitDfCreation(EqualityCheckProblem):
    _var = 'fruits'
    _expected = (
            pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas']),
    )
    # TODO: This is a case where it would be nice to have a helper for creating 
    # a solution with multiple alternatives.
    _hint = 'Use the `pd.DataFrame` constructor to create the DataFrame.'
    _solution = CS(
            "fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])"
    )
    
class FruitSalesDfCreation(EqualityCheckProblem):
    _var = 'fruit_sales'
    _hint = 'Set the row labels in the DataFrame by using the `index` parameter in `pd.DataFrame`.'
    _expected = (
            pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales']),
    )
    _solution = CS(
            """fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])""",
            )
            
qvars = bind_exercises(globals(), [
    FruitDfCreation,
    FruitSalesDfCreation,
    ],
    )
__all__ = list(qvars)
