#
#  Copyright (c) 2007            Paul Scherrer Institute
#  Copyright (c) 2017 - Present  European Spallation Source ERIC
#  Copyright (c) 2019            Jeong Han Lee
#
#  The program is free software: you can redistribute
#  it and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation, either version 2 of the
#  License, or any newer version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  this program. If not, see https://www.gnu.org/licenses/gpl-2.0.txt
#
#  PSI original author : Dirk Zimoch
#
#  ESS specific author  : Jeong Han Lee
#               email   : han.lee@esss.se
#               date    : Thursday, March  7 22:27:55 CET 2019
#               version : 0.0.3
#
#

include $(E3_REQUIRE_TOOLS)/driver.makefile

<<<<<<< HEAD
=======
#USR_CPPFLAGS += -DUSE_TYPED_RSET

>>>>>>> 076709a (Updated build configuration for require 6)
APP:=.
APPDB:=$(APP)/Db
APPSRC:=$(APP)/src

### CONFIG_STREAM START
RECORDTYPES += ao ai
RECORDTYPES += bo bi
RECORDTYPES += mbbo mbbi
RECORDTYPES += mbboDirect mbbiDirect
RECORDTYPES += longout longin
RECORDTYPES += stringout stringin
RECORDTYPES += waveform
RECORDTYPES += calcout
RECORDTYPES += aai aao

ifdef BASE_3_15
RECORDTYPES += lsi lso
endif
ifdef BASE_3_16
RECORDTYPES += int64in int64out
endif

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

### CONFIG_STREAM END


### GNUmakefile
SOURCES += $(RECORDTYPES:%=src/dev%Stream.c)
SOURCES += $(FORMATS:%=src/%Converter.cc)
SOURCES += $(BUSSES:%=src/%Interface.cc)
SOURCES += $(wildcard src/Stream*.cc)

## E3 Specific
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

<<<<<<< HEAD
LIB_LIBS += pcre asyn calc
=======
LIB_LIBS += pcre asyn
>>>>>>> 076709a (Updated build configuration for require 6)

SCRIPTS += $(wildcard ./iocsh/*.iocsh)

StreamCore$(DEP): streamReferences

# Build StreamVersion before everything
$(addsuffix $(DEP),$(notdir $(basename $(SOURCES)))): StreamVersion.h
# These are a bit special due to the wildcard above
StreamVersion$(DEP) StreamEpics$(DEP): StreamVersion.h

StreamVersion.h: ../$(APPSRC)/../.VERSION
	@echo Creating $@
	perl -CSD $(where_am_I)$(APPSRC)/makeStreamVersion.pl $@


# the original StreamDevice GNUMakefile uses perl
# I would like to use EPICS PERL instead of perl
# $PERL = perl -CSD

streamReferences:
	$(PERL) $(where_am_I)$(APPSRC)/makeref.pl Interface $(BUSSES)   > $@
	$(PERL) $(where_am_I)$(APPSRC)/makeref.pl Converter $(FORMATS) >> $@

export DBDFILES = streamSup.dbd

streamSup.dbd:
	@echo Creating $@
	$(PERL) $(where_am_I)$(APPSRC)/makedbd.pl $(RECORDTYPES) > $@
