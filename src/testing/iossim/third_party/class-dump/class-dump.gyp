# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'class-dump',
      'toolsets': ['host'],
      'type': 'executable',
      'sources': [
        'src/CDBalanceFormatter.h',
        'src/CDBalanceFormatter.m',
        'src/CDClassDump.h',
        'src/CDClassDump.m',
        'src/CDClassDumpVisitor.h',
        'src/CDClassDumpVisitor.m',
        'src/CDClassFrameworkVisitor.h',
        'src/CDClassFrameworkVisitor.m',
        'src/CDDataCursor.h',
        'src/CDDataCursor.m',
        'src/CDFatArch.h',
        'src/CDFatArch.m',
        'src/CDFatFile.h',
        'src/CDFatFile.m',
        'src/CDFile.h',
        'src/CDFile.m',
        'src/CDFindMethodVisitor.h',
        'src/CDFindMethodVisitor.m',
        'src/CDLCDyldInfo.h',
        'src/CDLCDyldInfo.m',
        'src/CDLCDylib.h',
        'src/CDLCDylib.m',
        'src/CDLCDylinker.h',
        'src/CDLCDylinker.m',
        'src/CDLCDynamicSymbolTable.h',
        'src/CDLCDynamicSymbolTable.m',
        'src/CDLCEncryptionInfo.h',
        'src/CDLCEncryptionInfo.m',
        'src/CDLCLinkeditData.h',
        'src/CDLCLinkeditData.m',
        'src/CDLCPrebindChecksum.h',
        'src/CDLCPrebindChecksum.m',
        'src/CDLCPreboundDylib.h',
        'src/CDLCPreboundDylib.m',
        'src/CDLCRoutines32.h',
        'src/CDLCRoutines32.m',
        'src/CDLCRoutines64.h',
        'src/CDLCRoutines64.m',
        'src/CDLCRunPath.h',
        'src/CDLCRunPath.m',
        'src/CDLCSegment.h',
        'src/CDLCSegment.m',
        'src/CDLCSegment32.h',
        'src/CDLCSegment32.m',
        'src/CDLCSegment64.h',
        'src/CDLCSegment64.m',
        'src/CDLCSubClient.h',
        'src/CDLCSubClient.m',
        'src/CDLCSubFramework.h',
        'src/CDLCSubFramework.m',
        'src/CDLCSubLibrary.h',
        'src/CDLCSubLibrary.m',
        'src/CDLCSubUmbrella.h',
        'src/CDLCSubUmbrella.m',
        'src/CDLCSymbolTable.h',
        'src/CDLCSymbolTable.m',
        'src/CDLCTwoLevelHints.h',
        'src/CDLCTwoLevelHints.m',
        'src/CDLCUUID.h',
        'src/CDLCUUID.m',
        'src/CDLCUnixThread.h',
        'src/CDLCUnixThread.m',
        'src/CDLCUnknown.h',
        'src/CDLCUnknown.m',
        'src/CDLoadCommand.h',
        'src/CDLoadCommand.m',
        'src/CDMachO32File.h',
        'src/CDMachO32File.m',
        'src/CDMachO64File.h',
        'src/CDMachO64File.m',
        'src/CDMachOFile.h',
        'src/CDMachOFile.m',
        'src/CDMethodType.h',
        'src/CDMethodType.m',
        'src/CDMultiFileVisitor.h',
        'src/CDMultiFileVisitor.m',
        'src/CDOCCategory.h',
        'src/CDOCCategory.m',
        'src/CDOCClass.h',
        'src/CDOCClass.m',
        'src/CDOCIvar.h',
        'src/CDOCIvar.m',
        'src/CDOCMethod.h',
        'src/CDOCMethod.m',
        'src/CDOCModule.h',
        'src/CDOCModule.m',
        'src/CDOCProperty.h',
        'src/CDOCProperty.m',
        'src/CDOCProtocol.h',
        'src/CDOCProtocol.m',
        'src/CDOCSymtab.h',
        'src/CDOCSymtab.m',
        'src/CDObjectiveC1Processor.h',
        'src/CDObjectiveC1Processor.m',
        'src/CDObjectiveC2Processor32.h',
        'src/CDObjectiveC2Processor32.m',
        'src/CDObjectiveC2Processor64.h',
        'src/CDObjectiveC2Processor64.m',
        'src/CDObjectiveCProcessor.h',
        'src/CDObjectiveCProcessor.m',
        'src/CDRelocationInfo.h',
        'src/CDRelocationInfo.m',
        'src/CDSearchPathState.h',
        'src/CDSearchPathState.m',
        'src/CDSection.h',
        'src/CDSection.m',
        'src/CDSection32.h',
        'src/CDSection32.m',
        'src/CDSection64.h',
        'src/CDSection64.m',
        'src/CDStructureInfo.h',
        'src/CDStructureInfo.m',
        'src/CDStructureTable.h',
        'src/CDStructureTable.m',
        'src/CDSymbol.h',
        'src/CDSymbol.m',
        'src/CDSymbolReferences.h',
        'src/CDSymbolReferences.m',
        'src/CDTextClassDumpVisitor.h',
        'src/CDTextClassDumpVisitor.m',
        'src/CDTopoSortNode.h',
        'src/CDTopoSortNode.m',
        'src/CDTopologicalSortProtocol.h',
        'src/CDType.h',
        'src/CDType.m',
        'src/CDTypeController.h',
        'src/CDTypeController.m',
        'src/CDTypeFormatter.h',
        'src/CDTypeFormatter.m',
        'src/CDTypeLexer.h',
        'src/CDTypeLexer.m',
        'src/CDTypeName.h',
        'src/CDTypeName.m',
        'src/CDTypeParser.h',
        'src/CDTypeParser.m',
        'src/CDVisitor.h',
        'src/CDVisitor.m',
        'src/CDVisitorPropertyState.h',
        'src/CDVisitorPropertyState.m',
        'src/NSArray-Extensions.h',
        'src/NSArray-Extensions.m',
        'src/NSData-CDExtensions.h',
        'src/NSData-CDExtensions.m',
        'src/NSError-CDExtensions.h',
        'src/NSError-CDExtensions.m',
        'src/NSObject-CDExtensions.h',
        'src/NSObject-CDExtensions.m',
        'src/NSScanner-Extensions.h',
        'src/NSScanner-Extensions.m',
        'src/NSString-Extensions.h',
        'src/NSString-Extensions.m',
        'src/cd_objc2.h',
        'src/class-dump.m',
        'src/dyld-info-compat.h',
      ],
      'libraries': [
        '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
        '$(SDKROOT)/usr/lib/libcrypto.dylib',
      ],
      'xcode_settings': {
        'WARNING_CFLAGS': [
          '-Wno-format',
          '-Wno-deprecated',
        ],
      },
    },
  ],  # targets
}
