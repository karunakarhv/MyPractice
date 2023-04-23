from jsonschema import validate

GET_EMP_RESPONSE = {
    "data": {
        "employees": [
            {
                "guidKey": "5eb24667-bea9-4ec8-8d4e-76456f57eebc",
                "employeeCode": "1234568210",
                "payrollCode": "104",
                "nameFirst": "Anna",
                "nameFamily": "Bliss",
                "dOB": "1976",
                "dateEnd": "123"
            },
            {
                "guidKey": "5eb24667-bea9-4ec8-8d4e-76456f57eebc",
                "employeeCode": "1234568210",
                "payrollCode": "105",
                "nameFirst": "Test",
                "nameFamily": "Bliss",
                "dOB": "1976-06-04",
                "dateEnd": "123"
            }
        ]
    }
}
# Generate JSON Schema:https://extendsclass.com/json-schema-validator.html
GET_EMP_SCHEMA = {
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#",
	"$id": "https://example.com/object1681871603.json",
	"title": "Root",
	"type": "object",
	"required": [
		"data"
	],
	"properties": {
		"data": {
			"$id": "#root/data",
			"title": "Data",
			"type": "object",
			"required": [
				"employees"
			],
			"properties": {
				"employees": {
					"$id": "#root/data/employees",
					"title": "Employees",
					"type": "array",
					"default": [],
					"items":{
						"$id": "#root/data/employees/items",
						"title": "Items",
						"type": "object",
						"required": [
							"guidKey",
							"employeeCode",
							"payrollCode",
							"nameFirst",
							"nameFamily",
							"dOB",
							"dateEnd"
						],
						"properties": {
							"guidKey": {
								"$id": "#root/data/employees/items/guidKey",
								"title": "Guidkey",
								"type": "string",
								"default": "",
								"examples": [
									"5eb24667-bea9-4ec8-8d4e-76456f57eebc"
								],
								"pattern": "^.*$"
							},
							"employeeCode": {
								"$id": "#root/data/employees/items/employeeCode",
								"title": "Employeecode",
								"type": "string",
								"default": "",
								"examples": [
									"1234568210"
								],
								"pattern": "^.*$"
							},
							"payrollCode": {
								"$id": "#root/data/employees/items/payrollCode",
								"title": "Payrollcode",
								"type": "string",
								"default": "",
								"examples": [
									"104"
								],
								"pattern": "^.*$"
							},
							"nameFirst": {
								"$id": "#root/data/employees/items/nameFirst",
								"title": "Namefirst",
								"type": "string",
								"default": "",
								"examples": [
									"Anna"
								],
								"pattern": "^.*$"
							},
							"nameFamily": {
								"$id": "#root/data/employees/items/nameFamily",
								"title": "Namefamily",
								"type": "string",
								"default": "",
								"examples": [
									"Bliss"
								],
								"pattern": "^.*$"
							},
							"dOB": {
								"$id": "#root/data/employees/items/dOB",
								"title": "Dob",
								"type": "string",
								"default": "",
								"examples": [
									"1976-06-04"
								],
								"pattern": "^.*$"
							},
							"dateEnd": {
								"$id": "#root/data/employees/items/dateEnd",
								"title": "Dateend",
								"type": "string",
								"default": "",
								"examples": [
									"123"
								],
								"pattern": "^.*$"
							}
						}
					}

				}
			}
		}

	}
}

print(validate(instance=GET_EMP_RESPONSE, schema=GET_EMP_SCHEMA))