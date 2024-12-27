# Open API Access Guide

# 1 Overview

## 1.1 Status Code
| Status Code	| Explain |
| :-: | - |
| 400	| Bad Request |
| 401	| Unauthorized access |
| 403	| Forbidden |
| 413	| Request-size limit exceeded |
| 417	| Request-size limit exceeded |
| 429	| API Rate limit exceeded |
| 500	| Internal server error |

## 1.2 General Error Code In Result
| Error Code	| Explain |
| :-: | - |
| -1005	| Operation forbidden |
| -44106	| The client id or client secret is invalid |
| -44107	| The response type is invalid |
| -44108	| The CSRF token is invalid |
| -44109	| The session id is invalid |
| -44110	| The auth code has expired |
| -44111	| The grant type is invalid |
| -44112	| The access token has expired. Please re-initiate the refreshToken process to obtain the access token. |
| -44113	| The access token is Invalid |
| -44114	| The refresh token has expired. Please re-initiate the authentication process to obtain the refresh token. |
| -44116	| Open API authorized failed, please check whether the input parameters are legal. |
| -44118	| This interface only supports the authorization code mode, not the client credentials mode. |

## 1.3 Process Introduction
Omada's Open API supports the REST API of most Controller services. This feature allows Omada users to write custom applications, embed APIs, or combine their own applications. The REST API supports HTTP GET and POST operations by providing specific URLs for each query. The output of these operations is returned in JSON format. To access the API securely, the Omada API framework supports the OAuth 2.0 protocol for authentication and authorization, which allows you to access resources authorized by users without obtaining user names and passwords, and supports the authorization code mode and client credentials mode.

The authorization code grant type is used to obtain both access tokens and refresh tokens and is optimized for confidential clients. Since this is a redirection-based flow, the client must be capable of interacting with the resource owner's user-agent (typically a web browser) and capable of receiving incoming requests (via redirection) from the authorization server.

The following is the authorization code mode process：
1. The user visits the client.
2. The client directs the user to the authentication server (Omada).
3. User logs in (`/openapi/login`), and authorize the third-party client.
4. The authentication server directs the user to the redirection URL specified by the client in advance, and attaches an authorization code (`redirect URL + ?code={authorization code}`, if the redirect URL is `https://redirect.com`, it is `https://redirect.com?code=authCode`).
5. The client uses the authorization code to exchange the accessToken from the authentication server (Omada).
6. The authentication server (Omada) authenticates the client and issues an access token.
7. The client uses the access token to apply for resources from the resource server (Omada).
8. The resource server (Omada) confirms the access token and opens resources to the client.
9. The client can exchange an access token through refresh token, client ID, and client secret.

The client can request an access token using only its client credentials (or other supported means of authentication) when the client is requesting access to the protected resources under its control, or those of another resource owner that have been previously arranged with the authorization server (the method of which is beyond the scope of this specification).

The following is the client credentials mode process：
1. The user opens the client, and the client requires the user to authorize.
2. The user agrees to authorize the client.
3. The client uses the authorization obtained to apply for an access token from the authentication server (Omada).
4. The authentication server (Omada) authenticates the client and issues an access token.
5. The client uses the access token to apply for resources from the resource server (Omada).
6. The resource server (Omada) confirms the access token and open resources to the client.
7. The client can exchange an access token through refresh token, client ID, and client secret.

# 2 Access Process
## 2.1 Create Application
1. To access the Open API, first create an application at Settings > Platform Integration in the MSP or Global view. You can customize the content：
    - **Authorization code mode**: You can define the Application name and Redirect URL. When calling the interface in this mode, the authority is the same as that of the login user.
    - **Client mode**: You can define the Application name and access permissions. When calling the interface in this mode, the rights are the same as the login Application.
2. After the creation is successful, each Application will have a corresponding client ID and client secret, which will be used for subsequent access to the Open API. You can view the details on the interface to know the Omada ID and the access address of the Open API.

## 2.2 Authorization Code Mode Access Process
### 2.2.1 Login Authentication & Obtain Authorization Code
#### 2.2.1.1 Redirect URL not specified
When the redirect URL is not specified, the operation process is as follows.

First of all, you need to log in. When using the Open API function later, its authority is the same as that of the current login user. The login interface uses the POST method, the interface path is `/openapi/authorize/login`.

In the Query, fill in the client ID (The field name is client_id) and msp id or customer id (The field name is omadac_id).
In the Body, fill in the user name (The field name is username) and password (The field name is password).
After logging in successfully, it will return the `csrfToken`, `sessionId`.
Note: Please save the return parameters for later use.

An example of the curl command of the login interface is as follows:

Request:
```bash
curl "https://localhost:8043/openapi/authorize/login?client_id=38f2d1b616434374b3f3215246f39940&omadac_id=beed48c7a2b0ea97c9698408843119f3" -H 'content-type:application/json' -d '{"username":"admin","password":"tplink123"}' -X POST -i -k --insecure
```

Response:
```json
{"errorCode":0,"msg":"Open API Log in successfully.","result":{"csrfToken":"51cb83c7d00a4e85b3dd2d6174a614d9","sessionId":"2fc0ca155ab94957a9a9e6a3b00662ea"}}
```

After logging in, you need to obtain the authorization code. The obtaining the authorization interface uses the POST method, the interface path is as follows: `/openapi/authorize/code`.

In the Query, fill in the client ID (The field name is `client_id`) and response type (The field name is `response_type`), msp id or customer id (The field name is `omadac_id`). The `response_type` represents the reply type, and is filled with "code" by default in authorization code mode.
In the Headers, fill in the csrf token (The field name is `Csrf-Token`) and cookie (The field name is `Cookie`) obtained in the login step.

Note that the prefix `TPOMADA_SESSIONID=` is required when filling in the cookie. After obtaining authorization code successfully, it will return the authorization code.

Note: The authorization code is only available for 2 minutes. If it expires, you need to obtain it again.

An example of the curl command of the obtaining authorization code interface is as follows:
Request:
```bash
curl "https://localhost:8043/openapi/authorize/code?client_id=29f2fdbeb5a84d50b9b1cdd08cd1a3ff&omadac_id=de382a0e78f4deb681f3128c3e75dbd1&response_type=code" -H 'content-type:application/json' -H 'Csrf-Token:ae6b935c92cf4b1b9f3eb852e20ed2b8' -H 'Cookie:TPOMADA_SESSIONID=9cb86bf3a99e48a59e4f3bb464a3c443' -X POST -i -k --insecure
```

