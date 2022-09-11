import urllib3
import json
import get_secret

def lambda_handler(event, context):
    #get enterprise wechat corpid and corpsecret from Secret Manager.
    secret = json.loads(get_secret.get_secret())
    corpid = secret['corpid']
    corpsecret = secret['corpsecret']
    print ('corpid is ' + corpid)
    print ('corpsecret is ' + corpsecret)
    
    #get access token through corpid and corpsecret, this token will expired after 7200 seconds.
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid  + '&corpsecret=' + corpsecret
    response = urllib3.PoolManager().request('GET', url, headers={})
    access_token = json.loads(response.data)['access_token']
    print ('access_token is ' + access_token)
    
    #send notification text message to enterprise wechat id @all.
    #reference url: https://developer.work.weixin.qq.com/document/path/90236
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    headers = {'Content-Type': 'application/json'}
    body = {
                "touser" : "WangHua",
                "msgtype" : "text",
                "agentid" : 1000002,
                "text" : {
                    "content" : "hello, this is a test message from Lambda"
                },
                "safe":0,
                "enable_id_trans": 0,
                "enable_duplicate_check": 0,
                "duplicate_check_interval": 1800
            }

    response = urllib3.PoolManager().request('POST', url, headers=headers, body=json.dumps(body))

    return {
        'statusCode': response.data,
    }
