#  Copyright (c) 2007            Paul Scherrer Institute
#  Copyright (c) 2017 - Present  European Spallation Source ERIC
#  Copyright (c) 2019            Jeong Han Lee

include $(E3_REQUIRE_TOOLS)/driver.makefile

APP:=.
APPDB:=$(APP)/Db
APPSRC:=$(APP)/src

RECORDTYPES += ao ai
RECORDTYPES += bo bi
RECORDTYPES += mbbo mbbi
RECORDTYPES += mbboDirect mbbiDirect
RECORDTYPES += longout longin
RECORDTYPES += stringout stringin
RECORDTYPES += waveform
RECORDTYPES += calcout
RECORDTYPES += aai aao
RECORDTYPES += lsi lso
RECORDTYPES += int64in int64out
RECORDTYPES += scalcout

BUSSES  += Debug
BUSSES  += Dummy
BUSSES  += AsynDriver

FORMATS += Enum
FORMATS += BCD
FORMATS += Raw
FORMATS += RawFloat
FORMATS += Binary
FORMATS += Checksum
FORMATS += MantissaExponent
FORMATS += Timestamp
FORMATS += Regexp

### GNUmakefile
SOURCES += $(RECORDTYPES:%=src/dev%Stream.c)
SOURCES += $(FORMATS:%=src/%Converter.cc)
SOURCES += $(BUSSES:%=src/%Interface.cc)
SOURCES += $(wildcard src/Stream*.cc)

### e3
SOURCES += $(APPSRC)/StreamVersion.c

### GNUmakefile
HEADERS += $(APPSRC)/devStream.h
HEADERS += $(APPSRC)/StreamFormat.h
HEADERS += $(APPSRC)/StreamFormatConverter.h
HEADERS += $(APPSRC)/StreamBuffer.h
HEADERS += $(APPSRC)/StreamError.h
HEADERS += $(APPSRC)/StreamVersion.h
HEADERS += $(APPSRC)/StreamProtocol.h
HEADERS += $(APPSRC)/StreamBusInterface.h
HEADERS += $(APPSRC)/StreamCore.h
HEADERS += $(APPSRC)/MacroMagic.h

USR_LIBS += pcre asyn calc

SCRIPTS += $(wildcard ./iocsh/*.iocsh)

StreamCore$(DEP): streamReferences

# Build StreamVersion before everything
$(addsuffix $(DEP),$(notdir $(basename $(SOURCES)))): StreamVersion.h
# These are a bit special due to the wildcard above
StreamVersion$(DEP) StreamEpics$(DEP): StreamVersion.h

StreamVersion.h: ../$(APPSRC)/../.VERSION
	@echo Creating $@
	perl -CSD $(where_am_I)$(APPSRC)/makeStreamVersion.pl $@

streamReferences:
	$(PERL) $(where_am_I)$(APPSRC)/makeref.pl Interface $(BUSSES)   > $@
	$(PERL) $(where_am_I)$(APPSRC)/makeref.pl Converter $(FORMATS) >> $@

export DBDFILES = streamSup.dbd

streamSup.dbd:
	@echo Creating $@
	$(PERL) $(where_am_I)$(APPSRC)/makedbd.pl $(RECORDTYPES) > $@
