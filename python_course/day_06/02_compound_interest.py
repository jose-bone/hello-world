#%%
def compound_interest(contribution:int, fee:float, years:int)->float:
    return contribution * (1 + fee) ** years

#%%
compound_interest(fee=0.13, years=5, contribution=1000)