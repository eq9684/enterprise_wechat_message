# enterprise_wechat_message
send message to enterprise wechat

企业微信corpid和corpsecret通过CloudFormation部署在Secret Manager，不直接写到代码里  
lambda 需要读取secret manager的权限  
lambda 需要在vpc的私有子网执行，使用natgateway的EIP  
在企业微信app后台把EIP配置为可信IP  