Response:
```json
{"errorCode":0,"msg":"Open API Authorize successfully.","result":"OC-9iyxaKVOVMBpYhQ4NryaYBjghj3dTY32"}
```

#### 2.2.1.2 redirect URL already specified
When the redirect URL is specified, the operation process is as follows.

Omada customized the login page for the third party. Note that client ID is required to carry. When logging in directly through the login page, the user will be redirected to the third-party service with the authorization code. For example, if the redirect URL is http://test.com:8082/redirect/test, Omada will send a redirect request http://test.com:8082/redirect/test?code={authorization code}, and the client can directly parse the authorization code for subsequent processing. If you don't know your login URL, go to Settings > Platform Integration > Open API, find your application and click the View button to check the Oauth Login Page Address.

In the Query, fill in the client ID (The field name is `client_id`)
Note: If you need to redirect the authorization code, please contact our technical support to add your domain name to the trusted list of the Omada system.

### 2.2.2 Obtain Access Token
After the authorization code is obtained, it will be used to obtain the access token. The obtaining the access token interface uses the POST method, the interface path is as follows: `/openapi/authorize/token`.

In the Query, fill in the grant type (The field name is `grant_type`). The grant type indicates the authentication method, and the authorization code needs to be filled in with "authorization_code"
In the Body, fill in the client ID (the field name is `client_id`) and client secret (the field name is `client_secret`).
After obtaining access token successfully, it will return the access token (The field name is `accessToken`), token type (The field name is `tokenType`), expire time (The field name is `expiresIn`, unit is second), refresh token (The field name is `refreshToken`).

An example of the curl command of the obtaining access token interface is as follows:
Request:
```bash
curl "https://localhost:8043/openapi/authorize/token?grant_type=authorization_code&code=OC-y8fyWAyICCqCWw44Oi9GeSr7fQIKHg7g" -H 'content-type:application/json' -d '{"client_id": "29f2fdbeb5a84d50b9b1cdd08cd1a3ff", "client_secret": "cf6b13af0dd045628c9f05f088eb5493"}' -X POST -i -k --insecure
```

Response:
```json
{"errorCode":0,"msg":"Open API Get Access Token successfully.","result":{"accessToken":"AT-bllLYOOYASck11SBSDmmHs85lCrkN6Gi","tokenType":"bearer","expiresIn":7200,"refreshToken":"RT-HqvaDuSxEqayM75U2ukTRnBl6f6fiRAc"}}
```

### 2.2.3 Access API Interface
After obtaining access token, it will be used to access API interfaces.

In the Header, fill in the access token. Note prefix of the access token in the Authorization header is "AccessToken=" .
Other parameters can be filled in according to the description in the online document

An example of the curl command of the get site list interface is as follows:
Request:
```bash
curl "https://localhost:8043/openapi/v1/de382a0e78f4deb681f3128c3e75dbd1/sites?pageSize=1&page=1" -H 'content-type:application/json' -H 'Authorization:AccessToken=AT-RCio7FS9p46wSD7dM8CwNQA7ylcrmAcV' -X GET -i -k --insecure
```

Response:
```json
{"errorCode":0,"msg":"Success.","result":{"totalRows":1,"currentPage":1,"currentSize":1,"data":[{"siteId":"640effd1b3f2ae5b912275ec","name":"323233232","region":"China mainland","timeZone":"UTC","scenario":"Hotel","type":0}]}}
```

### 2.2.4 Refresh Access Token
Currently, the access token is valid for 2 hours, and the refresh token is valid for 14 days. If the access token expires, you can use the refresh token interface to obtain a new access token. The refresh access token interface uses the POST method, the interface path is as follows: /openapi/authorize/token. If the refresh token also expires, you will need to go through the previous authentication process again.

In the Query, fill in the grant type(The field name is grant_type), refresh token(The field name is refresh_token). The grant type indicate the authentication method, and the refresh token needs to be filled in with "refresh_token"
In the Body, fill in the client ID(the field name is client_id) and client secret(the field name is client_secret).
An example of the curl command of the refresh token interface is as follows:

Request:
```bash
curl "https://localhost:8043/openapi/authorize/token?client_id=185586e0df424f5ea938de13cba91e01&client_secret=767372a5258a4fc1a03c57f3d071fc35&refresh_token=RT-AhzwqCenDCZ84qpBHnZhYs3j2RGw9q8E&grant_type=refresh_token" -H 'content-type:application/json' -X POST -i -k --insecure
```

Response:
```json
{"errorCode":0,"msg":"Open API Get Access Token successfully.","result":{"accessToken":"AT-w9veJNQlaK8dH08qEQZCTas6y70IRAii","tokenType":"bearer","expiresIn":7001,"refreshToken":"RT-AhzwqCenDCZ84qpBHnZhYs3j2RGw9q8E"}}
```

## 2.3 Client Credentials Mode Access Process
### 2.3.1 Obtain Access Token
The client credentials mode can directly obtain the access token without the need to obtain the authorization code.

In the Query, fill in the grant type(the field name is grant_type). The grant type indicate the authentication method, and the client credentials code needs to be filled in with "client_credentials"
In the Body, fill in the msp id or customer id(The field name is omadacId), client ID(the field name is client_id) and client secret(the field name is client_secret).
An example of the curl command of the obtaining access token interface is as follows:

Request:
```bash
curl "https://localhost:8043/openapi/authorize/token?grant_type=client_credentials" -H 'content-type:application/json' -d '{"omadacId": "de382a0e78f4deb681f3128c3e75dbd1", "client_id": "185586e0df424f5ea938de13cba91e01", "client_secret": "767372a5258a4fc1a03c57f3d071fc35"}' -X POST -i -k --insecure
```

Response:
```json
{"errorCode":0,"msg":"Open API Get Access Token successfully.","result":{"accessToken":"AT-bjaJkIMIiekZY6NBufoQO4hdmJTswlwU","tokenType":"bearer","expiresIn":7200,"refreshToken":"RT-3ZjJgcORJSh76UCh7pj0rs5VRISIpagV"}}
```

Note: After obtaining the token, if you copy or import sites, or change application permission-related parameters (such as role/site/customer privilege) in the controller, the original token will become invalid and you need to authorize it again.

