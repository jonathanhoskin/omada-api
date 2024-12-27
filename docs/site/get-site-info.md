## Get site info


**Url**:`/openapi/v1/{omadacId}/sites/{siteId}`


**Method**:`GET`


**produces**:`application/x-www-form-urlencoded`


**consumes**:`*/*`


**description**:<p>Get site info<br/><br/>The interface requires one of the permissions: <br/>Global Dashboard Manager View Only<br/><br/>The possible error code for the interface in the returned body is one of the following error codes (non generic error codes): <br/>-1300  -  Failed to get site information.</p>



**Params**:


**Params**:


| name | description | in    | require | type | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|omadacId|Omada ID|path|true|string||
|siteId|Site ID|path|true|string||


**status**:


| code | description | schema |
| -------- | -------- | ----- |
|200|OK|OperationResponseSiteEntity|


**Responses**:


| name | description | type | schema |
| -------- | -------- | ----- |----- |
|errorCode||integer(int32)|integer(int32)|
|msg||string||
|result||SiteEntity|SiteEntity|
|&emsp;&emsp;siteId|Site ID|string||
|&emsp;&emsp;name|Name of the site should contain 1 to 64 characters.|string||
|&emsp;&emsp;type|Type of the site should be 0 or 1, and 0 means basic site, 1 means pro site.|integer(int32)||
|&emsp;&emsp;tagIds|Site tag ID|array|string|
|&emsp;&emsp;region|Country/Region of the site; For the values of region, refer to the abbreviation of the ISO country code; For example, you need to input "United States" for the United States of America.|string||
|&emsp;&emsp;timeZone|For the values of the timezone of the site, refer to section 5.1 of the Open API Access Guide.|string||
|&emsp;&emsp;ntpEnable|NTP server status of the site|boolean||
|&emsp;&emsp;ntpServers|NTP server address; Up to 5 entries are allowed for the NTP server address list.|array|string|
|&emsp;&emsp;dst|Daylight Saving Time config of the site|DstDTO|DstDTO|
|&emsp;&emsp;&emsp;&emsp;enable|DST config status; If false, other parameters are not required.|boolean||
|&emsp;&emsp;&emsp;&emsp;start|DST end time config|DstTimeDTO|DstTimeDTO|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;month|Month of the DST config should be a value as follows: 1: January; 2: February; 3: March; 4: April; 5: May; 6: June; 7: July; 8: August; 9: September; 10: October; 11: November; 12: December.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;serial|Week of the DST config should be a value as follows: 1: 1st; 2: 2nd; 3: 3rd; 4: 4th; 5: Last.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;day|Day of the DST config should be a value as follows: 1: Monday; 2: Tuesday; 3: Wednesday; 4: Thursday; 5: Friday; 6: Saturday; 7: Sunday.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour|Hour of the DST config should be within the range of 0–23.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute|Minute of the DST config should be within the range of 0–59.|integer||
|&emsp;&emsp;&emsp;&emsp;end|DST end time config|DstTimeDTO|DstTimeDTO|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;month|Month of the DST config should be a value as follows: 1: January; 2: February; 3: March; 4: April; 5: May; 6: June; 7: July; 8: August; 9: September; 10: October; 11: November; 12: December.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;serial|Week of the DST config should be a value as follows: 1: 1st; 2: 2nd; 3: 3rd; 4: 4th; 5: Last.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;day|Day of the DST config should be a value as follows: 1: Monday; 2: Tuesday; 3: Wednesday; 4: Thursday; 5: Friday; 6: Saturday; 7: Sunday.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour|Hour of the DST config should be within the range of 0–23.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute|Minute of the DST config should be within the range of 0–59.|integer||
|&emsp;&emsp;&emsp;&emsp;status|DST available status|boolean||
|&emsp;&emsp;&emsp;&emsp;startTime|The timeStamp of the DST available start time|integer||
|&emsp;&emsp;&emsp;&emsp;endTime|The timeStamp of the DST available end time|integer||
|&emsp;&emsp;&emsp;&emsp;offset|DST offset config(Unit: ms); It should be a value as follows: [1800000, 3600000, 5400000, 7200000].|integer||
|&emsp;&emsp;&emsp;&emsp;nextStart|The timeStamp of the DST start time of the next year(Unit: ms)|integer||
|&emsp;&emsp;&emsp;&emsp;nextEnd|The timeStamp of the DST end time of the next year(Unit: ms)|integer||
|&emsp;&emsp;&emsp;&emsp;timeZone|Timezone of the site|string||
|&emsp;&emsp;&emsp;&emsp;lastStart|The timeStamp of the DST start time of the last year(Unit: ms)|integer||
|&emsp;&emsp;&emsp;&emsp;lastEnd|The timeStamp of the DST end time of the last year(Unit: ms)|integer||
|&emsp;&emsp;scenario|For the values of the scenario of the site, refer to result of the interface for Get scenario list.|string||
|&emsp;&emsp;longitude|Longitude of the site should be within the range of -180 - 180.|number(double)||
|&emsp;&emsp;latitude|Latitude of the site should be within the range of -90 - 90.|number(double)||
|&emsp;&emsp;address|Address of the site|string||
|&emsp;&emsp;supportES|Whether the site supports adopting Easy Managed switches|boolean||
|&emsp;&emsp;supportL2|Whether the site supports adopting Smart+ or L2+ or L3 switches|boolean||


**Response Sample**:
```javascript
{
	"errorCode": 0,
	"msg": "",
	"result": {
		"siteId": "",
		"name": "",
		"type": 0,
		"tagIds": [],
		"region": "",
		"timeZone": "",
		"ntpEnable": true,
		"ntpServers": [],
		"dst": {
			"enable": true,
			"start": {
				"month": 0,
				"serial": 0,
				"day": 0,
				"hour": 0,
				"minute": 0
			},
			"end": {
				"month": 0,
				"serial": 0,
				"day": 0,
				"hour": 0,
				"minute": 0
			},
			"status": true,
			"startTime": 0,
			"endTime": 0,
			"offset": 0,
			"nextStart": 0,
			"nextEnd": 0,
			"timeZone": "",
			"lastStart": 0,
			"lastEnd": 0
		},
		"scenario": "",
		"longitude": 0,
		"latitude": 0,
		"address": "",
		"supportES": true,
		"supportL2": true
	}
}
```
