# b4sic drozer exts

This is the result of some experiments with drozer. It features a super simple broadcastreceiver fuzzer, a gui for sending intents for broadcastreceivers and a drozer module to observe changes in folders. 

## Usage

On your smartphone or emulator a drozer client should be up and running. Also remember to forward the port:

```
adbsdk forward tcp:31415 tcp:31415
```

Also remember that only one drozer connection is possible to the standard drozer client at the same time. 

### Broadcast Receiver Tester

Just start the broad_tester.py in the broad_tester folder. 

### Broadcast Receiver Fuzzer

```
Usage:
python broad_fuzzer.py [packagename] [extra] [extra] ...

[extra]	e.g. string,test,test
```

For example:

```
python broad_fuzzer.py com.mwr.dz string,test,test2
```

To test the package com.mwr.dz (drozer client) with a string extra named "test" with the value "test2" 

### Drozer Fileobserver

The file observer is a module for the drozer console. Just open the drozer console and type

```
module repository enable /path/to/b4sic_drozer_exts/drozer_fileobserver/testrepo
```

Then the file observer can be run on the drozer console using 

```
run b4sic.fileobserver.classloading [packagename]
```
