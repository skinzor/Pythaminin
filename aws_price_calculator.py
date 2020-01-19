from termcolor import cprint

price = float(input('Enter Value: '))
cost_daily = (price * 24)
cost_monthly = (cost_daily * 30)
cost_yearly = (cost_monthly * 12)

cprint(f'Cost in 24 Hour/Day    : {cost_daily}', 'green')
cprint(f'Cost in 30 Days/Month  : {cost_monthly}', 'blue')
cprint(f'Cost in 12 Months/Year : {cost_yearly}', 'magenta')
