import datetime


def main() -> None:
	start = datetime.datetime(1970, 1, 1)
	now = datetime.datetime.now()

	diff = now - start

	print(f"Seconds since January 1, 1970 : {diff.total_seconds():,.4f} or {diff.total_seconds():e} in scientific notation")
	print(f"{now.strftime("%b %d %Y")}")


if __name__=="__main__":
	main()