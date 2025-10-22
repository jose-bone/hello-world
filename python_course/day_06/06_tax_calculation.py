#%%
def tax_calc(price:float, base_tax:float, **kwargs):
    tax = price * base_tax

    for i in kwargs:
        print(i, kwargs[i])
        tax += price * kwargs[i]
    
    return tax

#%%
general_taxes = {
    "state":0.003,
    "national":0.001
}

tax_calc(100, 0.05, **general_taxes, international=0.00002)