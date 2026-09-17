def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	result = []

	len_h = len(height)
	len_w = len(weight)

	if len_h != len_w:
		return result

	try:
		for i in range(len_h):
			if (i >= len(weight)):
				break
			result.append(weight[i] / (height[i] ** 2))
	except TypeError, ZeroDivisionError:
		return []
		
	return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

	result = []

	try:
		for item in bmi:
			result.append(item > limit)
	except TypeError:
		return []

	return result;
