ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

def replace_list(replace : str):
	ft_list[1] = replace

def replace_tuple(replace: str):
	global ft_tuple
	my_list = list(ft_tuple)
	my_list[1] = replace
	ft_tuple = tuple(my_list)

def replace_set(replace: str):
	global ft_set
	
	ft_set.remove("tutu!")
	ft_set.add(replace)

def replace_dict(replace: str) -> void:
	ft_dict["Hello"] = replace

replace_list("World")
replace_tuple("Portugal")
replace_set(" Lisbon")
replace_dict("42Lisbon")

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