### 2.3.2 Access API Interface
This step is the same as the authorization code mode.

### 2.3.3 Refresh Access Token
This step is the same as the authorization code mode.

## 2.4 Batch Processing OpenAPIs
You can process up to 20 other OpenAPIs through the OpenAPI Batch Processing OpenAPIs, excluding MSP OpenAPIs. All processing should use the same `omadacId`.

In MSP mode, You can process up to 20 other OpenAPIs through the OpenAPI Batch Processing MSP OpenAPIs. For dealing with MSP OpenAPIs, the same `mspId` should be used. For dealing with other non MSP OpenAPIs, the corresponding `customerId` should be used.

## 3 Domain Name (Dedicated to CBC)

### 3.1 Front-end Login Domain Name
Singapore：aps1-omada-controller.tplinkcloud.com
Europe：euw1-omada-controller.tplinkcloud.com
US：use1-omada-controller.tplinkcloud.com

Note: If you don't know your service area, find the domain name as follows: go to Settings > Platform Integration > Open API, find your application and click the View button to check the Oauth Login Page Address.

### 3.2 Rest API Domain Name
Singapore：aps1-northbound-omada-controller.tplinkcloud.com
Europe：euw1-northbound-omada-controller.tplinkcloud.com
US：use1-northbound-omada-controller.tplinkcloud.com

Note: If you don't know your service area, find the domain name as follows: go to Settings > Platform Integration > Open API, find your application and click the View button to check the Interface Access Address.

## 4 Domain Name (Dedicated to local)

### 4.1 Front-end Login Domain Name
Find the domain name as follows: go to Settings > Platform Integration > Open API, find your application and click the View button to check the Oauth Login Page Address.

### 4.2 Rest API Domain Name
Find the domain name as follows: go to Settings > Platform Integration > Open API, find your application and click the View button to check the Interface Access Address.

# 5 Appendix

## 5.1 Time Zone
Some interfaces may require Time Zone. The table below lists the Time Zone values of the controller.

| Time Zone |
| Pacific/Wake |
| Pacific/Midway |
| Pacific/Honolulu |
| America/Anchorage |
| America/Los_Angeles |
| America/Phoenix |
| America/Chihuahua |
| America/Denver |
| America/Tegucigalpa |
| America/Chicago |
| America/Mexico_City |
| Canada/Saskatchewan |
| America/Bogota |
| America/New_York |
| America/Indiana/Indianapolis |
| America/Caracas |
| America/Asuncion |
| America/Halifax |
| America/Cuiaba |
| America/La_Paz |
| Canada/Newfoundland |
| America/Sao_Paulo |
| America/Buenos_Aires |
| America/Cayenne |
| America/Godthab |
| America/Montevideo |
| America/Santiago |
| Atlantic/South_Georgia |
| Atlantic/Azores |
| Atlantic/Cape_Verde |
| Africa/Casablanca |
| UTC |
| Europe/London |
| Atlantic/Reykjavik |
| Europe/Amsterdam |
| Europe/Belgrade |
| Europe/Brussels |
| Europe/Sarajevo |
| Africa/Algiers |
| Europe/Athens |
| Asia/Beirut |
| Africa/Cairo |
| Asia/Damascus |
| Africa/Harare |
| Europe/Vilnius |
| Asia/Jerusalem |
| Asia/Amman |
| Asia/Baghdad |
| Europe/Minsk |
| Asia/Kuwait |
| Africa/Nairobi |
| Asia/Istanbul |
| Asia/Tehran |
| Asia/Muscat |
| Asia/Baku |
| Europe/Moscow |
| Asia/Tbilisi |
| Asia/Yerevan |
| Asia/Kabul |
| Asia/Karachi |
| Asia/Yekaterinburg |
| Asia/Tashkent |
| Asia/Kolkata |
| Asia/Colombo |
| Asia/Katmandu |
| Asia/Dhaka |
| Asia/Rangoon |
| Asia/Bangkok |
| Asia/Novosibirsk |
| Asia/Hong_Kong |
| Asia/Krasnoyarsk |
| Asia/Kuala_Lumpur |
| Australia/Perth |
| Asia/Taipei |
| Asia/Ulaanbaatar |
| Asia/Irkutsk |
| Asia/Tokyo |
| Asia/Seoul |
| Australia/Adelaide |
| Australia/Darwin |
| Australia/Brisbane |
| Australia/Canberra |
| Pacific/Guam |
| Australia/Hobart |
| Asia/Yakutsk |
| Pacific/Noumea |
| Asia/Vladivostok |
| Pacific/Auckland |
| Pacific/Fiji |
| Asia/Magadan |
| Asia/Kamchatka |
| Pacific/Tongatapu |

## 5.2 Audit Log

### 5.2.1 Audit Log Notification
Some interfaces may require Audit Log Notification Category Key. The tables below lists the Audit Log Notification Category Key of the controller.

#### Msp Level

| Audit Log Notification Category Key |
| ACCOUNT |
| BACKUP |
| CLOUD_ACCESS |
| DASHBOARD |
| DATA_EXPORT |
| DEVICE_MANAGEMENT |
| LICENSE |
| LOG |
| MSP_SETTINGS |
| RESTORE |
| SITE_MANAGEMENT |
| SYSTEM_SETTINGS |
| USER_INTERFACE |
| WEBHOOK_SETTINGS |

#### Global/Customer Level

| Audit Log Notification Category Key |
| ACCOUNT |
| BACKUP |
| CLOUD_ACCESS |
| CONTROLLER_SETTINGS |
| DATA_EXPORT |
| IPS |
| LICENSE |
| LOG |
| MIGRATION |
| RESTORE |
| SITE_MANAGEMENT |
| SYSTEM_SETTINGS |
| USER_ACTIVITY |
| USER_INTERFACE |
| WEBHOOK_SETTINGS |

#### Site Level

| Audit Log Notification Category Key |
| ABNORMAL |
| APPLICATION_CONTROL |
| AUTHENTICATION |
| CLI |
| CLIENTS |
| DASHBOARD |
| DEVICE_MANAGEMENT |
| HOTSPOT_MANAGER |
| INSIGHT |
| IPS |
| LOG |
| MAP |
| NETWORK_SECURITY |
| PROFILES |
| REPORT |
| SIM |
| SITE_SERVICES |
| SITE_SETTINGS |
| TOOLS |
| TRANSMISSION |
| VPN |
| WIRED_NETWORKS |
| WIRELESS_NETWORKS |

