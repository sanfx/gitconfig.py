Installing
----------

	sudo pip install GitPython # requires
	sudo pip install gitconfig


Usage
----------

	import gitconfig
	config=gitconfig.config("~/.gitconfig")
	print config.user.name, config.user.email
	print config.list
	config.set("section","key","value")
    print config.get("section","key")
    config.unset("section","key")
    # shorthands:
    config.section.key="value"
	print config.section.key
	>>> "value"