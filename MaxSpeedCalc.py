import pandas as pd
import numpy as np
import sys
import datetime as dt

def calc_esno(small_df, val):
    prev = small_df.iloc[0]
    if val<prev[-1]:
        return 0
    for i in small_df.index[1:]:
        if small_df.iloc[i,-1]!=255.0:
            if small_df.iloc[i,-1]>val:
                return prev["esno"]
            prev = small_df.iloc[i]
    return prev["esno"]

def map_tier(speed):
    if speed >= 35:
        return "Tier 1"
    elif speed >= 25:
        return "Tier 2"
    elif speed >= 20:
        return "Tier 3"
    elif speed >= 15:
        return "Tier 4"
    elif speed >= 10:
        return "Tier 5"
    elif speed >= 5:
        return "Tier 6"
    elif speed >= 3:
        return "Tier 7"
    elif speed >=0:
        return "Tier 8"
    else:
        print (speed, "; Max Speed is below 0, Tier 8 was assigned")
        return "Tier 8"


if __name__=="__main__":
    path = sys.argv[1]
    print (path)
    ### Tables ####
    # Link Budget Table named df#
    df = pd.read_excel(path, sheet_name="J3Rtn_LinkBudget")
    # Trajectory Table named trajectory#
    trajectory = pd.read_excel(path, sheet_name="TrajectoryTable")
    # L2 Efficiency Table named L2E#
    L2E = pd.read_excel(path, sheet_name="L2EfficiencyMulti")
    # L3 Efficiency Table named L3E#
    L3E = pd.read_excel(path, sheet_name="L3EfficiencyMulti")

    ### Constant lists/pd.DataFrame ###

    # The column name where 'Msps' cell is located
    col_msps = df.columns[df.eq("Msps").any(axis=0)][0]

    # The row number where 'Msps' cell is located
    row_msps = df[df.eq("Msps").any(axis=1)][df.columns[df.eq("Msps").any(axis=0)][0]].index[0]

    # Computing of the Msps values in variable named msps_values, assume there is a blank cell after the last Msps value.
    x=1
    msps_values = np.array([])
    temp_values = np.array([])
    while df.iloc[row_msps,df.columns.get_indexer([col_msps])+x][0] is not np.nan:
        msps_values = np.append(msps_values, df.iloc[row_msps,df.columns.get_indexer([col_msps])+x][0])
        x+=1

    # enso_dict: Dictionary of DataFrames with esno info for each mod.
    esno_dict = {}
    for mod in trajectory["mod"].drop_duplicates().dropna():
        esno_info = pd.DataFrame()
        esno_info["esno"] = trajectory.loc[trajectory["Title"]=="FEC Multiplier",
                       ["1/2 FEC EsNo target", "2/3 FEC EsNo target", "4/5 FEC EsNo target", "8/9 FEC EsNo target",
                        "9/10 FEC EsNo target"]].values[0]
        for x in msps_values:
            esno_info[x] = trajectory.loc[(trajectory["Title"]==x) & (trajectory["mod"]==mod),
                ["1/2 FEC EsNo target", "2/3 FEC EsNo target", "4/5 FEC EsNo target", "8/9 FEC EsNo target",
                 "9/10 FEC EsNo target"]].values[0]
        esno_dict[mod] = esno_info

    # l2e_dict/l3e_dict: Dictionary of DataFrames with l2/l3 Efficiency info for each mod.
    l2e_dict = {}
    for mod in L2E["mod"].drop_duplicates().dropna():
        l2e_info = pd.DataFrame()
        l2e_info["esno"] = L2E.loc[L2E["Title"]=="FEC Multiplier",
                       ["1/2 FEC EsNo target", "2/3 FEC EsNo target", "4/5 FEC EsNo target", "8/9 FEC EsNo target",
                        "9/10 FEC EsNo target"]].values[0]
        for x in msps_values:
            l2e_info[x] = L2E.loc[(L2E["Title"]==x) & (L2E["mod"]==mod),
                ["1/2 FEC EsNo target", "2/3 FEC EsNo target", "4/5 FEC EsNo target", "8/9 FEC EsNo target",
                 "9/10 FEC EsNo target"]].values[0]
        l2e_dict[mod] = l2e_info

    l3e_dict = {}
    for mod in L3E["mod"].drop_duplicates().dropna():
        l3e_info = pd.DataFrame()
        l3e_info["esno"] = L3E.loc[L3E["Title"]=="FEC Multiplier",
                       ["1/2 FEC EsNo target", "2/3 FEC EsNo target", "4/5 FEC EsNo target", "8/9 FEC EsNo target",
                        "9/10 FEC EsNo target"]].values[0]
        for x in msps_values:
            l3e_info[x] = L3E.loc[(L3E["Title"]==x) & (L3E["mod"]==mod),
                ["1/2 FEC EsNo target", "2/3 FEC EsNo target", "4/5 FEC EsNo target", "8/9 FEC EsNo target",
                 "9/10 FEC EsNo target"]].values[0]
        l3e_dict[mod] = l3e_info
    ###################################################################################################################
    res = pd.DataFrame()
    res[df.iloc[row_msps + 1, df.columns.get_indexer([col_msps]) - 5]] = df.iloc[row_msps + 2:,
                                                                         df.columns.get_indexer([col_msps]) - 5]
    res[df.iloc[row_msps + 1, df.columns.get_indexer([col_msps]) - 4]] = df.iloc[row_msps + 2:,
                                                                         df.columns.get_indexer([col_msps]) - 4]
    res[df.iloc[row_msps + 1, df.columns.get_indexer([col_msps]) - 3]] = df.iloc[row_msps + 2:,
                                                                         df.columns.get_indexer([col_msps]) - 3]
    res[df.iloc[row_msps + 1, df.columns.get_indexer([col_msps]) - 2]] = df.iloc[row_msps + 2:,
                                                                         df.columns.get_indexer([col_msps]) - 2]
    res[df.iloc[row_msps + 1, df.columns.get_indexer([col_msps]) - 1]] = df.iloc[row_msps + 2:,
                                                                         df.columns.get_indexer([col_msps]) - 1]
    res["temp_values"] = df.iloc[row_msps + 2:,
                         df.columns.get_indexer([col_msps])[0] + 1:df.columns.get_indexer([col_msps])[
                                                                       0] +11].values.tolist()

    calc = pd.DataFrame()
    calc["msps"] = msps_values
    mods = trajectory["mod"].drop_duplicates().dropna()
    for mod in mods:
        calc["bps_multi_{}".format(mod)] = calc["msps"].apply(
            lambda x: trajectory["bps multi"][(trajectory["Title"] == x) & (trajectory["mod"] == mod)].values[0])
        calc["backoff_{}".format(mod)] = calc["msps"].apply(lambda x: trajectory["EsNo Backoff (Linear)"][
            (trajectory["Title"] == x) & (trajectory["mod"] == mod)].values[0])
    l2e_dict2 = {}
    for mod in L2E["mod"].drop_duplicates().dropna():
        for col in ["1/2 FEC EsNo target", "2/3 FEC EsNo target", "4/5 FEC EsNo target", "8/9 FEC EsNo target",
                    "9/10 FEC EsNo target"]:
            for x in msps_values:
                l2e_dict2[(mod, L2E.loc[L2E["Title"] == "FEC Multiplier", col].values[0], x)] = \
                L2E[col][(L2E["Title"] == x) & (L2E["mod"] == mod)].values[0]

    l3e_dict2 = {}
    for mod in L3E["mod"].drop_duplicates().dropna():
        for col in ["1/2 FEC EsNo target", "2/3 FEC EsNo target", "4/5 FEC EsNo target", "8/9 FEC EsNo target",
                    "9/10 FEC EsNo target"]:
            for x in msps_values:
                l3e_dict2[(mod, L3E.loc[L3E["Title"] == "FEC Multiplier", col].values[0], x)] = \
                    L3E[col][(L3E["Title"] == x) & (L3E["mod"] == mod)].values[0]

    def calc_f(temp_values):
        calc["temp_value"] = temp_values
        for mod in mods:
            calc["esno_value_{}".format(mod)] = calc.apply(
                lambda x: calc_esno(esno_dict[mod][["esno", x["msps"]]], x["temp_value"] - x["backoff_{}".format(mod)]), axis=1)
            calc["speed_{}".format(mod)] = calc.apply(
                lambda x: 0 if x["esno_value_{}".format(mod)]==0 else x["msps"] * x["esno_value_{}".format(mod)] * x["bps_multi_{}".format(mod)] *
                          l2e_dict2[(mod, x["esno_value_{}".format(mod)], x["msps"])] * l3e_dict2[(mod, x["esno_value_{}".format(mod)], x["msps"])], axis=1)
        max_val=calc[["speed_{}".format(mod) for mod in mods]].to_numpy().max()
        max_col = calc.columns[calc.eq(max_val).any(axis=0)][0]
        max_mod = max_col[max_col.find("_")+1:]
        mask = calc[max_col]==max_val
        to_ret = max_val, (calc["msps"][mask].values[0], calc["esno_value_{}".format(max_mod)][mask].values[0], max_mod)
        return to_ret

    res["Max Speed Symbol, Esno rate, mod"] = res["temp_values"].apply(calc_f)
    res["Max Speed"] = res["Max Speed Symbol, Esno rate, mod"].apply(lambda x: x[0])
    res["Max Speed Symbol, Esno rate, mod"] = res["Max Speed Symbol, Esno rate, mod"].apply(lambda x: x[1])
    res.drop("temp_values", inplace=True, axis=1)
    res.to_csv("results2.csv")

    rtn_tier = pd.DataFrame(
        columns=["Tiers", "Contents of Tier", "% of Area in Tier", "% of Area that can be hit at least this tier",
                 "Color of Tier"])
    rtn_tier["Tiers"] = ["Tier 1", "Tier 2", "Tier 3", "Tier 4", "Tier 5", "Tier 6", "Tier 7", "Tier 8"]
    rtn_tier["Contents of Tier"] = [">=35", "35 to 25", "25 to 20", "20 to 15", "15 to 10", "10 to 5", "5 to 3",
                                    "3 to 0"]
    rtn_tier["Color of Tier"] = ["#016B04", "#01CB06", "#B7FE1A", "#FFFF00", "#FFC000", "#A47D00", "#FF0000", "#C00000"]
    rtn_tier
    res["tier"] = res["Max Speed"].apply(map_tier)
    sr = res["tier"].value_counts() / res["tier"].count()

    for tier in rtn_tier["Tiers"]:
        if tier not in sr.index:
            sr[tier] = 0.0










# x=1
# while df.iloc[row_msps,df.columns.get_indexer([col_msps])+x][0] is not np.nan:
#     temp_values = np.append(temp_values, df.iloc[row_msps+2 ,df.columns.get_indexer([col_msps])+x][0])
#     x+=1