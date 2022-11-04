def calculate_std_range(df,column,FACTOR=3):
   col_std  = df[column].std() 
   col_mean = df[column].mean()
   col_min_range = col_mean - col_std * FACTOR
   col_max_range = col_mean + col_std * FACTOR
   df = df[(df[column]>=col_min_range) & (df[column]<=col_max_range) ]
   return df
