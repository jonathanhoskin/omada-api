## Get client list


**Url**:`/openapi/v1/{omadacId}/sites/{siteId}/clients`


**Method**:`GET`


**produces**:`application/x-www-form-urlencoded`


**consumes**:`*/*`


**description**:<p>Get all clients.<br/><br/>The interface requires one of the permissions: <br/>Site Clients Manager View Only<br/>Site Device Manager View Only</p>



**Params**:


**Params**:


| name | description | in    | require | type | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|omadacId|Omada ID|path|true|string||
|siteId|Site ID|path|true|string||
|page|Start page number. Start from 1.|query|true|integer(int32)||
|pageSize|Number of entries per page. It should be within the range of 1–1000.|query|true|integer(int32)||
|sorts.name|Sort parameter may be one of asc or desc. Optional parameter. If it is not carried, it means it is not sorted by this field. When there are more than one, the first one takes effect|query|false|string||
|sorts.mac|Sort parameter may be one of asc or desc. Optional parameter. If it is not carried, it means it is not sorted by this field. When there are more than one, the first one takes effect|query|false|string||
|sorts.ip|Sort parameter may be one of asc or desc. Optional parameter. If it is not carried, it means it is not sorted by this field. When there are more than one, the first one takes effect|query|false|string||
|filters.wireless|Filter query parameters, support field wireless: true/false.|query|false|string||
|filters.radioId|Filter query parameters, support field radioId: 0: 2G, 1: 5G1, 2: 5G2, 3: 6G|query|false|string||
|filters.apMac|Filter query parameters, support field ap mac|query|false|string||
|filters.switchMac|Filter query parameters, support field switch mac|query|false|string||
|filters.gatewayMac|Filter query parameters, support field gateway mac|query|false|string||
|searchKey|Fuzzy query parameters, support field clientName,clientMac,ip,channel,ssid,apName,apMac,switchMac,switchName,gatewayMac,gatewayName.|query|false|string||


**status**:


| code | description | schema |
| -------- | -------- | ----- |
|200|OK|OperationResponseClientGridVOClient Info|


**Responses**:


