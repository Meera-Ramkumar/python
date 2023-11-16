def test_function(content):
	print(f'this is an imported function with the parameter:{content}')


test_var='test'
def sum_calculator(*nums):
	return sum(nums)

print(__name__)	