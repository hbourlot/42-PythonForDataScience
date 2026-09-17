import numpy as np

def slice_me(family: list, start: int, end: int) -> list:

	total_len = len(family)
	block_len = len(family[0])

	family_np = 0
 
	try:
		family_np = np.array(family)[start:end]

		print(f"My shape is : ({total_len}, {block_len})")
		print(f"My new shape is : ({len(family_np)}, {block_len})")
	except:
		return [];
		
 
	return family_np