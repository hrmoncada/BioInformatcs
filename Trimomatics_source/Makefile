# http://semver.org/
VERSION := 0.38.0
INSTALL := ${HOME}   # /home/henry
SOURCES := $(shell find src/ -name "*.java" | sed 's|src/||g')

all:
	rm -rf classes; mkdir -p classes/; \
	cd src/; javac -classpath ".:../lib/jbzip2-0.9.jar" -d ../classes ${SOURCES}; \
	cd ../classes; jar xf ../lib/jbzip2-0.9.jar; \
	jar cmf ../MANIFEST.MF trimmomatic.jar ./

check:
	@echo "this package doesn't have any test (yet)"

install: 
	mkdir -p ${INSTALL}/TRIMHOME                       # Created folder /home/henry/TRIMHOME 
	cp classes/trimmomatic.jar ${INSTALL}/TRIMHOME/    # Copy  classes/trimmomatic.jar into  /home/henry/TRIMHOME/trimmomatic.jar
	cp -vrf * ${INSTALL}/TRIMHOME/

dist:
	mkdir -p trimmomatic-${VERSION}
	cp AUTHORS Makefile README trimmomatic-${VERSION}
	cp build.xml MANIFEST.MF versionHistory.txt trimmomatic-${VERSION}
	cp -r adapters distSrc lib/ src/ trimmomatic-${VERSION}
	tar -czvf trimmomatic-${VERSION}.tar.gz trimmomatic-${VERSION}/
	rm -rf trimmomatic-${VERSION}

clean:
	rm -rf classes/
