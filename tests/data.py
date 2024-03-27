# Copyright (c) stefan6419846. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.

from pathlib import Path

from tests import Download

from license_tools.tools.scancode_tools import (
    FileResults,
    LicenseClue,
    LicenseDetection,
    LicenseMatch,
    Licenses,
)


SETUP_PATH = Path(__file__).parent.parent / "setup.py"
LICENSE_PATH = SETUP_PATH.parent / "LICENSE.txt"


TYPING_EXTENSIONS__4_8_0__WHEEL = Download(
    url="https://files.pythonhosted.org/packages/24/21/7d397a4b7934ff4028987914ac1044d3b7d52712f30e2ac7a2ae5bc86dd0/typing_extensions-4.8.0-py3-none-any.whl",
    name="typing_extensions-4.8.0-py3-none-any.whl",
    suffix=".whl",
)

TYPING_EXTENSIONS__4_8_0__SDIST = Download(
    url="https://files.pythonhosted.org/packages/1f/7a/8b94bb016069caa12fc9f587b28080ac33b4fbb8ca369b98bc0a4828543e/typing_extensions-4.8.0.tar.gz",
    name="typing_extensions-4.8.0.tar.gz",
    suffix=".tar.gz",
)

LIBAIO1__0_3_109_1_25__RPM = Download(
    url="https://download.opensuse.org/distribution/leap/15.6/repo/oss/x86_64/libaio1-0.3.109-1.25.x86_64.rpm",
    name="libaio1-0.3.109-1.25.x86_64.rpm",
    suffix=".rpm",
)

LIBAIO1__0_3_109_1_25__SRC_RPM = Download(
    url="https://download.opensuse.org/source/distribution/leap/15.6/repo/oss/src/libaio-0.3.109-1.25.src.rpm",
    name="libaio1-0.3.109-1.25.src.rpm",
    suffix=".src.rpm",
)

PYPDF__3_17_4__WHEEL = Download(
    url="https://files.pythonhosted.org/packages/29/10/055b649e914ad8c5d07113c22805014988825abbeff007b0e89255b481fa/pypdf-3.17.4-py3-none-any.whl",
    name="pypdf-3.17.4-py3-none-any.whl",
    suffix=".whl",
)

JWCRYPTO__1_5_4__TAR_GZ = Download(
    url="https://files.pythonhosted.org/packages/13/f8/7b0a3e7ad80c04b8a020fa3061e4df8987a7d3c92f9ddc6552e4e908706b/jwcrypto-1.5.4.tar.gz",
    name="jwcrypto-1.5.4.tar.gz",
    suffix=".tar.gz",
)

JSON__20231013__JAR = Download(
    url="https://repo1.maven.org/maven2/org/json/json/20231013/json-20231013.jar",
    name="json-20231013.jar",
    suffix=".jar",
)