### 5.2.2 Audit Log Type
Some interfaces may require Audit Log Type. The tables below lists the Audit Log Type of the controller.

#### Msp Level

| Audit Log Type |
| Account |
| Backup |
| Cloud Access |
| Dashboard |
| Data Export |
| Device Management |
| License |
| Log |
| MSP Settings |
| Restore |
| Site Management |
| System Settings |
| User Interface |
| Webhook Settings |

#### Global/Customer Level

| Audit Log Type |
| Account |
| Backup |
| Cloud Access |
| Controller Settings |
| Data Export |
| IPS |
| License |
| Log |
| Migration |
| Restore |
| Site Management |
| System Settings |
| User Activity |
| User Interface |
| Webhook Settings |

#### Site Level

| Audit Log Type |
| Abnormal |
| Application Control |
| Authentication |
| CLI |
| Clients |
| Dashboard |
| Device Management |
| Hotspot Manager |
| IPS |
| Insight |
| Log |
| Map |
| Network Security |
| Profiles |
| Report |
| SIM |
| Site Services |
| Site Settings |
| Tools |
| Transmission |
| VPN |
| Wired Networks |
| Wireless Networks |

## 5.3 Webhook

### 5.3.1 Webhook Message Template
The template of webhook message is as follows.

```json
{
  "Site": " site-name (Only the site-level log will have this field) ",
  "description": "This is a webhook message from Omada Controller",
  "shardSecret": "shard secret of webhook",
  "text": [
    "content of audit log"
  ],
  "Controller": "USA-Toast",
  "timestamp": 1692128478856
}
```

### 5.4 Country

#### 5.4.1 Country Template

```
Country Name/Country Code/Calling Code

Afghanistan/AF/+93
Albania/AL/+355
Algeria/DZ/+213
Angola/AO/+244
Anguilla/AI/+1264
Antigua and Barbuda/AG/+268
Argentina/AR/+54
Armenia/AM/+374
Aruba/AW/+297
Australia/AU/+61
Austria/AT/+43
Azerbaijan/AZ/+994
Bahamas/BS/+1242
Bahrain/BH/+973
Bangladesh/BD/+880
Barbados/BB/+1246
Belarus/BY/+375
Belgium/BE/+32
Belize/BZ/+501
Benin/BJ/+229
Bermuda/BM/+1441
Bhutan/BT/+975
Bolivia/BO/+591
Botswana/BW/+267
Brasil/BR/+55
Brunei/BN/+673
Burkina Faso/BF/+226
Burundi/BI/+257
Cabo Verde/CV/+238
Cambodia/KH/+855
Cameroon/CM/+237
Canada/CA/+1
Cayman Islands/KY/+1345
Central African/CF/+236
Chad/TD/+235
Chile/CL/+56
China/CN/+86
Christmas Island/CX/+618
Colombia/CO/+57
Comoros/KM/+269
Congo/CD/+243
Congo/CG/+242
Costa Rica/CR/+506
Cote d'Ivoire/CI/+225
Croatia/HR/+385
Cuba/CU/+53
Cyprus/CY/+357
Czech/CZ/+420
Denmark/DK/+45
Djibouti/DJ/+253
Dominica/DM/+1767
Dominican/DO/+1809
Dominican/DO/+1829
Dominican/DO/+1849
Ecuador/EC/+593
Egypt/EG/+20
Equatorial Guinea/GQ/+240
Eritrea/ER/+291
Estonia/EE/+372
Ethiopia/ET/+251
Falkland Islands/FK/+500
Fiji/FJ/+679
Finland/FI/+358
France/FR/+33
French Guiana/GF/+594
French Polynesia/PF/+689
Gabon/GA/+241
Gambia/GM/+220
Georgia/GE/+995
Germany/DE/+49
Ghana/GH/+233
Greece/GR/+30
Greenland/GL/+45
Grenada/GD/+1473
Guam/GU/+1
Guatemala/GT/+502
Guinea/GN/+224
Guinea-Bissau/GW/+245
Guyana/GY/+592
Haiti/HT/+509
Honduras/HN/+504
Hong Kong/HK/+852
Hungary/HU/+36
Iceland/IS/+354
India/IN/+91
Indonesia/ID/+62
Iran/IR/+98
Iraq/IQ/+964
Ireland/IE/+353
Israel/IL/+972
Italy/IT/+39
Jamaica/JM/+876
Japan/JP/+81
Jordan/JO/+962
Kazakhstan/KZ/+7
Kenya/KE/+254
Kiribati/KI/+686
Korea/KR/+82
Kuwait/KW/+965
Kyrgyzstan/KG/+996
Lao/LA/+856
Latvia/LV/+371
Lebanon/LB/+961
Lesotho/LS/+266
Liberia/LR/+231
Libya/LY/+218
Liechtenstein/LI/+423
Lithuania/LT/+370
Luxembourg/LU/+352
Macao/MO/+853
Macedonia/MK/+389
Madagascar/MG/+261
Malawi/MW/+265
Malaysia/MY/+60
Maldives/MV/+960
Mali/ML/+223
Malta/MT/+356
Marshall Islands/MH/+692
Mauritania/MR/+222
Mauritius/MU/+230
Mexico/MX/+52
Micronesia/FM/+691
Moldova/MD/+373
Monaco/MC/+377
Mongolia/MN/+976
Montenegro/ME/+382
Morocco/MA/+212
Mozambique/MZ/+258
Myanmar/MM/+95
Namibia/NA/+264
Nauru/NR/+674
Nepal/NP/+977
Netherlands/NL/+31
Netherlands Antilles/AN/+599
New Caledonia/NC/+687
New Zealand/NZ/+64
Nicaragua/NI/+505
Niger/NE/+227
Nigeria/NG/+234
Niue/NU/+683
North Korea/KP/+850
Norway/NO/+47
Oman/OM/+968
Pakistan/PK/+92
Palau/PW/+680
Palestine/PS/+970
Panama/PA/+507
Papua New Guinea/PG/+675
Paraguay/PY/+595
Peru/PE/+51
Philippines/PH/+63
Pitcairn Islands/PN/+64
Poland/PL/+48
Portuguese/PT/+351
Puerto Rico/PR/+1787
Puerto Rico/PR/+1939
Qatar/QA/+974
Romania/RO/+40
Russia/RU/+7
Rwanda/RW/+250
Saint Kitts and Nevis/KN/+1869
Saint Lucia/LC/+1758
Saint Vincent and the Grenadines/VC/+1784
Saint-Martin/MF/+1721
Salvador/SV/+503
Samoa/WS/+685
San Marino/SM/+378
Sao Tome and Principe/ST/+239
Saudi Arabia/SA/+966
Senegal/SN/+221
Serbia/RS/+381
Seychelles/SC/+248
Sierra Leone/SL/+232
Singapore/SG/+65
Slovak/SK/+421
Slovenia/SI/+386
Solomon Islands/SB/+677
Somalia/SO/+252
South Africa/ZA/+27
South Sudan/SS/+211
Spain/ES/+34
Sri Lanka/LK/+94
Sudan/SD/+249
Suriname/SR/+597
Swaziland/SZ/+268
Sweden/SE/+46
Swiss/CH/+41
Syria/SY/+963
Taiwan/TW/+886
Tajikistan/TJ/+992
Tanzania/TZ/+255
Thailand/TH/+66
The Cook Islands/CK/+682
The Turks and Caicos Islands/TC/+1649
The United States Virgin Islands/VI/+1340
Timor-Leste/TL/+670
Togo/TG/+228
Tokelau/TK/+690
Tonga/TO/+676
Trinidad and Tobago/TT/+1868
Tunisia/TN/+216
Turkey/TR/+90
Turkmenistan/TM/+993
Tuvalu/TV/+688
Uganda/UG/+256
Ukraine/UA/+380
United Arab Emirates/AE/+971
United Kingdom/UK/+44
United States/US/+1
Uruguay/UY/+598
Uzbekistan/UZ/+998
Vanuatu/VU/+678
Vatican/VA/+379
Venezuela/VE/+58
Vietnam/VN/+84
Yemen/YE/+967
Zambia/ZM/+260
Zimbabwe/ZW/+263
```

