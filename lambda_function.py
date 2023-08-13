import pandas as pd

def lambda_handler(event, context):
    d = {'Col_Number1': [1, 2], 'Col_Number2': [3, 4]}
    df = pd.DataFrame(data=d)
    
    # Adding more columns to the DataFrame
    df['Col_Number3'] = [5, 6]
    df['Col_Number4'] = [7, 8]
    df['Col_Number5'] = [9, 10]
    df['Col_Number6'] = [11, 12]
    
    
    print("Modified DataFrame:")
    print(df)
    
    print('Finished')
