# getAndroidSecurityLevel
**getAospSecurityPatchLevel.py** uses scrapy to retrieve the latest Android security patch level value from following URL https://source.android.com/security/bulletin#bulletins
<br>The returned value is to be checked against Build.VERSION.SECURITY_PATCH retrieved from the device.
<br>Example:
<br>~$ scrapy runspider getAospSecurityPatchLevel.py --nolog
<br>2021-04-01
