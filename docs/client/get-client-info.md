## Get client info


**Url**:`/openapi/v1/{omadacId}/sites/{siteId}/clients/{clientMac}`


**Method**:`GET`


**produces**:`application/x-www-form-urlencoded`


**consumes**:`*/*`


**description**:<p>Get client info.<br/><br/>The interface requires one of the permissions: <br/>Site Clients Manager View Only<br/>Site Device Manager View Only</p>



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
|200|OK|OperationResponseClient Detail|


**Responses**:


| name | description | type | schema |
| -------- | -------- | ----- |----- |
|errorCode||integer(int32)|integer(int32)|
|msg||string||
|result||Client Detail|Client Detail|
|&emsp;&emsp;id|Client ID|string||
|&emsp;&emsp;mac|Client MAC Address|string||
|&emsp;&emsp;name|Client Name, alias|string||
|&emsp;&emsp;hostName|Host name, device name|string||
|&emsp;&emsp;vendor|Vendor|string||
|&emsp;&emsp;deviceType|Device Type: iphone, ipod, android, pc, printer, tv...|string||
|&emsp;&emsp;deviceCategory|Device Category: loT, TV, computer, phone...|string||
|&emsp;&emsp;osName|Device system version|string||
|&emsp;&emsp;ip|IP Address|string||
|&emsp;&emsp;ipv6List|IPv6 Address|array|string|
|&emsp;&emsp;connectType|Connect type should be a value as follows: 0: wireless guest; 1: wireless user; 2: wired user|integer(int32)||
|&emsp;&emsp;connectDevType|connect device type should be a value as follows: ap, switch, gateway|string||
|&emsp;&emsp;connectedToWirelessRouter|true: Client is connecting to a wireless router.|boolean||
|&emsp;&emsp;wireless|true: Wireless device (connectDevType=ap);  false: Not wireless device(connectDevType=switch or gateway)|boolean||
|&emsp;&emsp;ssid|(Wireless)  SSID name|string||
|&emsp;&emsp;signalLevel|(Wireless) Signal strength percentage should be within the range of 0-100.|integer(int32)||
|&emsp;&emsp;signalRank|(Wireless) Signal strength level should be within the range of 0-5.|integer(int32)||
|&emsp;&emsp;wifiMode|(Wireless) Wifi mode should be a value as follows: 0: 11a; 1: 11b; 2: 11g; 3: 11na; 4: 11ng; 5: 11ac; 6: 11axa; 7: 11axg; 8: 11beg; 9: 11bea|integer(int32)||
|&emsp;&emsp;apName|(Wireless)  AP Name|string||
|&emsp;&emsp;apMac|(Wireless)  AP MAC Address|string||
|&emsp;&emsp;radioId|(Wireless) Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3: 6GHz|integer(int32)||
|&emsp;&emsp;channel|(Wireless)  Actual channel|integer(int32)||
|&emsp;&emsp;rxRate|(Wireless) Uplink negotiation rate (Kbit/s)|integer(int64)||
|&emsp;&emsp;txRate|(Wireless) Downlink negotiation rate (Kbit/s)|integer(int64)||
|&emsp;&emsp;powerSave|(Wireless)  true: Power save mode enabled|boolean||
|&emsp;&emsp;rssi|(Wireless) Signal strength, unit: dBm|integer(int32)||
|&emsp;&emsp;snr|(Wireless) Signal Noise Ratio|integer(int32)||
|&emsp;&emsp;switchMac|(Wired, connectDevType=switch)  Switch MAC address|string||
|&emsp;&emsp;switchName|(Wired, connectDevType=switch)  Switch name|string||
|&emsp;&emsp;gatewayMac|(Wired, connectDevType=gateway)  Gateway MAC Address|string||
|&emsp;&emsp;gatewayName|(Wired, connectDevType=gateway)  Gateway name|string||
|&emsp;&emsp;vid|(Wired) vlan|integer(int32)||
|&emsp;&emsp;networkName|(Wired) Network name|string||
|&emsp;&emsp;dot1xIdentity|(Wired) 802.1x authentication identity|string||
|&emsp;&emsp;dot1xVlan|(Wired) Network name corresponding to the VLAN obtained by 802.1x D-VLAN|integer(int32)||
|&emsp;&emsp;port|(Wired) Port ID|integer(int32)||
|&emsp;&emsp;lagId|(Wired) LAG ID. Exists only when the client is connected to the LAG|integer(int32)||
|&emsp;&emsp;activity|Real-time downlink rate (Byte/s)|integer(int64)||
|&emsp;&emsp;trafficDown|Downstream traffic (Byte)|integer(int64)||
|&emsp;&emsp;trafficUp|Upstream traffic (Byte)|integer(int64)||
|&emsp;&emsp;uptime|Up time (unit: s)|integer(int64)||
|&emsp;&emsp;lastSeen|Last found time, timestamp (ms)|integer(int64)||
|&emsp;&emsp;authStatus|Authentication status should be a value as follows: 0: CONNECTED // Access without any authentication method; 1: PENDING // Access to Portal, but authentication failed; 2: AUTHORIZED // Pass through portal, pass other authentication without portal; 3: AUTH-FREE // No portal authentication required.|integer(int32)||
|&emsp;&emsp;blocked|Whether the client is blocked|boolean||
|&emsp;&emsp;guest|(Wireless) Whether it is Guest (used to display the wireless Guest client icon)|boolean||
|&emsp;&emsp;active|Whether the client is online|boolean||
|&emsp;&emsp;manager|Whether it is the client currently being managed|boolean||
|&emsp;&emsp;ipSetting||Client Ip Setting|Client Ip Setting|
|&emsp;&emsp;&emsp;&emsp;useFixedAddr|Whether to use the specified IP|boolean||
|&emsp;&emsp;&emsp;&emsp;netId|LAN network ID|string||
|&emsp;&emsp;&emsp;&emsp;ip|Client IP|string||
|&emsp;&emsp;downPacket|Number of downstream packets|integer(int64)||
|&emsp;&emsp;upPacket|Number of upstream packets|integer(int64)||
|&emsp;&emsp;rateLimit||Client Rate Limit Setting|Client Rate Limit Setting|
|&emsp;&emsp;&emsp;&emsp;mode|Rate limit mode should be a value as follows: <br/>0: Custom mode. Apply the given rate limit value to the client; <br/>1: Rate limit profile mode. Find the corresponding rate limit file with rate limit ID and apply it to the client.|integer||
|&emsp;&emsp;&emsp;&emsp;rateLimitProfileId|Rate limit profile ID. Required when ratelimit mode is 1|string||
|&emsp;&emsp;&emsp;&emsp;customRateLimit|Custom configuration rate limit.|Custom rate limit entity|Custom rate limit entity|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;upEnable|Up limit enable|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;upUnit|Up limit unit should be a value as follows: 1: Kbps; 2: Mbps|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;upLimit|Up limit should be within the range of 1–1024.|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;downEnable|Down limit enable|boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;downUnit|Down limit unit should be a value as follows: 1: Kbps; 2: Mbps|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;downLimit|Down limit should be within the range of 1–1024.|integer||
|&emsp;&emsp;clientLockToApSetting|Client lock to ap setting|Client Lock To Ap Setting|Client Lock To Ap Setting|
|&emsp;&emsp;&emsp;&emsp;enable|Lock to AP enable|boolean||
|&emsp;&emsp;&emsp;&emsp;aps|AP name and MAC info list|array|ApBriefInfoVO|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|AP name|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mac|AP MAC, for example: AA-AA-AA-AA-AA-AA|string||
|&emsp;&emsp;multiLink|(Wireless) Client multifrequency info list|array|Client Multifrequency Info|
|&emsp;&emsp;&emsp;&emsp;radioId|Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3: 6GHz|integer||
|&emsp;&emsp;&emsp;&emsp;wifiMode|Wi-Fi mode should be a value as follows: 0: 11a; 1: 11b; 2: 11g; 3: 11na; 4: 11ng; 5: 11ac; 6: 11axa; 7: 11axg.|integer||
|&emsp;&emsp;&emsp;&emsp;channel|(Wireless)  Actual channel|integer||
|&emsp;&emsp;&emsp;&emsp;rxRate|(Wireless) Uplink negotiation rate (Kbit/s)|integer||
|&emsp;&emsp;&emsp;&emsp;txRate|(Wireless) Downlink negotiation rate (Kbit/s)|integer||
|&emsp;&emsp;&emsp;&emsp;powerSave|(Wireless)  true: Power save mode enabled|boolean||
|&emsp;&emsp;&emsp;&emsp;rssi|(Wireless) Signal strength, unit: dBm|integer||
|&emsp;&emsp;&emsp;&emsp;snr|(Wireless) Signal Noise Ratio|integer||
|&emsp;&emsp;&emsp;&emsp;signalLevel|(Wireless) Signal strength percentage should be within the range of 0-100.|integer||
|&emsp;&emsp;&emsp;&emsp;signalRank|(Wireless) Signal strength level should be within the range of 0-5.|integer||
|&emsp;&emsp;&emsp;&emsp;upPacket|Number of upstream packets|integer||
|&emsp;&emsp;&emsp;&emsp;downPacket|Number of downstream packets|integer||
|&emsp;&emsp;&emsp;&emsp;trafficDown|Downstream traffic (Byte)|integer||
|&emsp;&emsp;&emsp;&emsp;trafficUp|Upstream traffic (Byte)|integer||
|&emsp;&emsp;&emsp;&emsp;activity|Real-time downlink rate (Byte/s)|integer||
|&emsp;&emsp;&emsp;&emsp;signalLevelAndRank||integer||
|&emsp;&emsp;unit|Unit ID|integer(int32)||
|&emsp;&emsp;standardPort|Standard port|string||
|&emsp;&emsp;blockDisable|Block client disabled, default value: false|boolean||
|&emsp;&emsp;dhcpLeaseTime|DHCP lease time, unit seconds|integer(int64)||
|&emsp;&emsp;systemName|Device system name|string||
|&emsp;&emsp;description|Device description|string||
|&emsp;&emsp;capabilities|One or more of the following values: Station、DOCSIS cable device、Telephone、Router、WLAN access point、Bridge、Repeater、other.|array|string|


**Response Sample**:
```javascript
{
	"errorCode": 0,
	"msg": "",
	"result": {
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
}
```
