
from typing import Literal, TypeAlias

NULLNotFoundType: TypeAlias = Literal[0, 1]

def NULL_not_found(obj : any) -> NULLNotFoundType:
	type_labels = {
		type(None) : ["Nothing", obj],
		float : ["Cheese", obj],
		int : ["Zero", obj],
		str : ["Empty", obj],
		bool: ["Fake", obj],
	}


	if type(obj) == str and len(obj) > 0:
		print("Type not Found") 
	elif type(obj) in type_labels:
		print(f"{type_labels[type(obj)][0]}: {type_labels[type(obj)][1]} {type(obj)}")
	else:
		print("Type not Found")

	return 1
