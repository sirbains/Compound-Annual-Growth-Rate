def calc_cagr(initial_value, final_value, years):
  """
  Calculates the compound annual growth rate (CAGR) of an investment.
  
  Parameters:
  initial_value (float): the initial value of the investment
  final_value (float): the final value of the investment
  years (float): the number of years over which the investment was held
  
  Returns:
  float: the compound annual growth rate of the investment
  """
  return (final_value / initial_value) ** (1 / years) - 1

# Example usage
initial_value = 1000
final_value = 1500
years = 5
cagr = calc_cagr(initial_value, final_value, years)
print(f"The CAGR of the investment is {cagr:.2f}%")
