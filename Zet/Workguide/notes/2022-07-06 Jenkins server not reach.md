---
title: 2022-07-06 Jenkins server not reach
created: 2022-Jul-06
tags:
  - 'permanent/common'
---

up:: [[Inphi Jenkins]]

```
SEVERE: http://sw.inphi-corp.local/jenkins/ provided port:36602 is not reachable
java.io.IOException: http://sw.inphi-corp.local/jenkins/ provided port:36602 is not reachable
	at org.jenkinsci.remoting.engine.JnlpAgentEndpointResolver.resolve(JnlpAgentEndpointResolver.java:314)
	at hudson.remoting.Engine.innerRun(Engine.java:694)
	at hudson.remoting.Engine.run(Engine.java:519)
```


From [[Ignacio]] for odsp:
1.  Open Windows Command Prompt
2.  Move to C:/usr/jenkins
3.  Run the following command 
	```
	java -jar agent.jar -jnlpUrl https://odsp-sqa-jenkins.marvell.com/computer/hcm-lab-1006/jenkins-agent.jnlp -secret 68fa2af3f8970867db823b47f9925f8e9d70628cca85d5002f52291abf39e6f8
	```
4.  You should get some logs on the terminal and a final message saying `INFO: Connected`
5.  Leave the cmd open