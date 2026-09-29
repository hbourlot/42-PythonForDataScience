
def all_thing_is_obj(object: any) -> int:
	type_labels = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
	}

	if (isinstance(object, str)):
		print(f"{object} is in the kitchen : {type(object)}")
	elif (type(object) in type_labels):
		print(f"{type_labels[type(object)]} : {type(object)}")
	else:
		print("Type not found")

	return 42

