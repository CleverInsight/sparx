:orphan:


Usage
=================


is_categorical
---------------

	**Parameters**:
	
		df: pandas.core.Dataframe
			enter the complete dataframe

		col_name: str

	**Usage**:
		>>> p = process()
		>>> p.is_categorical(df['State'])
		>>> True/False





is_number
----------

	**Parameters**:
	
		df: pandas.core.Dataframe
			enter the complete dataframe

		col_name: str
		



	**Usage**:
	
		>>> p = process()
		>>> p.is_categorical(df['State'])
		>>> True/False


geocode
----------

        **Parameters**:
            address: str
                Enter a dictionary of address whose latitude and longitude
                should be returned

        **Usage**:
        
            >>> p = preprocess()
            >>> p.geocode("172 5th Avenue NYC")
            >>> {'latitude': 40.74111015, 'adress': u'172, 5th Avenue, Flatiron,
             Manhattan, Manhattan Community Board 5, New York County, NYC,
             New York, 10010, United States of America',
            'longitude': -73.9903105}