## 5.5 Protocol

### 5.5.1 ACL Protocol Template

```
ACL Protocol	Code Integer
ICMP	1
GGP	3
IP/IPENCAP	4
ST	5
TCP	6
EGP	8
IGP	9
PUP	12
UDP	17
HMP	20
XNS-IDP	22
RDP	27
ISO-TP4	29
DCCP	33
XTP	36
DDP	37
IDRP-CMTP	38
IDRP	45
RSVP	46
GRE	47
ESP	50
AH	51
SKIP	57
VMTP	81
EIGRP	88
OSPF	89
AX.25	93
IPIP	94
EtherIP	97
ENCAP	98
PIM	103
IPComp	108
VRRP	112
L2TP	115
IS-IS	124
SCTP	132
FC	133
Mobility Header	135
UDP-Lite	136
MPLS-in-IP	137
MANET	138
HIP	139
Shim6	140
WESP	141
ROHC	142
ALL	256
5.5.2 Routing Protocol Template
Routing Protocol	Code Integer
ICMP	1
GGP	3
IP	4
ST	5
TCP	6
EGP	8
IGP	9
PUP	12
UDP	17
HMP	20
XNS-IDP	22
RDP	27
ISO-TP4	29
DCCP	33
XTP	36
DDP	37
IDRP-CMTP	38
IDRP	45
RSVP	46
GRE	47
ESP	50
AH	51
SKIP	57
VMTP	81
EIGRP	88
OSPF	89
AX.25	93
IPIP	94
EtherIP	97
ENCAP	98
PIM	103
IPComp	108
VRRP	112
L2TP	115
IS-IS	124
SCTP	132
FC	133
Mobility Header	135
UDP-Lite	136
MPLS-in-IP	137
MANET	138
HIP	139
Shim6	140
WESP	141
ROHC	142
VOIP	255
ALL	256
```

## 5.6 Log

### 5.6.1 Log Notification Key

Some interfaces may require Log Notification Key. The tables below lists the Log Notification Key of the controller.

#### 5.6.1.1 Msp Level

| Module | Log Notification Key | Log Notification Name | Pro | Non-Pro | Restriction |
| --- | --- | --- | --- | --- | --- |
| Operation | LOGIN_OK | User Logged In | No Support | Support | -- |
| Operation | LOGIN_FL | User Login Failed | No Support | Support | -- |
| Operation | MSP_DEV_MOVED_OK | Device Moved to another Customer | No Support | Support | -- |
| Operation | MSP_DEV_MOVED_FL | Device Move to another Customer Failed | No Support | Support | -- |
| System | RO_O_SS | Running Out Of Storage Space | Support | Support | No Support on CBC |
| System | MSP_LOG_MAIL_OK | MSP Logs Mailed Automatically | Support | Support | -- |
| System | MSP_LOG_MAIL_FL | Automatic MSP Logs Mail Failed | Support | Support | -- |
| System | MSP_LOG_SRV_OK | MSP Logs Sent to Log Server | Support | Support | -- |
| System | MSP_LOG_SRV_FL | Sending MSP Logs to Log Server Failed | Support | Support | -- |
| Device | DEV_DISCOVER | Device Discovered | Support | Support | -- |
| System | MNG_PORT_C | Controller Access Port Changed | Support | Support | No Support on CBC |
| System | PRT_PORT_C | Portal Port Changed | Support | Support | No Support on CBC |
| System | CONNECTED_CLOUD_ACCESS_SUCCESS | Cloud Access Success | Support | Support | No Support on CBC |
| System | CLOUD_ACCESS_CONNECTION_FAILED | Network Disconnection | Support | Support | No Support on CBC |
| System | CLOSE_CLOUD_ACCESS_SUCCESS | Cloud Access Closed | Support | Support | No Support on CBC |

### 5.6.1.2 Global Level

