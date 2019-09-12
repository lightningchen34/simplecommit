import os

def commit(type, subject, issue=""):
	issue_msg = ""
	if issue is not "":
		issue_msg = " #" + str(issue)
	message = "git commit -m \"{}: {}{}\"".format(type, subject, issue_msg)
	os.system(message)

def _run():
	print("type of commit: ")
	print("\t1. build -- changes that affect the build system or external dependencies")
	print("\t2. docs -- documentation only changes")
	print("\t3. feat -- a new feature")
	print("\t4. fix -- a bug fix")
	print("\t5. refactor -- a code change that nerther fixes a bug nor adds a feature")
	print("\t6. style -- changes that do not affect the meaning of the code")
	print("\t7. test -- adding missing tests or correcting existing tests")
	print("\t8. revert -- reverting a previous commit")
	print("")
	print("provisions of subject:")
	print("\t1. use the imperative, present tense: \"change\" not \"changed\" nor \"changes\"")
	print("\t2. don't capitalize the first letter")
	print("\t3. no dot (.) at the end")
	print("")
	
	type = 0
	while True:
		try:
			number = int(input("input the index of type: "))
			if number >= 1 and number <= 7:
				type = number
				break
		except Exception as e:
			pass
		else:
			pass
		finally:
			pass
		print("illegal input")

	subject = input("input subject of commit: ")
	issue = input("issue(no input for none): ")
	types = ["", "build", "docs", "feat", "fix", "refactor", "style", "test", "revert"]
	commit(types[type], subject, issue)

def run():
	try:
		_run()
	except KeyboardInterrupt as e:
		pass