# Generated by `scancode-toolkit==32.0.8`.
SETUP_PY_LICENSES = Licenses(
    detected_license_expression="apache-2.0 AND (unknown-license-reference AND apache-2.0)",
    detected_license_expression_spdx="Apache-2.0 AND (LicenseRef-scancode-unknown-license-reference AND Apache-2.0)",
    percentage_of_license_text=19.55,
    license_detections=[
        LicenseDetection(
            license_expression="apache-2.0",
            license_expression_spdx="Apache-2.0",
            identifier="apache_2_0-1e5a86d5-35db-eb02-fd60-5cbcf1ec1d21",
            matches=[
                LicenseMatch(
                    score=100.0,
                    start_line=2,
                    end_line=2,
                    matched_length=6,
                    match_coverage=100.0,
                    matcher="1-spdx-id",
                    license_expression="apache-2.0",
                    spdx_license_expression="Apache-2.0",
                    rule_identifier="spdx-license-identifier-apache_2_0-5dcda840588b4f07f49f2c0100924ebca7bc0649",
                    rule_relevance=100,
                    rule_url=None,
                    from_file=None,
                ),
                LicenseMatch(
                    score=100.0,
                    start_line=3,
                    end_line=3,
                    matched_length=13,
                    match_coverage=100.0,
                    matcher="2-aho",
                    license_expression="apache-2.0",
                    spdx_license_expression="Apache-2.0",
                    rule_identifier="apache-2.0_1251.RULE",
                    rule_relevance=100,
                    rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/apache-2.0_1251.RULE",
                    from_file=None,
                ),
            ],
        ),
        LicenseDetection(
            license_expression="unknown-license-reference AND apache-2.0",
            license_expression_spdx="LicenseRef-scancode-unknown-license-reference AND Apache-2.0",
            identifier="unknown_license_reference_and_apache_2_0-1a5d5a31-4478-b9fc-43db-706bd5353d3d",
            matches=[
                LicenseMatch(
                    score=80.0,
                    start_line=15,
                    end_line=15,
                    matched_length=3,
                    match_coverage=100.0,
                    matcher="2-aho",
                    license_expression="unknown-license-reference",
                    spdx_license_expression="LicenseRef-scancode-unknown-license-reference",
                    rule_identifier="unknown-license-reference_331.RULE",
                    rule_relevance=80,
                    rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/unknown-license-reference_331.RULE",
                    from_file=None,
                ),
                LicenseMatch(
                    score=100.0,
                    start_line=17,
                    end_line=17,
                    matched_length=4,
                    match_coverage=100.0,
                    matcher="2-aho",
                    license_expression="apache-2.0",
                    spdx_license_expression="Apache-2.0",
                    rule_identifier="apache-2.0_65.RULE",
                    rule_relevance=100,
                    rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/apache-2.0_65.RULE",
                    from_file=None,
                ),
            ],
        ),
        LicenseDetection(
            license_expression="apache-2.0",
            license_expression_spdx="Apache-2.0",
            identifier="apache_2_0-e267f9d9-ae62-e9c9-9cc2-8cd0a1e4928f",
            matches=[
                LicenseMatch(
                    score=95.0,
                    start_line=51,
                    end_line=51,
                    matched_length=6,
                    match_coverage=100.0,
                    matcher="2-aho",
                    license_expression="apache-2.0",
                    spdx_license_expression="Apache-2.0",
                    rule_identifier="pypi_apache_no-version.RULE",
                    rule_relevance=95,
                    rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/pypi_apache_no-version.RULE",
                    from_file=None,
                )
            ],
        ),
    ],
    license_clues=[
        LicenseClue(
            score=50.0,
            start_line=57,
            end_line=57,
            matched_length=3,
            match_coverage=100.0,
            matcher="2-aho",
            license_expression="free-unknown",
            spdx_license_expression="LicenseRef-scancode-free-unknown",
            rule_identifier="free-unknown_88.RULE",
            rule_relevance=50,
            rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/free-unknown_88.RULE",
            from_file=None,
        )
    ],
)

TYPING_EXTENSION_4_8_0__WHEEL_FILES = [
    "typing_extensions-4.8.0.dist-info/LICENSE",
    "typing_extensions-4.8.0.dist-info/METADATA",
    "typing_extensions-4.8.0.dist-info/RECORD",
    "typing_extensions-4.8.0.dist-info/WHEEL",
    "typing_extensions.py",
]

TYPING_EXTENSION_4_8_0__SOURCE_FILES = [
    "typing_extensions-4.8.0/CHANGELOG.md",
    "typing_extensions-4.8.0/LICENSE",
    "typing_extensions-4.8.0/PKG-INFO",
    "typing_extensions-4.8.0/README.md",
    "typing_extensions-4.8.0/pyproject.toml",
    "typing_extensions-4.8.0/src/_typed_dict_test_helper.py",
    "typing_extensions-4.8.0/src/test_typing_extensions.py",
    "typing_extensions-4.8.0/src/typing_extensions.py",
    "typing_extensions-4.8.0/tox.ini",
]

