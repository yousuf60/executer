from time import sleep
def a():
	while True:

		try:
			with open("main.py") as code:
				exec(code.read())
		except Exception as ex:print(ex)

		sleep(3)

a()