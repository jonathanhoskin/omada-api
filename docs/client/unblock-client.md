## Unblock the client


**Url**:`/openapi/v1/{omadacId}/sites/{siteId}/clients/{clientMac}/unblock`


**Method**:`POST`


**produces**:`application/x-www-form-urlencoded`


**consumes**:`*/*`


**description**:<p>Unblock the client.<br/><br/>The interface requires one of the permissions: <br/>Site Clients Manager Modify<br/>Site Insight Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the following error codes (non generic error codes): <br/>-41004  -  This client does not exist.</p>



**Params**:


**Params**:


| name | description | in    | require | type | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|omadacId|Omada ID|path|true|string||
|siteId|Site ID|path|true|string||
|clientMac|Client MAC|path|true|string||


**status**:


| code | description | schema |
| -------- | -------- | ----- |
|200|OK|OperationResponseWithoutResult|


**Responses**:


| name | description | type | schema |
| -------- | -------- | ----- |----- |
|errorCode||integer(int32)|integer(int32)|
|msg||string||


**Response Sample**:
```javascript
{
	"errorCode": 0,
	"msg": ""
}
```