| name | description | type | schema |
| -------- | -------- | ----- |----- |
|errorCode||integer(int32)|integer(int32)|
|msg||string||
|result||ClientGridVOClient Info|ClientGridVOClient Info|
|&emsp;&emsp;totalRows|Total rows of all items.|integer(int64)||
|&emsp;&emsp;currentPage|Current page number.|integer(int32)||
|&emsp;&emsp;currentSize|Number of entries per page.|integer(int32)||
|&emsp;&emsp;data||array|Client Info|
|&emsp;&emsp;&emsp;&emsp;id|Client ID|string||
|&emsp;&emsp;&emsp;&emsp;mac|Client MAC Address|string||
|&emsp;&emsp;&emsp;&emsp;name|Client Name, alias|string||
|&emsp;&emsp;&emsp;&emsp;hostName|Host name, device name|string||
|&emsp;&emsp;&emsp;&emsp;vendor|Vendor|string||
|&emsp;&emsp;&emsp;&emsp;deviceType|Device Type: iphone, ipod, android, pc, printer, tv...|string||
|&emsp;&emsp;&emsp;&emsp;deviceCategory|Device Category: loT, TV, computer, phone...|string||
|&emsp;&emsp;&emsp;&emsp;osName|Device system version|string||
|&emsp;&emsp;&emsp;&emsp;ip|IP Address|string||
|&emsp;&emsp;&emsp;&emsp;ipv6List|IPv6 Address|array|string|
|&emsp;&emsp;&emsp;&emsp;connectType|Connect type should be a value as follows: 0: wireless guest; 1: wireless user; 2: wired user|integer||
|&emsp;&emsp;&emsp;&emsp;connectDevType|connect device type should be a value as follows: ap, switch, gateway|string||
|&emsp;&emsp;&emsp;&emsp;connectedToWirelessRouter|true: Client is connecting to a wireless router.|boolean||
|&emsp;&emsp;&emsp;&emsp;wireless|true: Wireless device (connectDevType=ap);  false: Not wireless device(connectDevType=switch or gateway)|boolean||
|&emsp;&emsp;&emsp;&emsp;ssid|(Wireless)  SSID name|string||
|&emsp;&emsp;&emsp;&emsp;signalLevel|(Wireless) Signal strength percentage should be within the range of 0-100.|integer||
|&emsp;&emsp;&emsp;&emsp;healthScore|1~3: poor; 4~7: fair; 0: no data; 8~10 good.|integer||
|&emsp;&emsp;&emsp;&emsp;signalRank|(Wireless) Signal strength level should be within the range of 0-5.|integer||
|&emsp;&emsp;&emsp;&emsp;wifiMode|(Wireless) Wifi mode should be a value as follows: 0: 11a; 1: 11b; 2: 11g; 3: 11na; 4: 11ng; 5: 11ac; 6: 11axa; 7: 11axg; 8: 11beg; 9: 11bea|integer||
|&emsp;&emsp;&emsp;&emsp;apName|(Wireless)  AP Name|string||
|&emsp;&emsp;&emsp;&emsp;apMac|(Wireless)  AP MAC Address|string||
|&emsp;&emsp;&emsp;&emsp;radioId|(Wireless) Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3: 6GHz|integer||
|&emsp;&emsp;&emsp;&emsp;channel|(Wireless)  Actual channel|integer||
|&emsp;&emsp;&emsp;&emsp;rxRate|(Wireless) Uplink negotiation rate (Kbit/s)|integer||
|&emsp;&emsp;&emsp;&emsp;txRate|(Wireless) Downlink negotiation rate (Kbit/s)|integer||
|&emsp;&emsp;&emsp;&emsp;powerSave|(Wireless)  true: Power save mode enabled|boolean||
|&emsp;&emsp;&emsp;&emsp;rssi|(Wireless) Signal strength, unit: dBm|integer||
|&emsp;&emsp;&emsp;&emsp;snr|(Wireless) Signal Noise Ratio|integer||
|&emsp;&emsp;&emsp;&emsp;switchMac|(Wired, connectDevType=switch)  Switch MAC address|string||
|&emsp;&emsp;&emsp;&emsp;switchName|(Wired, connectDevType=switch)  Switch name|string||
|&emsp;&emsp;&emsp;&emsp;gatewayMac|(Wired, connectDevType=gateway)  Gateway MAC Address|string||
|&emsp;&emsp;&emsp;&emsp;gatewayName|(Wired, connectDevType=gateway)  Gateway name|string||
|&emsp;&emsp;&emsp;&emsp;vid|(Wired) vlan|integer||
|&emsp;&emsp;&emsp;&emsp;networkName|(Wired) Network name|string||
|&emsp;&emsp;&emsp;&emsp;dot1xIdentity|(Wired) 802.1x authentication identity|string||
|&emsp;&emsp;&emsp;&emsp;dot1xVlan|(Wired) Network name corresponding to the VLAN obtained by 802.1x D-VLAN|integer||
|&emsp;&emsp;&emsp;&emsp;port|(Wired) Port ID|integer||
|&emsp;&emsp;&emsp;&emsp;lagId|(Wired) LAG ID. Exists only when the client is connected to the LAG|integer||
|&emsp;&emsp;&emsp;&emsp;activity|Real-time downlink rate (Byte/s)|integer||
|&emsp;&emsp;&emsp;&emsp;trafficDown|Downstream traffic (Byte)|integer||
|&emsp;&emsp;&emsp;&emsp;trafficUp|Upstream traffic (Byte)|integer||
|&emsp;&emsp;&emsp;&emsp;uptime|Up time (unit: s)|integer||
|&emsp;&emsp;&emsp;&emsp;lastSeen|Last found time, timestamp (ms)|integer||
|&emsp;&emsp;&emsp;&emsp;authStatus|Authentication status should be a value as follows: 0: CONNECTED // Access without any authentication method; 1: PENDING // Access to Portal, but authentication failed; 2: AUTHORIZED // Pass through portal, pass other authentication without portal; 3: AUTH-FREE // No portal authentication required.|integer||
|&emsp;&emsp;&emsp;&emsp;blocked|Whether the client is blocked|boolean||
|&emsp;&emsp;&emsp;&emsp;guest|(Wireless) Whether it is Guest (used to display the wireless Guest client icon)|boolean||
|&emsp;&emsp;&emsp;&emsp;active|Whether the client is online|boolean||
|&emsp;&emsp;&emsp;&emsp;manager|Whether it is the client currently being managed|boolean||
|&emsp;&emsp;&emsp;&emsp;ipSetting||Client Ip Setting|Client Ip Setting|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;useFixedAddr|Whether to use the specified IP|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;netId|LAN network ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ip|Client IP|string||
|&emsp;&emsp;&emsp;&emsp;downPacket|Number of downstream packets|integer||
|&emsp;&emsp;&emsp;&emsp;upPacket|Number of upstream packets|integer||
|&emsp;&emsp;&emsp;&emsp;rateLimit||Client Rate Limit Setting|Client Rate Limit Setting|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mode|Rate limit mode should be a value as follows: <br/>0: Custom mode. Apply the given rate limit value to the client; <br/>1: Rate limit profile mode. Find the corresponding rate limit file with rate limit ID and apply it to the client.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rateLimitProfileId|Rate limit profile ID. Required when ratelimit mode is 1|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;customRateLimit|Custom configuration rate limit.|Custom rate limit entity|Custom rate limit entity|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;upEnable|Up limit enable|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;upUnit|Up limit unit should be a value as follows: 1: Kbps; 2: Mbps|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;upLimit|Up limit should be within the range of 1–1024.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;downEnable|Down limit enable|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;downUnit|Down limit unit should be a value as follows: 1: Kbps; 2: Mbps|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;downLimit|Down limit should be within the range of 1–1024.|integer||
|&emsp;&emsp;&emsp;&emsp;clientLockToApSetting|Client lock to ap setting|Client Lock To Ap Setting|Client Lock To Ap Setting|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;enable|Lock to AP enable|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;aps|AP name and MAC info list|array|ApBriefInfoVO|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|AP name|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mac|AP MAC, for example: AA-AA-AA-AA-AA-AA|string||
|&emsp;&emsp;&emsp;&emsp;multiLink|(Wireless) Client multifrequency info list|array|Client Multifrequency Info|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;radioId|Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3: 6GHz|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;wifiMode|Wi-Fi mode should be a value as follows: 0: 11a; 1: 11b; 2: 11g; 3: 11na; 4: 11ng; 5: 11ac; 6: 11axa; 7: 11axg.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;channel|(Wireless)  Actual channel|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rxRate|(Wireless) Uplink negotiation rate (Kbit/s)|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;txRate|(Wireless) Downlink negotiation rate (Kbit/s)|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;powerSave|(Wireless)  true: Power save mode enabled|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rssi|(Wireless) Signal strength, unit: dBm|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;snr|(Wireless) Signal Noise Ratio|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;signalLevel|(Wireless) Signal strength percentage should be within the range of 0-100.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;signalRank|(Wireless) Signal strength level should be within the range of 0-5.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;upPacket|Number of upstream packets|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;downPacket|Number of downstream packets|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;trafficDown|Downstream traffic (Byte)|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;trafficUp|Upstream traffic (Byte)|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;activity|Real-time downlink rate (Byte/s)|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;signalLevelAndRank||integer||
|&emsp;&emsp;&emsp;&emsp;unit|Unit ID|integer||
|&emsp;&emsp;&emsp;&emsp;standardPort|Standard port|string||
|&emsp;&emsp;&emsp;&emsp;blockDisable|Block client disabled, default value: false|boolean||
|&emsp;&emsp;&emsp;&emsp;dhcpLeaseTime|DHCP lease time, unit seconds|integer||
|&emsp;&emsp;&emsp;&emsp;systemName|Device system name|string||
|&emsp;&emsp;&emsp;&emsp;description|Device description|string||
|&emsp;&emsp;&emsp;&emsp;capabilities|One or more of the following values: Station、DOCSIS cable device、Telephone、Router、WLAN access point、Bridge、Repeater、other.|array|string|
|&emsp;&emsp;clientStat||ClientStatVO|ClientStatVO|
|&emsp;&emsp;&emsp;&emsp;total||integer||
|&emsp;&emsp;&emsp;&emsp;wireless||integer||
|&emsp;&emsp;&emsp;&emsp;wired||integer||
|&emsp;&emsp;&emsp;&emsp;num2g||integer||
|&emsp;&emsp;&emsp;&emsp;num5g||integer||
|&emsp;&emsp;&emsp;&emsp;num6g||integer||
|&emsp;&emsp;&emsp;&emsp;numUser||integer||
|&emsp;&emsp;&emsp;&emsp;numGuest||integer||
|&emsp;&emsp;&emsp;&emsp;numWirelessUser||integer||
|&emsp;&emsp;&emsp;&emsp;numWirelessGuest||integer||
|&emsp;&emsp;&emsp;&emsp;num2gUser||integer||
|&emsp;&emsp;&emsp;&emsp;num5gUser||integer||
|&emsp;&emsp;&emsp;&emsp;num6gUser||integer||
|&emsp;&emsp;&emsp;&emsp;num2gGuest||integer||
|&emsp;&emsp;&emsp;&emsp;num5gGuest||integer||
|&emsp;&emsp;&emsp;&emsp;num6gGuest||integer||
|&emsp;&emsp;&emsp;&emsp;poor||integer||
|&emsp;&emsp;&emsp;&emsp;fair||integer||
|&emsp;&emsp;&emsp;&emsp;noData||integer||
|&emsp;&emsp;&emsp;&emsp;good||integer||


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
				"id": "",
				"mac": "",
				"name": "",
				"hostName": "",
				"vendor": "",
				"deviceType": "",
				"deviceCategory": "",
				"osName": "",
				"ip": "",
				"ipv6List": [],
				"connectType": 0,
				"connectDevType": "",
				"connectedToWirelessRouter": true,
				"wireless": true,
				"ssid": "",
				"signalLevel": 0,
				"healthScore": 0,
				"signalRank": 0,
				"wifiMode": 0,
				"apName": "",
				"apMac": "",
				"radioId": 0,
				"channel": 0,
				"rxRate": 0,
				"txRate": 0,
				"powerSave": true,
				"rssi": 0,
				"snr": 0,
				"switchMac": "",
				"switchName": "",
				"gatewayMac": "",
				"gatewayName": "",
				"vid": 0,
				"networkName": "",
				"dot1xIdentity": "",
				"dot1xVlan": 0,
				"port": 0,
				"lagId": 0,
				"activity": 0,
				"trafficDown": 0,
				"trafficUp": 0,
				"uptime": 0,
				"lastSeen": 0,
				"authStatus": 0,
				"blocked": true,
				"guest": true,
				"active": true,
				"manager": true,
				"ipSetting": {
					"useFixedAddr": true,
					"netId": "",
					"ip": ""
				},
				"downPacket": 0,
				"upPacket": 0,
				"rateLimit": {
					"mode": 0,
					"rateLimitProfileId": "",
					"customRateLimit": {
						"upEnable": true,
						"upUnit": 0,
						"upLimit": 0,
						"downEnable": true,
						"downUnit": 0,
						"downLimit": 0
					}
				},
				"clientLockToApSetting": {
					"enable": true,
					"aps": [
						{
							"name": "",
							"mac": ""
						}
					]
				},
				"multiLink": [
					{
						"radioId": 0,
						"wifiMode": 0,
						"channel": 0,
						"rxRate": 0,
						"txRate": 0,
						"powerSave": true,
						"rssi": 0,
						"snr": 0,
						"signalLevel": 0,
						"signalRank": 0,
						"upPacket": 0,
						"downPacket": 0,
						"trafficDown": 0,
						"trafficUp": 0,
						"activity": 0,
						"signalLevelAndRank": 0
					}
				],
				"unit": 0,
				"standardPort": "",
				"blockDisable": true,
				"dhcpLeaseTime": 0,
				"systemName": "",
				"description": "",
				"capabilities": []
			}
		],
		"clientStat": {
			"total": 0,
			"wireless": 0,
			"wired": 0,
			"num2g": 0,
			"num5g": 0,
			"num6g": 0,
			"numUser": 0,
			"numGuest": 0,
			"numWirelessUser": 0,
			"numWirelessGuest": 0,
			"num2gUser": 0,
			"num5gUser": 0,
			"num6gUser": 0,
			"num2gGuest": 0,
			"num5gGuest": 0,
			"num6gGuest": 0,
			"poor": 0,
			"fair": 0,
			"noData": 0,
			"good": 0
		}
	}
}
```
