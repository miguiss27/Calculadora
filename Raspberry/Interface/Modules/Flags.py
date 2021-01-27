#flags list

flags  = {
	"embedded":False,
	"tableMode":False, 
	"execMode":False,
	"keyboardMode":False,
	"graphicsMode":False,
}


#Dictionary for resolving flags

flagDictionary = {
	"table mode": "tableMode",
	"exec mode":"execMode"",
	"raw key mode": "keyboardMode",
	"graphics mode": "graphicsMode",
}

#Dictionary to change flag dependent flags

flagResolution = {
	"tableMode":["embedded"],
}

#processing flags utility

def processFlags(cmd, flags):
	#get flag name
	flag = flagDictionary[cmd]

	#get flag dependencies
	flagDependencies = []

	if (flag in flagResolution):
		for dependence in flagResolution[flag]:
			flagDependencies.append(dependence)
	
	#change flag state
	flags[flag] = not(flags[flag])

	#change flag dependencies state
	if ((flag in flagResolution) and (flag != "tableMode")):
		for dependence in flagDependencies:
			flags[dependence] = not(flags[dependence])

	#fix for tableMode exception
	if ((flag == "tableMode") and (flags["embedded"])):
		flags[flag] = False
		flags["embedded"] = False
	

	return flags
