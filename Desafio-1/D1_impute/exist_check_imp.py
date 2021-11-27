import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer

class ImputeVariables(BaseEstimator, TransformerMixin):

	def __init__(self, columns):

		self.columns = columns

	def fit(self, X, y = None):

		return self

	def transform(self, X):

		data=X.copy()

		exist_sav_col_mod = pd.DataFrame(data[self.columns[0]].replace(to_replace='UNKNOWN', value=np.nan))
		imp_exist = SimpleImputer(missing_values=np.nan, strategy= 'mean')
		clean_exist = imp_exist.fit_transform(exist_sav_col_mod)

		check_bal_col_mod = pd.DataFrame(data[self.columns[1]].replace(to_replace='NO_CHECKING', value= np.nan))
		imp_check = SimpleImputer(missing_values=np.nan, strategy= 'mean')
		clean_check = imp_exist.fit_transform(check_bal_col_mod)

		data.loc[:,'EXISTING_SAVINGS'] = clean_exist
		data.loc[:,'CHECKING_BALANCE'] = clean_check

		return data