| Module | Log Notification Key | Log Notification Name | Pro | Non-Pro | On Customer Level | Restriction |
| --- | --- | --- | --- | --- | --- | --- |
| Operation | LOGIN_OK | User Logged In | No Support | Support | No Support | -- |
| Operation | LOGIN_FL | User Login Failed | No Support | Support | No Support | -- |
| Operation | HS_LOGIN_OK | Hotspot Operator Logged In | No Support | Support | Support | -- |
| Operation | HS_LOGIN_FL | Hotspot Operator Login Failed | No Support | Support | Support | -- |
| Operation | SITE_ADD | Site Created | No Support | Support | Support | -- |
| Operation | SITE_MIGR | Site Migrated | No Support | Support | Support | -- |
| System | AUTO_BK_OK | Auto Backup Executed | Support | Support | Support | -- |
| System | AUTO_BK_FL | Auto Backup Failed | Support | Support | Support | -- |
| System | RO_O_SS | Running Out Of Storage Space | Support | Support | No Support | No Support on CBC |
| System | GLOBAL_LOG_MAIL_OK | Global Logs Mailed Automatically | Support | Support | Support | -- |
| System | GLOBAL_LOG_MAIL_FL | Automatic Global Logs Mail Failed | Support | Support | Support | -- |
| System | DEVICE_LIST_MAIL_FL | Device List Schedule Mail Failed | Support | Support | Support | -- |
| System | NETWORK_CHECK_MAIL_FL | Network check Mail Failed | Support | Support | Support | Only Support on OC |
| System | DEVICE_LIST_SCHEDULE_EXECUTED | Device List Schedule Executed | Support | Support | Support | -- |
| System | GLOBAL_LOG_SRV_OK | Global Logs Sent to Log Server | Support | Support | Support | -- |
| System | GLOBAL_LOG_SRV_FL | Sending Global Logs to Log Server Failed | Support | Support | Support | -- |
| Device | DEV_DISCOVER | Device Discovered | Support | Support | Support | -- |
| System | MNG_PORT_C | Controller Access Port Changed | Support | Support | No Support | No Support on CBC |
| System | PRT_PORT_C | Portal Port Changed | Support | Support | No Support | No Support on CBC |
| System | LOG_FULL | Log Full | Support | Support | Support | Only Support on OC |
| System | EMAIL_LIMIT_REACHED | Email Limit Reached | Support | Support | Support | -- |
| System | CONNECTED_CLOUD_ACCESS_SUCCESS | Cloud Access Success | Support | Support | Support | No Support on CBC |
| System | CLOUD_ACCESS_CONNECTION_FAILED | Network Disconnection | Support | Support | Support | No Support on CBC |
| System | CLOSE_CLOUD_ACCESS_SUCCESS | Cloud Access Closed | Support | Support | Support | No Support on CBC |

### 5.6.1.3 Site Level

