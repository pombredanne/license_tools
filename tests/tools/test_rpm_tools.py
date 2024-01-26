# Copyright (c) stefan6419846. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.

from __future__ import annotations

import sys
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory
from unittest import TestCase

import requests

from license_tools import retrieval
from license_tools.tools import rpm_tools
from tests.utils.test_archive_utils import download


class ExtractTestCase(TestCase):
    def test_unpack_rpm_file(self) -> None:
        url = "https://download.opensuse.org/distribution/leap/15.6/repo/oss/x86_64/libaio1-0.3.109-1.25.x86_64.rpm"
        with download(url, ".rpm") as path, TemporaryDirectory() as tempdir:
            directory = Path(tempdir)
            rpm_tools.extract(
                archive_path=path, target_path=directory
            )
            actual = [x[1] for x in retrieval.get_files_from_directory(directory)]
            self.assertEqual(
                [
                    "lib64/libaio.so.1",
                    "lib64/libaio.so.1.0.1",
                    "usr/share/doc/packages/libaio1/COPYING",
                    "usr/share/doc/packages/libaio1/TODO",
                ],
                actual,
            )


class CheckRpmHeadersTestCase(TestCase):
    maxDiff = None

    def test_binary(self) -> None:
        if sys.version_info < (3, 11):
            file_flags = "[<FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.DOC: 2>, <FileFlags.DOC: 2>]"
            file_verification_flags = "[<VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.0: 0>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>]"  # noqa: E501
            required_names_flags = "[<DependencyFlags.SCRIPT_POST|INTERP: 1280>, <DependencyFlags.SCRIPT_POSTUN|INTERP: 4352>, <DependencyFlags.FIND_REQUIRES: 16384>, <DependencyFlags.FIND_REQUIRES: 16384>, <DependencyFlags.RPMLIB|EQUAL|LESS: 16777226>, <DependencyFlags.RPMLIB|EQUAL|LESS: 16777226>, <DependencyFlags.RPMLIB|EQUAL|LESS: 16777226>, <DependencyFlags.RPMLIB|EQUAL|LESS: 16777226>]"  # noqa: E501
        else:
            file_flags = "[<FileFlags: 0>, <FileFlags: 0>, <FileFlags: 0>, <FileFlags.DOC: 2>, <FileFlags.DOC: 2>]"
            file_verification_flags = "[<VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags: 0>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>]"  # noqa: E501
            required_names_flags = "[<DependencyFlags.INTERP|SCRIPT_POST: 1280>, <DependencyFlags.INTERP|SCRIPT_POSTUN: 4352>, <DependencyFlags.FIND_REQUIRES: 16384>, <DependencyFlags.FIND_REQUIRES: 16384>, <DependencyFlags.LESS|EQUAL|RPMLIB: 16777226>, <DependencyFlags.LESS|EQUAL|RPMLIB: 16777226>, <DependencyFlags.LESS|EQUAL|RPMLIB: 16777226>, <DependencyFlags.LESS|EQUAL|RPMLIB: 16777226>]"  # noqa: E501

        url = "https://download.opensuse.org/distribution/leap/15.6/repo/oss/x86_64/libaio1-0.3.109-1.25.x86_64.rpm"
        with NamedTemporaryFile(suffix=".rpm") as rpm_file:
            rpm_path = Path(rpm_file.name)
            rpm_path.write_bytes(requests.get(url).content)
            results = rpm_tools.check_rpm_headers(rpm_path)
        self.assertEqual(
            r"""
                                                            Header Signatures: b'\x00\x00\x00>\x00\x00\x00\x07\xff\xff\xffp\x00\x00\x00\x10'
                                              OpenPGP RSA Signature Of Header: b'\x89\x01\x15\x03\x05\x00[\x08R$p\xaf\x9e\x819\xdb|\x82\x01\x08\x8a\xe2\x08\x00\xc2_\x1a\x1f\xc7E>\x9f\x96"(\x0eF4b>\xb4\x00\x99\xb1y\xab\xb1\xa8>\xe4\xe4\xeb\x99\xe2?D`\xd3\x0eS\xc7P{{\x88\x8d\xa3dB\xa3\xef\\{{\xa3\xf8\x06cg\xc1\x98\xea\x82u\xa4\xb9.r^o\x91\xe2o\x19\x1c\xcc$\xf9\xcd\x1b\x85\x98f[\xa2\xdd!3_\xde\x81\xea`\x99\xeb\x83Y\xd1\xfaw\x81\xf774\xd1\x11\xf6\xbf\x98\xb2\xb1\x84\xf1\x9e^l\x1eY\xc9\x9c\x1c\xed\xc8\xd3[X\xeb\xc7h7\x82V\xab\x80\xd7]\xb0\xdbC\x86\xe2\xc0\x9d\x86\xd0 %\x1e{{\x1c\xd394\x89\xabp8\x04GE\xf4Z4(\xeaoF\xec\xe1\x9c&\xd1\x17z\x8dC/\x08\xf0\x0e(\xcc9\x04\xddJ\xb3b\xe4)\x8b\'\xac\x15\xb6\x1a?\xb2\xd9\xdf\xbeJ\xf7\xd8\xfa~*\xaa\xa5S\x8c\xd8\x0c\xd1J\xec<j\xee\xf3\xab9\x10Fe\xaa4I\xf4;\xd4v\x83\xe9BMN\xff\xd3{{\xb2\xd1(Py"\x1f\'\'(\xc9?:\xb1\xee\xd9\x0f\x1f\x8c\x9d|P'
                                                        SHA1 Digest Of Header: dbeb3eb27337e5d21b569b6cc73165320c35164b
                                                      SHA256 Digest Of Header: 3c4d1b9d2da6a1223c2ed6b2187f6c9618982c9526405ab88112fde3a06fe03e
                                                                 Package Name: libaio1
                                                              Package Release: 1.25
                                                             One-line Summary: Linux-Native Asynchronous I/O Access Library
                                                     Hostname Of Build System: sheep53
                                                    Package Installation Time: None
                                            Unmodified, Original Header Image: b'\x00\x00\x00?\x00\x00\x00\x07\xff\xff\xfb\xd0\x00\x00\x00\x10'
                                                   Header Translation Locales: ['C']
                                                              Package Version: 0.3.109
                                                       Multi-line Description: The Linux-native asynchronous I/O facility ("async I/O", or "aio") has
a richer API and capability set than the simple POSIX async I/O
facility. This library provides the Linux-native API for async I/O. The
POSIX async I/O facility requires this library to provide
kernel-accelerated async I/O capabilities, as do applications that
require the Linux-native async I/O API.
                                                           Package Build Time: datetime.datetime(2018, 5, 25, 18, 12, 44, tzinfo=datetime.timezone.utc)
                                                       Installed Package Size: 32262
                                                            Distribution Name: SUSE Linux Enterprise 15
                                                               Package Vendor: SUSE LLC <https://www.suse.com/>
                                                          License Of Contents: LGPL-2.1+
                                                                     Packager: https://www.suse.com/
                                                                Package Group: System/Libraries
                                                                 Upstream URL: http://kernel.org/pub/linux/libs/aio/
                                                             Operating System: linux
                                                                 Architecture: x86_64
                                                 File Sizes (when all < 4 GB): [15, 5608, 0, 26532, 122]
                                                             Unix Files Modes: [-24065, -32275, 16877, -32348, -32348]
                                                 Device IDs (of device files): [0, 0, 0, 0, 0]
                                                 File Modification Timestamps: [datetime.datetime(2018, 5, 25, 18, 12, 43, tzinfo=datetime.timezone.utc), datetime.datetime(2018, 5, 25, 18, 12, 43, tzinfo=datetime.timezone.utc), datetime.datetime(2018, 5, 25, 18, 12, 44, tzinfo=datetime.timezone.utc), datetime.datetime(2009, 10, 9, 18, 17, 2, tzinfo=datetime.timezone.utc), datetime.datetime(2009, 10, 9, 18, 17, 2, tzinfo=datetime.timezone.utc)]
                                                                    File Hash: ['', 'bf8977f717cdf65b34fdad5e00daec89bdbc9a6ac512887c5cf2e78ff7cc7191', '', '5bbcbb737e60fe9deba08ecbd00920cfcc3403ba2e534c64fdeea49d6bb87509', 'f7b7efb8cb7bf444fe0f8c97f0989308e0a6d54e888c87db501494973d2c656b']
                                                         File Symlink Targets: ['libaio.so.1.0.1', '', '', '', '']
                                                                   File Flags: {file_flags}
                                                        File Unix Owner Names: ['root', 'root', 'root', 'root', 'root']
                                                        File Unix Group Names: ['root', 'root', 'root', 'root', 'root']
                                                          Source RPM Filename: libaio-0.3.109-1.25.src.rpm
                                                      File Verification Flags: {file_verification_flags}
                                                               Provided Names: ['libaio', 'libaio.so.1()(64bit)', 'libaio.so.1(LIBAIO_0.1)(64bit)', 'libaio.so.1(LIBAIO_0.4)(64bit)', 'libaio1', 'libaio1(x86-64)']
                                                       Required Names (Flags): {required_names_flags}
                                                               Required Names: ['/sbin/ldconfig', '/sbin/ldconfig', 'libc.so.6()(64bit)', 'libc.so.6(GLIBC_2.4)(64bit)', 'rpmlib(CompressedFileNames)', 'rpmlib(FileDigests)', 'rpmlib(PayloadFilesHavePrefix)', 'rpmlib(PayloadIsXz)']
                                                    Required Names (Versions): ['', '', '', '', '3.0.4-1', '4.6.0-1', '4.0-1', '5.2-1']
                                                     RPM Version For Building: 4.14.1
                                                         Changelog Timestamps: [datetime.datetime(2016, 4, 17, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2014, 8, 26, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2013, 3, 1, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2012, 2, 17, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2012, 2, 16, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2012, 2, 13, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 11, 28, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 11, 28, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 10, 5, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 9, 30, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 3, 15, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2010, 2, 12, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2010, 1, 23, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2009, 8, 2, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2009, 3, 3, 12, 0, tzinfo=datetime.timezone.utc)]
                                                            Changelog Authors: ['meissner@suse.com', 'fcrozat@suse.com', 'dmueller@suse.com', 'coolo@suse.com', 'mvyskocil@suse.cz', 'coolo@suse.com', 'jengelh@medozas.de', 'ro@suse.de', 'uli@suse.com', 'adrian@suse.de', 'jengelh@medozas.de', 'jengelh@medozas.de', 'jengelh@medozas.de', 'jansimon.moeller@opensuse.org', 'crrodriguez@suse.de']
                                                              Changelog Texts: ['- libaio-optflags.diff: readd -stdlib to allow -fstack-protector-strong\n  builds (unclear why it was not allowed)\n- 01_link_libgcc.patch, 02_libdevdir.patch: refreshed', '- Add obsoletes/provides to baselibs.conf (bsc#881698)', '- Add libaio-aarch64-support.diff:\n  * add support for aarch64\n- Add libaio-generic-arch.diff:\n  * support all archtes (also aarch64)', '- fix baselibs.conf after shlib split', '- fix typo versoin/version', '- patch license to follow spdx.org standard', '- Remove redundant/unwanted tags/section (cf. specfile guidelines)\n- Employ shlib packaging', '- fix lib64 platform check', '- cross-build fix: use %__cc macro', '- drop debian arm hack to fix build on arm ;)', '- Update to libaio 0.3.109\n  * add ARM architecture support (grabbed from Debian arches tree)\n  * replace check of __i386__ with __LP64__ in test harness\n- refreshed patches', '- fix more symbolic links to not include a /usr/src/ prefix', '- update to libaio 0.3.107\n- add more patches from Debian to fix compile errors on SPARC\n- package baselibs.conf', '- add ARM support to libaio sources', '- remove static libraries\n- fix -devel package dependencies']
                                    Post-installation Interpreter + Arguments: /sbin/ldconfig
                                  Post-uninstallation Interpreter + Arguments: /sbin/ldconfig
                                                               Obsolete Names: ['libaio']
                                                   Cookie For Build Operation: sheep53 1527271964
                                                                 File Devices: [1, 1, 1, 1, 1]
                                                  Abstract File Inode Numbers: [1, 2, 3, 4, 5]
                                                               File Languages: ['', '', '', '', '']
                                                       Provided Names (Flags): [<DependencyFlags.EQUAL: 8>, <DependencyFlags.FIND_PROVIDES: 32768>, <DependencyFlags.FIND_PROVIDES: 32768>, <DependencyFlags.FIND_PROVIDES: 32768>, <DependencyFlags.EQUAL: 8>, <DependencyFlags.EQUAL: 8>]
                                                    Provided Names (Versions): ['0.3.109-1.25', '', '', '', '0.3.109-1.25', '0.3.109-1.25']
                                                       Obsolete Names (Flags): <DependencyFlags.LESS: 2>
                                                    Obsolete Names (Versions): ['0.3.109-1.25']
                                     Index Into Directory Names For Basenames: [0, 0, 1, 2, 2]
                                                                    Basenames: ['libaio.so.1', 'libaio.so.1.0.1', 'libaio1', 'COPYING', 'TODO']
                                                              Directory Names: ['/lib64/', '/usr/share/doc/packages/', '/usr/share/doc/packages/libaio1/']
                                               %{{optflags}} Value During Build: -fmessage-length=0 -grecord-gcc-switches -O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -g
                                                    Distribution-specific URL: obs://build.suse.de/SUSE:SLE-15:GA/standard/77c22af2cb0aefbc84316daac8f5b8ac-libaio
                                                               Payload Format: cpio
                                                      Payload Compressor Name: xz
                                                     Payload Compressor Level: 5
                                                             Package Platform: x86_64-suse-linux
                                                  Index Into Class Dictionary: [0, 1, 2, 3, 3]
                               Class Dictionary (File Class libmagic Entries): ['', 'ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=98eb213e51c843c9263a66ad0a5718c06a388a1c, stripped', 'directory', 'ASCII text']
Index Into File Dependencies Dictionary Denoting Start Of File's Dependencies: [0, 0, 0, 0, 0]
                       Number Of File Dependencies in Dependencies Dictionary: [0, 6, 0, 0, 0]
                                                 File Dependencies Dictionary: [1342177282, 1342177283, 1342177283, 1342177281, 1375731715, 1375731714]
                                                    Source Package Identifier: b'\xcc\x8cLq\xe6\xf8\xcb\xbf\xfa\x14\xcc6Li\x18\x85'
                                                        File Digest Algorithm: <FileDigestAlgorithm.SHA512: 8>
                                                  Header String Data Encoding: utf-8
                               Cryptographic Digest of the Compressed Payload: ['f001b298e5add90e4d2fdbc442b92b8aae7beb5fac77159a5baa33fb7217d48a']
                                                     Payload Digest Algorithm: <FileDigestAlgorithm.SHA512: 8>
"""[1:-1].format(file_flags=file_flags, file_verification_flags=file_verification_flags, required_names_flags=required_names_flags),  # noqa: E501
            results
        )

    def test_source(self) -> None:
        if sys.version_info < (3, 11):
            file_flags = "[<FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.0: 0>, <FileFlags.SPECFILE: 32>]"  # noqa: E501
            file_verification_flags = "[<VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>, <VerifyFlags.CAPS|RDEV|MODE|MTIME|GROUP|USER|LINK_TO|SIZE|MD5: -1>]"  # noqa: E501
            required_names_flags = "[<DependencyFlags.RPMLIB|EQUAL|LESS: 16777226>, <DependencyFlags.RPMLIB|EQUAL|LESS: 16777226>]"
        else:
            file_flags = "[<FileFlags: 0>, <FileFlags: 0>, <FileFlags: 0>, <FileFlags: 0>, <FileFlags: 0>, <FileFlags: 0>, <FileFlags: 0>, <FileFlags: 0>, <FileFlags: 0>, <FileFlags: 0>, <FileFlags.SPECFILE: 32>]"  # noqa: E501
            file_verification_flags = "[<VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>, <VerifyFlags.MD5|SIZE|LINK_TO|USER|GROUP|MTIME|MODE|RDEV|CAPS: 511>]"  # noqa: E501
            required_names_flags = "[<DependencyFlags.LESS|EQUAL|RPMLIB: 16777226>, <DependencyFlags.LESS|EQUAL|RPMLIB: 16777226>]"

        url = "https://download.opensuse.org/source/distribution/leap/15.6/repo/oss/src/libaio-0.3.109-1.25.src.rpm"
        with NamedTemporaryFile(suffix=".rpm") as rpm_file:
            rpm_path = Path(rpm_file.name)
            rpm_path.write_bytes(requests.get(url).content)
            results = rpm_tools.check_rpm_headers(rpm_path)
        self.assertEqual(
            r"""
                             Header Signatures: b'\x00\x00\x00>\x00\x00\x00\x07\xff\xff\xffp\x00\x00\x00\x10'
               OpenPGP RSA Signature Of Header: b'\x89\x01\x15\x03\x05\x00[\x08R$p\xaf\x9e\x819\xdb|\x82\x01\x08H\x05\x08\x00\x85wx\x9dG\xe0$\xfe\xf8\xf1*y\xfa\xc1\x0c\xa1-\xc9 B\xed\xf3\xfa\'\x80v\x91\xe1Wl\x02\xaf\x94\x06>^$\xe1\xca\xf3\x06\xc5\xaa\xa6\xa1\x85\x98\xa3\xdc\x00+\x03\xdd\x98\xef\xd2\x1d\x9b*\xb6Bu6J\xad\xf0\x12\xc9\xbb8"\x84\x9e\xbd\x87)\x94\xf3\xb4\x832\x99\xc1k\xf7r\xa3\xbf\xe9\xecA\xaf\x86\x02\xee\xb7\xb36;8\xc5\x19{{C\xfat\xdc\xec,\xdc\xef)\x92\xc4\xd3\xcd7\x88\xe0q\x18@\x95\x89n\xc3\x8a\xaah\\\x83\xd4L\xaa.\x00\xf3[\xce\xab\x17*D\xe4\xa4-\x1d-\x89\x15^\x02m\xec"\xca\n\xc4\xb9>\xcbS?\x14\x03\x00\x05#x\xb5\x83f\xc68A\x16\xe2k\x0e\x7f\x9bi\x9a\xe9\x88\xda\xf2j\t!K\xe7d\xa5\xf3\xaa2\xaay\xf2v\'\xb0\x11\xc9\x9an\xf2\x06\xefW6d\xa8\xf1\x85\xc7)\xc1\x05<\xea|\x8cJ\xb2\xc0\xd9\xe7\x10V=\xcd4\xf5:\xff\xf1\x1cL\xe5\xff9_\x14\'\x85u\xcd\xae\x8f\x11J\xf8\xd46'
                         SHA1 Digest Of Header: 42dd9660c0752a72f332b198f09c57a2a27a621e
                       SHA256 Digest Of Header: 453f75a56cd0fec8359b87d82e5423d332a4fe4c4fd2379261eea0d784e07a9a
                                  Package Name: libaio
                               Package Release: 1.25
                              One-line Summary: Linux-Native Asynchronous I/O Access Library
                      Hostname Of Build System: sheep53
                     Package Installation Time: None
             Unmodified, Original Header Image: b'\x00\x00\x00?\x00\x00\x00\x07\xff\xff\xfc\xb0\x00\x00\x00\x10'
                    Header Translation Locales: ['C']
                               Package Version: 0.3.109
                        Multi-line Description: The Linux-native asynchronous I/O facility ("async I/O", or "aio") has
a richer API and capability set than the simple POSIX async I/O
facility. This library provides the Linux-native API for async I/O. The
POSIX async I/O facility requires this library to provide
kernel-accelerated async I/O capabilities, as do applications that
require the Linux-native async I/O API.
                            Package Build Time: datetime.datetime(2018, 5, 25, 18, 12, 44, tzinfo=datetime.timezone.utc)
                        Installed Package Size: 158737
                             Distribution Name: SUSE Linux Enterprise 15
                                Package Vendor: SUSE LLC <https://www.suse.com/>
                           License Of Contents: LGPL-2.1+
                                      Packager: https://www.suse.com/
                                 Package Group: Development/Libraries/C and C++
                             Source File Names: ['baselibs.conf', 'libaio-0.3.109.tar.bz2']
                              Patch File Names: ['libaio-generic-arch.diff', 'libaio-aarch64-support.diff', '03_man_errors.patch', '02_libdevdir.patch', '01_link_libgcc.patch', '00_arches_sh.patch', '00_arches.patch', 'libaio-optflags.diff']
                                  Upstream URL: http://kernel.org/pub/linux/libs/aio/
                              Operating System: linux
                                  Architecture: x86_64
                  File Sizes (when all < 4 GB): [22666, 5028, 500, 2159, 73868, 207, 43579, 1018, 2053, 512, 7147]
                              Unix Files Modes: [-32348, -32348, -32348, -32348, -32348, -32348, -32348, -32348, -32348, -32348, -32348]
                  Device IDs (of device files): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                  File Modification Timestamps: [datetime.datetime(2011, 3, 24, 8, 43, 41, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 3, 24, 8, 43, 41, tzinfo=datetime.timezone.utc), datetime.datetime(2016, 4, 22, 14, 18, tzinfo=datetime.timezone.utc), datetime.datetime(2016, 4, 22, 14, 18, tzinfo=datetime.timezone.utc), datetime.datetime(2010, 2, 11, 19, 16, 55, tzinfo=datetime.timezone.utc), datetime.datetime(2014, 8, 26, 11, 53, 35, tzinfo=datetime.timezone.utc), datetime.datetime(2009, 11, 20, 14, 31, 19, tzinfo=datetime.timezone.utc), datetime.datetime(2013, 3, 1, 10, 32, 38, tzinfo=datetime.timezone.utc), datetime.datetime(2013, 3, 1, 10, 32, 38, tzinfo=datetime.timezone.utc), datetime.datetime(2016, 4, 22, 14, 18, tzinfo=datetime.timezone.utc), datetime.datetime(2018, 5, 25, 18, 12, 42, tzinfo=datetime.timezone.utc)]
                                     File Hash: ['ab4b71ed9914e09c9470ed193e6049ab251e2f13bc17e7a54f5c74c0965c841e', 'e14215abee7b135f9d0d832e3544b30dc3e7540b0ccec8414ce42b1a47a86986', '9e615a1fe27800756e68017d25c8e029614a72993d27d4ecfe59d410867a0b8f', '2474d6f7378e254d47370b68a992f08ad30e8b522234c283754361accec55aea', 'cb4b2b1a128f9eb1ab6f39660359098950cb1906eb883d8b6ad38e8fa8c319fa', 'aa4d278101271a5a269ca3471402203d70f8da05c42d46c52be1b2e24f95cf59', 'b5cefce0a3cb49f8dca4d00e9480c0d9b45b75863bd44764156e322ee214e794', '76beebbc9cc994a1be1dbe686a4c20d5374462da03ffa512083ccd2dac940c1e', 'e91be00e676f63a54a82699c3e20766248587edc09f84bfd8207743519a8dfca', 'fa8847f11938773bd93ab17bd2b1319bb2fe094561aeaaf75fd840205ff112ff', '6261948d71f6ff1c4c321ddef3bb655196d898ac08b44ec7ec1ee20d9d59dcf6']
                          File Symlink Targets: ['', '', '', '', '', '', '', '', '', '', '']
                                    File Flags: {file_flags}
                         File Unix Owner Names: ['root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root']
                         File Unix Group Names: ['root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root']
                       File Verification Flags: {file_verification_flags}
                        Required Names (Flags): {required_names_flags}
                                Required Names: ['rpmlib(CompressedFileNames)', 'rpmlib(FileDigests)']
                     Required Names (Versions): ['3.0.4-1', '4.6.0-1']
                      RPM Version For Building: 4.14.1
                          Changelog Timestamps: [datetime.datetime(2016, 4, 17, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2014, 8, 26, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2013, 3, 1, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2012, 2, 17, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2012, 2, 16, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2012, 2, 13, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 11, 28, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 11, 28, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 10, 5, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 9, 30, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2011, 3, 15, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2010, 2, 12, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2010, 1, 23, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2009, 8, 2, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2009, 3, 3, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2008, 12, 10, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2008, 12, 4, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2008, 4, 10, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2007, 9, 27, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2007, 8, 2, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2006, 1, 25, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2005, 5, 5, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2005, 4, 27, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2004, 12, 1, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2004, 4, 20, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2004, 3, 12, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2004, 3, 2, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2004, 1, 11, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2003, 10, 1, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2003, 4, 23, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2003, 4, 23, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2003, 4, 11, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2003, 4, 3, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2002, 10, 1, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2002, 9, 20, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2002, 9, 19, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2002, 9, 17, 12, 0, tzinfo=datetime.timezone.utc), datetime.datetime(2002, 9, 4, 12, 0, tzinfo=datetime.timezone.utc)]
                             Changelog Authors: ['meissner@suse.com', 'fcrozat@suse.com', 'dmueller@suse.com', 'coolo@suse.com', 'mvyskocil@suse.cz', 'coolo@suse.com', 'jengelh@medozas.de', 'ro@suse.de', 'uli@suse.com', 'adrian@suse.de', 'jengelh@medozas.de', 'jengelh@medozas.de', 'jengelh@medozas.de', 'jansimon.moeller@opensuse.org', 'crrodriguez@suse.de', 'olh@suse.de', 'olh@suse.de', 'ro@suse.de', 'hare@suse.de', 'hare@suse.de', 'mls@suse.de', 'schwab@suse.de', 'kukuk@suse.de', 'kukuk@suse.de', 'meissner@suse.de', 'kukuk@suse.de', 'ro@suse.de', 'adrian@suse.de', 'schwab@suse.de', 'coolo@suse.de', 'coolo@suse.de', 'ro@suse.de', 'kukuk@suse.de', 'meissner@suse.de', 'fehr@suse.de', 'schwab@suse.de', 'ro@suse.de', 'fehr@suse.de']
                               Changelog Texts: ['- libaio-optflags.diff: readd -stdlib to allow -fstack-protector-strong\n  builds (unclear why it was not allowed)\n- 01_link_libgcc.patch, 02_libdevdir.patch: refreshed', '- Add obsoletes/provides to baselibs.conf (bsc#881698)', '- Add libaio-aarch64-support.diff:\n  * add support for aarch64\n- Add libaio-generic-arch.diff:\n  * support all archtes (also aarch64)', '- fix baselibs.conf after shlib split', '- fix typo versoin/version', '- patch license to follow spdx.org standard', '- Remove redundant/unwanted tags/section (cf. specfile guidelines)\n- Employ shlib packaging', '- fix lib64 platform check', '- cross-build fix: use %__cc macro', '- drop debian arm hack to fix build on arm ;)', '- Update to libaio 0.3.109\n  * add ARM architecture support (grabbed from Debian arches tree)\n  * replace check of __i386__ with __LP64__ in test harness\n- refreshed patches', '- fix more symbolic links to not include a /usr/src/ prefix', '- update to libaio 0.3.107\n- add more patches from Debian to fix compile errors on SPARC\n- package baselibs.conf', '- add ARM support to libaio sources', '- remove static libraries\n- fix -devel package dependencies', '- use Obsoletes: -XXbit only for ppc64 to help solver during distupgrade\n  (bnc#437293)', '- obsolete old -XXbit packages (bnc#437293)', '- added baselibs.conf file to build xxbit packages\n  for multilib support', '- Fix dangling symlink (#307063)', '- Use RPM_OPT_FLAGS\n- Fix installation directories', '- converted neededforbuild to BuildRequires', '- Fix ia64 assembler.', '- Update to version 0.3.104', '- Update to version 0.3.102 [#44374]', '- fixed ppc64 alignment problems. [#38801/LTC#7503]', '- Update to 0.3.98 [Bug #35266]', '- use -fPIC for shared objects on ppc', '- add %defattr and %run_ldconfig', '- Fix for ia64.', '- fix build for lib64', '- use BuildRoot', '- fix header to be includable with glibc (#26033)', '- Add missing "const" to libaio.h [#26030]', '- Fixed __syscall_return for ppc.', '- Add syscall defines for x86_64\n- add Andreas fix for testsuite main program to compile on x86_64\n- add another fix to make testsuite build again on ia64', '- Add missing bits for ia64.', '- removed bogus self-provides', '- make package from  libaio-0.3.15-2.5']
                    Cookie For Build Operation: sheep53 1527271964
                                  File Devices: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                   Abstract File Inode Numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                                File Languages: ['', '', '', '', '', '', '', '', '', '', '']
                                    Source RPM: 1
      Index Into Directory Names For Basenames: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                     Basenames: ['00_arches.patch', '00_arches_sh.patch', '01_link_libgcc.patch', '02_libdevdir.patch', '03_man_errors.patch', 'baselibs.conf', 'libaio-0.3.109.tar.bz2', 'libaio-aarch64-support.diff', 'libaio-generic-arch.diff', 'libaio-optflags.diff', 'libaio.spec']
                               Directory Names: ['']
                     Distribution-specific URL: obs://build.suse.de/SUSE:SLE-15:GA/standard/77c22af2cb0aefbc84316daac8f5b8ac-libaio
                                Payload Format: cpio
                       Payload Compressor Name: gzip
                      Payload Compressor Level: 9
                         File Digest Algorithm: <FileDigestAlgorithm.SHA512: 8>
                   Header String Data Encoding: utf-8
Cryptographic Digest of the Compressed Payload: ['75c03228af86b5aa125966962a19ec402ab330054264f74a4d877dd357a46c26']
                      Payload Digest Algorithm: <FileDigestAlgorithm.SHA512: 8>
"""[1:-1].format(file_flags=file_flags, file_verification_flags=file_verification_flags, required_names_flags=required_names_flags),  # noqa: E501
            results
        )