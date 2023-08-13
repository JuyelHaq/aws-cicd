import pandas as pd

def lambda_handler(event, context):
    d = {'Col_Number1': [1,2], 'Col_Number2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Finished')