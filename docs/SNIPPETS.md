# This is the snippets file. That contains all the snippets for Versace.
## To install the snippets
1. Open the command palette (Ctrl+Shift+P)
2. Type `Preferences: Configure User Snippets`
3. Select `Versace`
4. Copy the snippets from this file and paste it in the file that opens
5. Save the file
6. Restart VS Code
7. Enjoy!

- Snippets :
```json
{
	// Place your snippets for versace here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	 "create start function": {
	 	"prefix": "pm",
	 	"body": [
	 		"public main()", 
			"{",
	 		"\t$1",
			"}"
	 	],
	 	"description": "Creates the starting function"
	},
	"create function": {
		"prefix": "fn",
		"body": [
			"func ${1:name}()", 
			"{",
			"\t",
			"}"
		],
		"description": "Makes a function"
	},
	"create class": {
		"prefix": "cl",
		"body": [
			"class ${1:name}", 
			"{",
			"\t",
			"}"
		],
		"description": "Creates a class"
	},
	"create if statement": {
		"prefix": "if",
		"body": [
			"if (${1:condition})", 
			"{",
			"\t",
			"}"
		],
		"description": "Creates an if statement"
	},
	"create else statement": {
		"prefix": "el",
		"body": [
			"else",
			"{",
			"\t$1",
			"}"
		],
		"description": "Creates an else statement"
	},
	"create async function": {
		"prefix": "as",
		"body": [
			"async func ${1:name}()",
			"{",
			"\t",
			"}"
		],
		"description": "Makes a function"
	},
	"create else if statement": {
		"prefix": "elif",
		"body": [
			"else if (${1:condition})", 
			"{",
			"\t",
			"}"
		],
		"description": "Creates an else if statement"
	},
	"create for loop": {
		"prefix": "for",
		"body": [
			"for ${1:condition}", 
			"{",
			"\t",
			"}"
		],
		"description": "Creates a for loop"
	},
	"create while loop": {
		"prefix": "wh",
		"body": [
			"while ${1:condition}", 
			"{",
			"\t",
			"}"
		],
		"description": "Creates a while loop"
	},
}
```
