import json
content = {
  "Employee": {
    "GuidKey": "DAEFB0BC-B260-446E-AFB7-022B64D53660",
    "EmployeeCode": "1020",
    "PayrollCode": "1020"
  },
  "DateActual": "2022-08-28T19:35:16.606Z",
  "StartTime": "2022-08-28T19:35:16.606Z",
  "EndTime": "2022-08-28T21:35:16.606Z",
  "TimeOfBreak": "2022-08-28T20:35:16.606Z",
  "BreakMinutes": 30,
  "Location": {
    "GuidKey": "941C0D5B-7CAE-4B91-B8E1-3613E66C616A",
    "Name": "Parramatta",
    "ShortName": "2222",
    "ExportCode": "2222"
  },
  "Department": {
    "GuidKey": "F9078066-B3AC-4488-80E4-A50364039519",
    "Name": "AUTOMATION_IAIN_TestDepartment",
    "ShortName": "AI_TD",
    "ExportCode": "AI_TD"
  },
  "Role": {
    "GuidKey": "63F2C6AB-B436-46DE-A640-8DE11FDF2F9A",
    "Name": "TESTROLE1",
    "ShortName": "TR",
    "ExportCode": "EXP_TR_01"
  },
  "Period": {
    "GuidKey": "11E1306B-54EB-41F7-BFD9-ED0FCCEA47FD",
    "Name": "1 Test"
  },
  "Area": {
    "GuidKey": "0DA9A9B2-5C17-4644-9C89-47822FFCE65B",
    "Name": "Boardroom",
    "ShortName": "",
    "ExportCode": ""
  },
  "Event": {
    "GuidKey": "FDC8D44E-28FF-4395-A37D-19079A219962",
    "Name": "Test Event ",
    "ShortName": "",
    "ExportCode": ""
  },
  "EventFunction": {
    "GuidKey": "2A557409-6582-4087-85EF-0E7099542D98",
    "Name": "Test Event ",
    "ShortName": "",
    "ExportCode": ""
  },
  "ShiftType": {
    "GuidKey": "D09BD00F-52CE-481B-BD6B-6317B886AC9E",
    "Name": "QA SHIFT TYPE FROM API",
    "ShortName": "",
    "ExportCode": ""
  },
  "ShiftDefinition": {
    "GuidKey": "8D93B020-CFD4-47A1-91D0-A2DB89BC9EC8",
    "Name": "Tuesday",
    "ShortName": "",
    "ExportCode": ""
  },
  "Confirmed": 1,
  "Changed": True,
  "NonAttended": True,
  "Published": True,
  "PublishedBy": {
    "GuidKey": "00000000-0000-0000-0000-000000000000",
    "EmployeeCode": "string",
    "PayrollCode": "string"
  },
  "PublishedAt": "2022-08-28T19:35:16.606Z",
  "ReadOnly": True,
  "ReadOnlySetBy": {
    "GuidKey": "DAEFB0BC-B260-446E-AFB7-022B64D53660",
    "EmployeeCode": "1020",
    "PayrollCode": "1020"
  },
  "ReadOnlySetAt": "2022-08-28T19:35:16.606Z",
  "RosterData1": {
    "GuidKey": "00000000-0000-0000-0000-000000000000",
    "Name": "string",
    "ShortName": "string",
    "ExportCode": "string"
  },
  "RosterData2": {
    "GuidKey": "00000000-0000-0000-0000-000000000000",
    "Name": "string",
    "ShortName": "string",
    "ExportCode": "string"
  },
  "RosterData3": {
    "GuidKey": "00000000-0000-0000-0000-000000000000",
    "Name": "string",
    "ShortName": "string",
    "ExportCode": "string"
  },
  "Comments": "Testing"
}
print(json.dumps(content))