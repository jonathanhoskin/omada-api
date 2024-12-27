## Get site list


**Url**:`/openapi/v1/{omadacId}/sites`


**Method**:`GET`


**produces**:`application/x-www-form-urlencoded`


**consumes**:`*/*`


**description**:<p>Get site list</p>



**Params**:


**Params**:


| name | description | in    | require | type | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|omadacId|Omada ID|path|true|string||
|page|Start page number. Start from 1.|query|true|integer(int32)||
|pageSize|Number of entries per page. It should be within the range of 1–1000.|query|true|integer(int32)||
|sorts.name|Sort parameter may be one of asc or desc. Optional parameter. If it is not carried, it means it is not sorted by this field. When there are more than one, the first one takes effect|query|false|string||
|searchKey|Fuzzy query parameters, support field name|query|false|string||
|filters.tag|Filter query parameters, support field tag ID|query|false|string||
|filters.type|Filter query parameters, support field site type. 0: basic site; 1: pro site.|query|false|string||


**status**:


| code | description | schema |
| -------- | -------- | ----- |
|200|OK|OperationResponseGridVOSiteSummaryInfo|


**Responses**:


| name | description | type | schema |
| -------- | -------- | ----- |----- |
|errorCode||integer(int32)|integer(int32)|
|msg||string||
|result||GridVOSiteSummaryInfo|GridVOSiteSummaryInfo|
|&emsp;&emsp;totalRows|Total rows of all items.|integer(int64)||
|&emsp;&emsp;currentPage|Current page number.|integer(int32)||
|&emsp;&emsp;currentSize|Number of entries per page.|integer(int32)||
|&emsp;&emsp;data|Site summary info|array|SiteSummaryInfo|
|&emsp;&emsp;&emsp;&emsp;siteId|Site ID|string||
|&emsp;&emsp;&emsp;&emsp;name|Name of the site should contain 1 to 64 characters.|string||
|&emsp;&emsp;&emsp;&emsp;tagIds|Site tag ID|array|string|
|&emsp;&emsp;&emsp;&emsp;region|Country/Region of the site; For the values of region, refer to the abbreviation of the ISO country code; For example, you need to input "United States" for the United States of America.|string||
|&emsp;&emsp;&emsp;&emsp;timeZone|For the values of the timezone of the site, refer to section 5.1 of the Open API Access Guide.|string||
|&emsp;&emsp;&emsp;&emsp;scenario|For the values of the scenario of the site, refer to result of the interface for Get scenario list.|string||
|&emsp;&emsp;&emsp;&emsp;longitude|Longitude of the site should be within the range of -180 - 180.|number||
|&emsp;&emsp;&emsp;&emsp;latitude|Latitude of the site should be within the range of -90 - 90.|number||
|&emsp;&emsp;&emsp;&emsp;address|Address of the site|string||
|&emsp;&emsp;&emsp;&emsp;type|Site type(only for pro controller). It should be a value as follows: 0: Basic Site; 1: Pro Site|integer||
|&emsp;&emsp;&emsp;&emsp;supportES|Whether the site supports adopting Easy Managed switches|boolean||
|&emsp;&emsp;&emsp;&emsp;supportL2|Whether the site supports adopting Smart+ or L2+ or L3 switches|boolean||


**Response Sample**:
```javascript
{
	"errorCode": 0,
	"msg": "",
	"result": {
		"totalRows": 0,
		"currentPage": 0,
		"currentSize": 0,
		"data": [
			{
				"siteId": "",
				"name": "",
				"tagIds": [],
				"region": "",
				"timeZone": "",
				"scenario": "",
				"longitude": 0,
				"latitude": 0,
				"address": "",
				"type": 0,
				"supportES": true,
				"supportL2": true
			}
		]
	}
}
```
