#key mapping

keys = {
	'1':0,'2':1,'3':2,'4':3,
	'q':4,'w':5,'e':6,'r':7,
	'a':8,'s':9,'d':10,'f':11,
	'z':12,'x':13,'c':14,'v':15

}


#menu dictionaries

menu0 = {
	0:"quit",1:"basic",2:"keyboard",3:"next",
	4:"delete",5:"clear",6:"clear result",7:"execute",
	8:"table mode",9:"raw key mode",10:"var assign mode",11:"graphics mode",
	12:"none",13:"none",14:"none",15:"none"
}

menu1 = {
	0:"back",1:"none",2:"none",3:"none",
	4:"none",5:"none",6:"none",7:"none",
	8:"none",9:"none",10:"none",11:"none",
	12:"desktop",13:"shutdown",14:"reboot",15:"kodi"
}

menu2 = {
	0:"back",1:"a",2:"b",3:"next",
	4:"c",5:"d",6:"e",7:"f",
	8:"g",9:"h",10:"i",11:"j",
	12:"k",13:"l",14:"m",15:"n"
}

menu3 = {
	0:"back",1:"o",2:"p",3:"next",
	4:"q",5:"r",6:"s",7:"t",
	8:"u",9:"v",10:"w",11:"x",
	12:"y",13:"z",14:"space",15:"^"
}

menu4 = {
	0:"back",1:"¿",2:"?",3:"next",
	4:";",5:"#",6:"¡",7:"@",
	8:"none",9:"none",10:"none",11:"none",
	12:"none",13:"none",14:"none",15:"none"
}

menu5 = {
	0:"back",1:"+",2:"-",3:"next",
	4:"0",5:"1",6:"2",7:"3",
	8:".",9:"4",10:"5",11:"6",
	12:"=",13:"7",14:"8",15:"9"
}

menu6 = {
	0:"back",1:"/",2:"*",3:"next",
	4:"**",5:"%",6:"(",7:")",
	8:",",9:"π",10:"ϵ",11:"!",
	12:"√",13:"sin(",14:"cos(",15:"tan("
}

menu7 = {
	0:"back",1:"min(",2:"max(",3:"next",
	4:"MCM(",5:"MCD(",6:"∞",7:"abs(",
	8:"degrees(",9:"radians(",10:"log(",11:"log10(",
	12:"*(10**",13:"asin(",14:"acos(",15:"atan("
}


menu8 = {
	0:"back",1:"[",2:"]",3:"next",
	4:"<",5:">",6:"{",7:"}",
	8:"&",9:"|",10:"\"",11:'\'',
	12:"none",13:"none",14:"none",15:"none"
}

#dictionary of menu dictionaries

menuDict = {
	"menu0":menu0,
	"menu1":menu1,
	"menu2":menu2,
	"menu3":menu3,
	"menu4":menu4,
	"menu5":menu5,
	"menu6":menu6,
	"menu7":menu7,
	"menu8":menu8,
}


#menu redirections

redirections = {
	"menu":{
		"basic":menu5,
		"keyboard":menu2,
	},

	"back":{
		"menu1":menu0,
		"menu2":menu0,
		"menu3":menu2,
		"menu4":menu3,
		"menu5":menu0,
		"menu6":menu5,
		"menu7":menu6,
		"menu8":menu7,
	},

	"next":{
		"menu0":menu1,
		"menu2":menu3,
		"menu3":menu4,
		"menu5":menu6,
		"menu6":menu7,
		"menu7":menu8,
	}
}

#menu expressions that are needed to replace in the menu

menuReplace = {
	"back":"",
	"next":"",
	"none":"",
	"space":" "
}


#menu expressions that are needed to replace when executing

execReplace = {
	"√":"sqrt(",
	"π":"pi",
	"ϵ":"e",
	"!":"factorial(",
	"MCM(":"lcm(",
	"MCD(":"gcd(",
	"abs(":"fabs(",
	"max(":"floor(",
	"min(":"ceil(",
}

#dictionary containin all external comands and their alias

externalComands = {
	"desktop":["startx"],
	"kodi":["kodi"],
	"shutdown":["shutdown","now"],
	"reboot":["reboot"]
}