| Module | Log Notification Key | Log Notification Name | Pro Controller | Non-Pro Controller | Restriction |
| --- | --- | --- | --- | --- | --- |
| Operation | ADV_FEA_EN | Advanced Features Enabled | No Support | Support | -- |
| Operation | MVLAN_CH | Management VLAN Changed | No Support | Support | -- |
| Operation | VOCH_ADD | Voucher Created | No Support | Support | -- |
| Operation | VOCH_DEL | Voucher Deleted | No Support | Support | -- |
| Operation | FORM_ADD | Form Auth Created | No Support | Support | -- |
| Operation | FORM_DEL | Form Auth Deleted | No Support | Support | -- |
| Operation | AP_ROLL_UP | Rolling Upgrade Triggered | No Support | Support | -- |
| Operation | DEV_ADOPT_OK | Device Adopted | No Support | Support | -- |
| Operation | DEV_ADOPT_FL | Device Adoption Failed | No Support | Support | -- |
| Operation | DEV_ADOPT_BATCH | Device Adoption in Batch | No Support | Support | -- |
| Operation | DEV_REBOOT | Device Rebooted | No Support | Support | -- |
| Operation | DEV_REBOOT_FL | Device Reboot Failed | No Support | Support | -- |
| Operation | DEV_FORGET_OK | Device Forgotten | No Support | Support | -- |
| Operation | DEV_FORGET_FL | Device Forgotten Failed | No Support | Support | -- |
| Operation | STACK_FORGET_OK | Switch Stack Forgotten | No Support | Support | -- |
| Operation | STACK_FORGET_FL | Switch Stack Forgotten Failed | No Support | Support | -- |
| Operation | STACK_OPT | Switch Stack Created/ Deleted | No Support | Support | -- |
| Operation | DEV_FORGET_BATCH | Device Forgotten in Batch | No Support | Support | -- |
| Operation | DEV_MOVED_OK | Device Moved | No Support | Support | -- |
| Operation | DEV_MOVED_FL | Device Move Failed | No Support | Support | -- |
| Operation | WLAN_OPT | WLAN Group Added/ Deleted | No Support | Support | -- |
| Operation | SSID_OPT | Wireless Network Created/Deleted | No Support | Support | -- |
| Operation | DEV_MAN_UP_OK | Device Upgraded Manually | No Support | Support | -- |
| Operation | DEV_MAN_UP_FL | Device Manual Upgrade Failed | No Support | Support | -- |
| Operation | STACK_MAN_UP_OK | Switch Stack Upgraded Manually | No Support | Support | -- |
| Operation | STACK_MAN_UP_FL | Switch Stack Manual Upgrade Failed | No Support | Support | -- |
| Operation | DEV_UP_CANCEL | Device Upgrade Cancelled | No Support | Support | -- |
| Operation | C_BLOCK | Client Blocked | No Support | Support | -- |
| Operation | C_UNBLOCK | Client Unblocked | No Support | Support | -- |
| System | REBOOT_SC_OK | Reboot Schedule Executed | Support | Support | -- |
| System | REBOOT_SC_FL | Reboot Schedule Execution Failed | Support | Support | -- |
| System | POE_SC_OK | PoE Schedule Executed | Support | Support | -- |
| System | POE_SC_FL | PoE Schedule Execution Failed | Support | Support | -- |
| System | PORT_SC_OK | Port Schedule Executed | Support | Support | -- |
| System | PORT_SC_FL | Port Schedule Execution Failed | Support | Support | -- |
| System | LOG_MAIL_OK | Logs Mailed Automatically | Support | Support | -- |
| System | LOG_MAIL_FL | Automatic Logs Mail Failed | Support | Support | -- |
| System | SITE_DEVICE_LIST_MAIL_FL | Site Device List Schedule Mail Failed | Support | Support | -- |
| System | SITE_NETWORK_CHECK_MAIL_FL | Site Network check Mail Failed | Support | Support | -- |
| System | TERMINAL_MAIL_FL | Site Terminal Mail Failed | Support | Support | -- |
| System | SITE_DEVICE_LIST_SCHEDULE_EXECUTED | Site Device List Schedule Executed | Support | Support | -- |
| System | LOG_SRV_OK | Site Logs Sent to Log Server | Support | Support | -- |
| System | LOG_SRV_FL | Sending Site Logs to Log Server Failed | Support | Support | -- |
| Device | DEV_DISCONN | Device Disconnected | Support | Support | -- |
| Device | DEV_CONN | Device Connected | Support | Support | -- |
| Device | AP_ISOLATE | EAP Isolated | Support | Support | -- |
| Device | DEV_IP_C | Device IP Changed | Support | Support | -- |
| Device | AP_RADAR | EAP Detected Radar | Support | Support | -- |
| Device | DEV_UP_OL_OK | Device Upgrade Online | No Support | Support | -- |
| Device | DEV_UP_OL_FL | Device Upgrade Online Failed | No Support | Support | -- |
| Device | STACK_UP_OL_OK | Switch Stack Upgrade Online | No Support | Support | -- |
| Device | STACK_UP_OL_FL | Switch Stack Upgrade Online No Support | Support | Support | -- |
| Device | DEV_READOPT_OK | Device Readopted Automatically | Support | Support | -- |
| Device | DEV_READOPT_FL | Automatic Device Readopt Failed | Support | Support | -- |
| Device | AP_CH_C | EAP Channel Changed | Support | Support | -- |
| Device | OSG_WAN_UP | WAN is up | Support | Support | -- |
| Device | OSG_WAN_DOWN | WAN is down | Support | Support | -- |
| Device | OSG_BK_WAN_UP | Backup WAN Takes Effect | Support | Support | -- |
| Device | OSG_PRI_WAN_UP | Primary WAN Recovered | Support | Support | -- |
| Device | WAN_ONLINE_DETECTION | WAN Online Detection | Support | Support | -- |
| Device | WAN_LINK_BACKUP | WAN Link Backup | Support | Support | -- |
| Device | OSG_ATK | Gateway Detected Attack | Support | Support | -- |
| Device | OSG_SF_ATK | Gateway Detected Stationary Flood Attack | Support | Support | -- |
| Device | OSG_ARP_ATK | Gateway Detected ARP Conflicts | Support | Support | -- |
| Device | OSW_DET_STORM | Switch Detected Storm | Support | Support | -- |
| Device | OSW_DET_LOOP | Detected Loops | Support | Support | -- |
| Device | OSW_PB | Port Blocked | Support | Support | -- |
| Device | OSW_LOOP_C | Loop Cleared | Support | Support | -- |
| Device | OSG_IPSEC_OK | IPsec Connection Established | Support | Support | -- |
| Device | OSG_IPSEC_FL | IPsec Connection Disconnected | Support | Support | -- |
| Device | OSG_IPSEC_FO | IPsec failover took effect | Support | Support | -- |
| Device | OSG_C_VPN_OK | PPTP/L2TP Client Connected | Support | Support | -- |
| Device | OSG_C_VPN_FL | PPTP/L2TP Client Connection Failed | Support | Support | -- |
| Device | OSG_RC_VPN_OK | Remote PPTP/L2TP Client Connected | Support | Support | -- |
| Device | OSG_RC_VPN_FL | Remote PPTP/L2TP Client Connection Failed | Support | Support | -- |
| Device | OSG_RC_VPN_LO | Remote PPTP/L2TP Client Logged Out | Support | Support | -- |
| Device | OSG_PPPOE_OK | PPPoE Connection Established | Support | Support | -- |
| Device | OSG_PPPOE_FL | PPPoE Connection Failed | Support | Support | -- |
| Device | OSW_TOPO_C | STP Topology Changed | Support | Support | -- |
| Client | AP_C_FL | Client Connection Failed (Wireless) | Support | Support | -- |
| Client | AP_C_OK | Client Online (Wireless) | Support | Support | -- |
| Client | W_C_PRT_OK | Client Authenticated with Portal (Wireless) | Support | Support | -- |
| Client | W_C_PRT_FL | Portal Authentication Failed (Wireless) | Support | Support | -- |
| Client | W_C_PRT_EXP | Client Authentication Expired (Wireless) | Support | Support | -- |
| Client | W_C_DISCONN | Client Offline (Wireless) | Support | Support | -- |
| Client | W_C_ROAM | Client Roaming (Wireless) | Support | Support | -- |
| Client | L_C_CONN | Client Online (Wired) | Support | Support | -- |
| Client | L_C_PTR_OK | Client Authenticated with Portal (Wired) | Support | Support | -- |
| Client | L_C_PTR_FL | Portal Authentication Failed (Wired) | Support | Support | -- |
| Client | L_C_AUTH_EXP | Client Authenticated Expired (Wired) | Support | Support | -- |
| Client | L_C_DISCONN | Client Offline (Wired) | Support | Support | -- |
| Client | C_AUTH_OPT | Client Authorized/Unauthorized by Admin | Support | Support | -- |
| Client | C_PRT_EXT | Client Authentication Extended by Admin | Support | Support | -- |
| Client | OSW_C_1X_OK | Client Authenticated with 802.1X | Support | Support | -- |
| Client | OSW_C_1X_FL | 802.1X Authentication Failed | Support | Support | -- |
| Device | DEV_C_DSYNC | Device Configurations Desynchronized | Support | Support | -- |
| Device | WAN_IP_O_F | WAN IP address Obtaining Failed | Support | Support | -- |
| System | REPORT_GENERATION_FAILED | Report Generation Failed | Support | Support | -- |
| System | REPORT_SENDING_FAILED | Report Sending Failed | Support | Support | -- |
| System | REPORT_SCHEDULE_EXECUTED | Report Schedule Executed | Support | Support | -- |
| Device | OSG_LARGE_PING_ATTACK | Large Ping Attack | Support | Support | -- |
| Device | OSG_DDNS | Gateway DDNS Module Information | Support | Support | -- |
| Device | OSG_IPSEC | Gateway IPsec Module Information | Support | Support | -- |
| Device | OSG_IPV6 | Gateway IPv6 Module Information | Support | Support | -- |
| Device | OSG_PPP | Gateway PPP Module Information | Support | Support | -- |
| Device | OSG_PPPOE | Gateway PPPoE Module Information | Support | Support | -- |
| Device | OSG_SSL_VPN | Gateway SSL VPN Module Information | Support | Support | -- |
| Device | OSG_DHCP_C | Gateway DHCP Client Module Information | Support | Support | -- |
| Device | OSG_DHCP_S | Gateway DHCP Server Module Information | Support | Support | -- |
| System | INCIDENT_MAILED_FAILED | Incidents auto mailed failed | No Support on Basic Site | No Support | -- |
| System | DST_C_FAIL | DST configuration error. | Support | Support | No Support on CBC |
| Device | OSG_DHCP_LEASE_POOL_EXHAUSTED | The DHCP lease pool is exhausted | Support | Support | -- |
| Device | OSG_ROGUE_DHCP_SERVER_DETECTED | A rogue DHCP server is detected | Support | Support | -- |
| Device | OSG_IP_CONFLICT_DETECTED | An IP conflict is detected | Support | Support | -- |
| Device | OSW_OUI_BASED_VLAN_EFFECT | Switch OUI Based VLAN rule applied | No Support on Basic Site | No Support | -- |
| Device | OSW_OUI_BASED_VLAN_NUM_LIMIT_EXCEED | Switch OUI Based VLAN rules exceeded the maximum simultaneous entry limit | No Support on Basic Site | No Support | -- |

