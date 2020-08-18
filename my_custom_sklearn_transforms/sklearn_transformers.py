from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

# All sklearn Transforms must have the `transform` and `fit` methods
class CreateColumnMean(BaseEstimator, TransformerMixin):
    def __init__(self, columns, new_column):
        self.columns = columns
        self.new_column = new_column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        data[self.new_column] = 0
        for column in self.columns:
            data[self.new_column] = data[self.new_column] + data[column]
        data[self.new_column] = data[self.new_column] / len(self.columns)
        # Retornamos um novo dataframe com a nova coluna
        return data
    
# All sklearn Transforms must have the `transform` and `fit` methods
class CreateColumnSum(BaseEstimator, TransformerMixin):
    def __init__(self, columns, new_column):
        self.columns = columns
        self.new_column = new_column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        data[self.new_column] = 0
        for column in self.columns:
            data[self.new_column] = data[self.new_column] + data[column]
        # Retornamos um novo dataframe com a nova coluna
        return data