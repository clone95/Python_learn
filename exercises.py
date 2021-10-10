import cryptocompare

portfolio_allocation = {"BTC": 0.7, "ETH": 0.2, "DOT": 0.1}
capital = 2000
n_steps = 34


def calculate_final_allocation(capital, portfolio_allocation):
    return {x : ( capital * portfolio_allocation[x] ) for x in portfolio_allocation }


def one_step_buy_size(capital, n_steps, portfolio_allocation):
    final_sizes = calculate_final_allocation(capital, portfolio_allocation)
    return {x: final_sizes[x] / n_steps    for x in portfolio_allocation}


def apply_asset_change(portfolio, asset_to_remove, asset_to_insert, n_steps, percentage_change = 0.3):
    # {'BTC': 70, 'ETH': 20, 'DOT': 10}  ->  {'BTC': 70, 'ETH': 20, 'LUNA': 10}
    
    prices = {asset_to_remove: cryptocompare.get_price(asset_to_remove, 'USD')[asset_to_remove]["USD"],
     asset_to_insert: cryptocompare.get_price(asset_to_insert, 'USD')[asset_to_insert]["USD"]} 
    try:
        if percentage_change == 1:
            one_step_sell_size = portfolio[asset_to_remove] / n_steps 
            size_in_usdt = one_step_sell_size * prices[asset_to_remove]
            one_step_buy_size = size_in_usdt / prices[asset_to_insert]
            
            print(f"you have to sell {round(one_step_sell_size, 2)} units of {asset_to_remove} and " +
                        f"buy {round(one_step_buy_size, 2)} units of {asset_to_insert}")
        else:
            one_step_sell_size = portfolio[asset_to_remove] * percentage_change / n_steps 
            size_in_usdt = one_step_sell_size * prices[asset_to_remove]
            one_step_buy_size = size_in_usdt / prices[asset_to_insert]
            
            print(f"you have to sell {round(one_step_sell_size, 2)} units of {asset_to_remove} and " +
                        f"buy {round(one_step_buy_size, 2)} units of {asset_to_insert}")
    except Exception as e:
        print(f"The asset {e} is not present in the portfolio")
        return None

    return one_step_sell_size, one_step_buy_size


portfolio = calculate_final_allocation(capital, portfolio_allocation)
apply_asset_change (portfolio, "BTC", "ETH", 15)