## 5.7 Insight

### 5.7.1 Insight Notification Key

Some interfaces may require Insight Notification Key. The tables below lists the Insight Notification Key of the controller.

#### 5.7.1.1 Event Category Key

| Event Category | Event Category Key |
| --- | --- |
| Web | Event category Key |
| Networking | networking |
| Mesh | mesh |
| Access | access |
| Roaming | roaming |
| Network Service | networkService |
| Software/Configuration | software |
| Hardware | hardware |
| Security | security |
| Throughput | throughput |
| Coverage | cover |

### 5.7.2 Anomaly Settings

#### 5.7.2.1 Effective parameter ranges for each event
The table below lists the effective parameter ranges for each event.

| Anomaly Code | Params and Effective Range |
| --- | --- |
| 01001001 | offlineCount[1, 15] |
| 01001003 | avgDisconnectCount[1, 100], disconnectApPercent[1, 100], disconnectCount[1, 100] |
| 01002001 | count[1, 100], threshold[-90, -60] |
| 01002003 | -- |
| 01002004 | -- |
| 01002005 | -- |
| 01003001 | -- |
| 01003002 | offlineCount[1, 15] |
| 01003004 | threshold[1, 100] |
| 01003005 | -- |
| 01003007 | threshold[1, 100] |
| 01003010 | threshold[1, 100] |
| 01003011 | threshold[1, 100] |
| 01003013 | -- |
| 01004001 | threshold[1, 100] |
| 01004002 | threshold[2, 100] |
| 01004003 | threshold[1, 100] |
| 01004004 | duration[1, 5], threshold[1, 100] |
| 01006001 | -- |
| 01007001 | count[1, 100], threshold[1, 100] |
| 01009001 | count[1, 100], threshold[1, 100] |
| 01009002 | count[1, 100], threshold[1, 100] |
| 01009003 | count[1, 100] |
| 01009004 | count2g[1, 100], count5g[1, 100], count5g2[1, 100], count6g[1, 100] |
| 01009006 | throughput2g[1, 4950], util2g[1, 100], throughput5g[1, 4950], util5g[1, 100], throughput5g2[1, 4950], util5g2[1, 100], throughput6g[1, 4950], util6g[1, 100] |
| 01009007 | count[1, 100], threshold[1, 100] |
| 01009008 | count[1, 100], threshold[1, 100] |
| 01009009 | count[1, 100], threshold[-90, -60] |
| 01009010 | count[1, 100], threshold[1, 100] |
| 01009011 | count2g[1, 100], count5g[1, 100], count5g2[1, 100], count6g[1, 100], threshold2g[1, 100], threshold5g[1, 100], threshold5g2[1, 100], threshold6g[1, 100] |
| 01009012 | count2g[1, 100], count5g[1, 100], count5g2[1, 100], count6g[1, 100], threshold2g[1, 100], threshold5g[1, 100], threshold5g2[1, 100], threshold6g[1, 100] |
| 01010001 | lowerThreshold2g[-95, -46], upperThreshold2g[-46, 0], ratio2g[1, 100], lowerThreshold5g[-95, -46], upperThreshold5g[-46, 0], ratio5g[1, 100], lowerThreshold5g2[-95, -46], upperThreshold5g2[-46, 0], ratio5g2[1, 100], lowerThreshold6g[-95, -46], upperThreshold6g[-46, 0], ratio6g[1, 100] |
| 02001001 | offlineCount[1, 15] |
| 02003001 | -- |
| 02005002 | -- |
| 02005003 | -- |
| 02005004 | -- |
| 02007001 | -- |
| 02007002 | count[1, 100], threshold[1, 100] |
| 02008001 | -- |
| 02008002 | -- |
| 02009001 | count[1, 100], threshold[1, 100] |
| 02009002 | count[1, 100], threshold[1, 100] |
| 02009003 | count[1, 100], threshold[1, 5000] |
| 03001001 | -- |
| 03001002 | offlineCount[1, 15] |
| 03003001 | successRate[1, 100] |
| 03003002 | count[1, 100], threshold[1, 5000] |
| 03003003 | -- |
| 03003005 | -- |
| 03003008 | -- |
| 03003009 | -- |
| 03003010 | addressPoolRate[1, 100] |
| 03003011 | -- |
| 03005003 | -- |
| 03005004 | timeRange_s[1, 300], changedTimes[1, 100] |
| 03005005 | -- |
| 03005006 | -- |
| 03005007 | -- |
| 03005009 | -- |
| 03005010 | -- |
| 03007008 | -- |
| 03007009 | -- |
| 03007011 | count[1, 100], threshold[1, 100] |
| 03007013 | count[1, 100], threshold[1, 100] |
| 03007015 | timeRange[1, 60], changedTimes[1, 100] |
| 03007016 | -- |
| 03008001 | retryCnt[1, 100] |
| 03009001 | count[1, 100], threshold[1, 100] |
| 03009002 | count[1, 100], threshold[1, 100] |
| 03009003 | count[1, 100], threshold[1, 100] |
| 03009004 | -- |
| 04003001 | -- |
| 04003002 | threshold[1, 10] |
| 06003001 | threshold[1, 100] |
