import pandas as pd

def diff_df(df1, df2):
    df_out = []

    df1_rows = [str(val.to_dict()) for idx, val in df1.iterrows()]
    df2_rows = [val.to_dict() for idx, val in df2.iterrows()]

    for row in df2_rows:
        if str(row) not in df1_rows:
            df_out.append(row)
    
    df_out = pd.DataFrame(df_out)
    return df_out

df1 = pd.read_excel("Student_results.xlsx")
df2 = pd.read_excel("Student_results1.xlsx")
df_out = diff_df(df1, df2)
df_out.to_excel("New_results.xlsx")