# Generated by `scancode-toolkit==32.0.8`.
# `retrieve_licenses` has been set to `False` to avoid actually retrieving them.
TYPING_EXTENSION_4_8_0__LICENSES = [
    FileResults(
        path=Path("/tmp/tmpr6n2cx2i/typing_extensions-4.8.0.dist-info/LICENSE"),
        short_path="typing_extensions-4.8.0.dist-info/LICENSE",
        retrieve_copyrights=False,
        retrieve_emails=False,
        retrieve_urls=False,
        retrieve_licenses=False,
        retrieve_file_info=False,
        copyrights=None,
        emails=None,
        urls=None,
        licenses=Licenses(
            detected_license_expression="python AND (python AND bsd-new) AND (python AND bsd-new AND bsd-zero)",
            detected_license_expression_spdx="Python-2.0 AND (Python-2.0 AND BSD-3-Clause) AND (Python-2.0 AND BSD-3-Clause AND 0BSD)",
            percentage_of_license_text=96.26,
            license_detections=[
                LicenseDetection(
                    license_expression="python",
                    license_expression_spdx="Python-2.0",
                    identifier="python-0a1026f6-4441-3a49-a425-36ae51b9b171",
                    matches=[
                        LicenseMatch(
                            score=20.38,
                            start_line=5,
                            end_line=59,
                            matched_length=400,
                            match_coverage=20.38,
                            matcher="3-seq",
                            license_expression="python",
                            spdx_license_expression="Python-2.0",
                            rule_identifier="python_43.RULE",
                            rule_relevance=100,
                            rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/python_43.RULE",
                            from_file=None,
                        ),
                        LicenseMatch(
                            score=100.0,
                            start_line=62,
                            end_line=63,
                            matched_length=10,
                            match_coverage=100.0,
                            matcher="2-aho",
                            license_expression="python",
                            spdx_license_expression="Python-2.0",
                            rule_identifier="python_16.RULE",
                            rule_relevance=100,
                            rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/python_16.RULE",
                            from_file=None,
                        ),
                    ],
                ),
                LicenseDetection(
                    license_expression="python AND bsd-new",
                    license_expression_spdx="Python-2.0 AND BSD-3-Clause",
                    identifier="python_and_bsd_new-ef6a0b00-3e20-7b5f-60ad-13fd68dfafaa",
                    matches=[
                        LicenseMatch(
                            score=100.0,
                            start_line=66,
                            end_line=66,
                            matched_length=3,
                            match_coverage=100.0,
                            matcher="2-aho",
                            license_expression="unknown-license-reference",
                            spdx_license_expression="LicenseRef-scancode-unknown-license-reference",
                            rule_identifier="lead-in_unknown_30.RULE",
                            rule_relevance=100,
                            rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/lead-in_unknown_30.RULE",
                            from_file=None,
                        ),
                        LicenseMatch(
                            score=100.0,
                            start_line=66,
                            end_line=66,
                            matched_length=2,
                            match_coverage=100.0,
                            matcher="2-aho",
                            license_expression="python",
                            spdx_license_expression="Python-2.0",
                            rule_identifier="python_34.RULE",
                            rule_relevance=100,
                            rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/python_34.RULE",
                            from_file=None,
                        ),
                        LicenseMatch(
                            score=99.0,
                            start_line=67,
                            end_line=67,
                            matched_length=2,
                            match_coverage=100.0,
                            matcher="2-aho",
                            license_expression="bsd-new",
                            spdx_license_expression="BSD-3-Clause",
                            rule_identifier="bsd-new_26.RULE",
                            rule_relevance=99,
                            rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/bsd-new_26.RULE",
                            from_file=None,
                        ),
                    ],
                ),
                LicenseDetection(
                    license_expression="python AND bsd-new AND bsd-zero",
                    license_expression_spdx="Python-2.0 AND BSD-3-Clause AND 0BSD",
                    identifier="python_and_bsd_new_and_bsd_zero-c0222c9a-2a19-8ee7-903b-cebffd111794",
                    matches=[
                        LicenseMatch(
                            score=78.37,
                            start_line=73,
                            end_line=265,
                            matched_length=1540,
                            match_coverage=78.37,
                            matcher="3-seq",
                            license_expression="python",
                            spdx_license_expression="Python-2.0",
                            rule_identifier="python_70.RULE",
                            rule_relevance=100,
                            rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/python_70.RULE",
                            from_file=None,
                        ),
                        LicenseMatch(
                            score=99.0,
                            start_line=267,
                            end_line=267,
                            matched_length=2,
                            match_coverage=100.0,
                            matcher="2-aho",
                            license_expression="bsd-new",
                            spdx_license_expression="BSD-3-Clause",
                            rule_identifier="bsd-new_26.RULE",
                            rule_relevance=99,
                            rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/bsd-new_26.RULE",
                            from_file=None,
                        ),
                        LicenseMatch(
                            score=100.0,
                            start_line=270,
                            end_line=279,
                            matched_length=98,
                            match_coverage=100.0,
                            matcher="2-aho",
                            license_expression="bsd-zero",
                            spdx_license_expression="0BSD",
                            rule_identifier="bsd-zero.LICENSE",
                            rule_relevance=100,
                            rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/licenses/bsd-zero.LICENSE",
                            from_file=None,
                        ),
                    ],
                ),
            ],
            license_clues=[],
        ),
        file_info=None,
    ),
    FileResults(
        path=Path("/tmp/tmpr6n2cx2i/typing_extensions-4.8.0.dist-info/METADATA"),
        short_path="typing_extensions-4.8.0.dist-info/METADATA",
        retrieve_copyrights=False,
        retrieve_emails=False,
        retrieve_urls=False,
        retrieve_licenses=False,
        retrieve_file_info=False,
        copyrights=None,
        emails=None,
        urls=None,
        licenses=Licenses(
            detected_license_expression="python",
            detected_license_expression_spdx="Python-2.0",
            percentage_of_license_text=2.01,
            license_detections=[
                LicenseDetection(
                    license_expression="python",
                    license_expression_spdx="Python-2.0",
                    identifier="python-03cf89ce-88f1-7600-71f7-302015c97123",
                    matches=[
                        LicenseMatch(
                            score=99.0,
                            start_line=12,
                            end_line=12,
                            matched_length=8,
                            match_coverage=100.0,
                            matcher="2-aho",
                            license_expression="python",
                            spdx_license_expression="Python-2.0",
                            rule_identifier="pypi_python_software_foundation_license2.RULE",
                            rule_relevance=99,
                            rule_url="https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/pypi_python_software_foundation_license2.RULE",  # noqa: E501
                            from_file=None,
                        )
                    ],
                )
            ],
            license_clues=[],
        ),
        file_info=None,
    ),
    FileResults(
        path=Path("/tmp/tmpr6n2cx2i/typing_extensions-4.8.0.dist-info/RECORD"),
        short_path="typing_extensions-4.8.0.dist-info/RECORD",
        retrieve_copyrights=False,
        retrieve_emails=False,
        retrieve_urls=False,
        retrieve_licenses=False,
        retrieve_file_info=False,
        copyrights=None,
        emails=None,
        urls=None,
        licenses=Licenses(
            detected_license_expression=None,
            detected_license_expression_spdx=None,
            percentage_of_license_text=0,
            license_detections=[],
            license_clues=[],
        ),
        file_info=None,
    ),
    FileResults(
        path=Path("/tmp/tmpr6n2cx2i/typing_extensions-4.8.0.dist-info/WHEEL"),
        short_path="typing_extensions-4.8.0.dist-info/WHEEL",
        retrieve_copyrights=False,
        retrieve_emails=False,
        retrieve_urls=False,
        retrieve_licenses=False,
        retrieve_file_info=False,
        copyrights=None,
        emails=None,
        urls=None,
        licenses=Licenses(
            detected_license_expression=None,
            detected_license_expression_spdx=None,
            percentage_of_license_text=0,
            license_detections=[],
            license_clues=[],
        ),
        file_info=None,
    ),
    FileResults(
        path=Path("/tmp/tmpr6n2cx2i/typing_extensions.py"),
        short_path="typing_extensions.py",
        retrieve_copyrights=False,
        retrieve_emails=False,
        retrieve_urls=False,
        retrieve_licenses=False,
        retrieve_file_info=False,
        copyrights=None,
        emails=None,
        urls=None,
        licenses=Licenses(
            detected_license_expression=None,
            detected_license_expression_spdx=None,
            percentage_of_license_text=0,
            license_detections=[],
            license_clues=[],
        ),
        file_info=None,
    ),
]

# Remove the leading linebreak which is just used to improve display here.
TYPING_EXTENSION_4_8_0__EXPECTED_OUTPUT = """
 typing_extensions-4.8.0.dist-info/LICENSE Python-2.0 AND (Python-2.0 AND BSD-3-Clause) AND (Python-2.0 AND BSD-3-Clause AND 0BSD) 
typing_extensions-4.8.0.dist-info/METADATA                                                             Python-2.0 [99.0]
  typing_extensions-4.8.0.dist-info/RECORD                                                                        
   typing_extensions-4.8.0.dist-info/WHEEL                                                                        
                      typing_extensions.py                                                                        

====================================================================================================

                                                                  None  3
                                                            Python-2.0  1
Python-2.0 AND (Python-2.0 AND BSD-3-Clause) AND (Python-2.0 AND BSD-3-Clause AND 0BSD)  1
"""[1:]  # noqa: W291
