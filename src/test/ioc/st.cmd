require stream

epicsEnvSet("STREAM_PROTOCOL_PATH", "$(E3_CMD_TOP)")
epicsEnvSet("PORT", "38081")
drvAsynIPPortConfigure("SIM", "127.0.0.1:$(PORT)", 0, 0, 0)
dbLoadRecords("$(E3_CMD_TOP)/simple.db", "P=TEST:,PORT=SIM")
