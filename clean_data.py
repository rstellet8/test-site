import pandas as pd


EXP_PATH = "data/export.csv"
IMP_PATH = "data/import.xlsx"
SAL_PATH = "data/sales.csv"

def clean_data(exp_path=EXP_PATH, imp_path=IMP_PATH, sal_path=SAL_PATH):
    """
    ### Summary
    Limpa os dados das planilhas export.csv, import.xlsx e sales.csv.\ 
    Os dataframes são retornados no seguinte formato:
    #### Exp:
    | name | variable | value
    |---|---|---|  
    | Benin | code | BEN 
    | Burkina Faso | code | BFA
    | Bangladesh | code | BGD 
    | Bulgaria | code | BGR 
    | Bahrain | code | BHR 

    #### Imp:
    | name | variable | value
    |---|---|---
    | Aruba | code | ABW
    | Andorra | code | AND
    | Afghanistan | code | AFG
    | Angola | code | AGO
    | Albania | code | ALB

    #### Sal:
    | id | region | variable | value
    |---|---|---|---
    | 1 | AUH | JANUARY | 3469
    | 1	| SHJ | JANUARY | 5840
    | 2 | AUH | JANUARY | 1328
    | 3 | SHJ | JANUARY | 2473
    | 3 | AUH | JANUARY | 2634

    ### Parameters
    - exp_path(str): path pra export.csv
    - imp_path(str): path pra import.xlsx
    - sal_path(str): path pra sales.csv

        Por padrão os arquivos serão buscados na pasta data.
    
    ### Returns:
    - tupla: (exp, imp, sal) \ 
        Onde cada valor é um DataFrame(pandas)

        """
    exp = (
        pd.read_csv(EXP_PATH)
        .rename(columns={"Country Name": "name", "Country Code": "code"})
        .melt(id_vars="name")
        )


    imp = (
        pd.read_excel(IMP_PATH, engine="openpyxl")
        .rename(columns={"Country Name": "name", "Country Code": "code"})
        .melt(id_vars="name")
        )


    sal = (
        pd.read_csv(SAL_PATH)
        .rename(columns={
            "SALES_ID": "id",
            "SALES_BY_REGION": "region"
        })
        .melt(id_vars=["id", "region"])
        )

    sal["value"] = sal["value"].apply(lambda x: x.replace(".00", "").replace(",", ""))

    sal = sal.query("region != '-1'    and region != 'not avilable'    and value != 'n.a.'    and value != '-1'    and value != 'not avilable'"
        )

    pd.to_numeric(sal["value"])

    return exp, imp, sal

if __name__ == "__main__":
    exp, imp, sal = clean_data()
    print(exp.head(10))
    print(imp.head(10))
    print(sal.head(10))