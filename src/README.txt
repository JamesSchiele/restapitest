# ACUPAY Python REST API

## Usage

All responses will have the form

''' json
{
	"data": "Mixed type holding the content of the response"
	"message": "Description of what happened"
}
'''

Subsequent response definitions will only detail the excepted value of the 'data field'

### List name, date of birthday, age and favourite_animal of team

**Definitions**

'GET /team'

**Response**

- '200 OK'

'''json
[
	{
		"name": "John Parker"
		"birthday": "21st February 1981"
		"age": "41"
		"favourite_animal": "axolotl"
	}
]
,,,

### Registering a new team member

**Definitions**

'POST /team'

**Arguments**

- '"name":string' the full name of the team member
- '"birthday":string' the birth date of the team member
- '"age":int' the number of years since the birth date of the team member
- '"favourite_animal:string' the favourite_animal of the team member

If a team member with the exact name already exists, the existing team member will be overwritten

**Response**

- '201 Created' on success

'''json
	{
		"name": "John Parker"
		"birthday": "21st February 1981"
		"age": "41"
		"favourite_animal": "axolotl"
	}
'''

## Look-up team member details

'GET /team/<name>'

**Response**

-'404 Not Found' if the team member does not existing
- '200 OK' on success

'''json
'''