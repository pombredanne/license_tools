# Copyright (c) stefan6419846. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.

from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from license_tools import retrieval
from license_tools.__main__ import log_level_type
from tests.data import TYPING_EXTENSION_4_8_0__EXPECTED_OUTPUT


EXAMPLE_CARGO_LOCK_FILE = """
# This file is automatically @generated by Cargo.
# It is not intended for manual editing.
version = 3

[[package]]
name = "autocfg"
version = "1.1.0"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "d468802bab17cbc0cc575e9b053f41e72aa36bfa6b7f55e3529ffa43161b97fa"

[[package]]
name = "base64"
version = "0.21.7"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "9d297deb1925b89f2ccc13d7635fa0714f12c87adce1c75356b39ca9b7178567"

[[package]]
name = "bitflags"
version = "1.3.2"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "bef38d45163c2f1dde094a7dfd33ccf595c92905c8f8f4fdc18d06fb1037718a"
"""

EXAMPLE_CARGO_LOCK_FILE__ONE_PACKAGE_ONLY = "".join(EXAMPLE_CARGO_LOCK_FILE.splitlines(keepends=True)[:10])


class LogLevelTypeTestCase(TestCase):
    def test_constant_name(self) -> None:
        self.assertEqual(40, log_level_type("error"))
        self.assertEqual(40, log_level_type("ERROR"))

    def test_integer(self) -> None:
        self.assertEqual(40, log_level_type(40))
        self.assertEqual(42, log_level_type(42))

    def test_invalid(self) -> None:
        with self.assertRaisesRegex(
                expected_exception=AttributeError, expected_regex=r"^module 'logging' has no attribute 'ABC'$"
        ):
            log_level_type("abc")


class MainTestCase(TestCase):
    @property
    def custom_env(self) -> dict[str, str]:
        custom_env = os.environ.copy()
        custom_env["COLUMNS"] = "100"
        custom_env["COVERAGE_PROCESS_START"] = "pyproject.toml"
        return custom_env

    def test_retrieval(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "license_tools", "--package", "typing_extensions==4.8.0", "--index-url", "https://pypi.org/simple"],
            capture_output=True, env=self.custom_env
        )
        self.assertEqual(0, result.returncode, result)
        self.assertEqual(b"", result.stderr)
        self.assertEqual(TYPING_EXTENSION_4_8_0__EXPECTED_OUTPUT, result.stdout.decode("UTF-8"))

    def test_cargo_lock_download(self) -> None:
        time.sleep(1)
        with TemporaryDirectory() as target_directory, TemporaryDirectory() as source_directory:
            cargo_lock = Path(source_directory) / "Cargo.lock"
            cargo_lock.write_text(EXAMPLE_CARGO_LOCK_FILE)

            result = subprocess.run(
                [sys.executable, "-m", "license_tools", "--cargo-lock-download", "--cargo-lock", cargo_lock, "--target-directory", target_directory],
                capture_output=True, env=self.custom_env
            )
            self.assertEqual(0, result.returncode, result)
            self.assertEqual(b"", result.stderr)
            self.assertEqual(b"", result.stdout)

            actual = [x[1] for x in retrieval.get_files_from_directory(target_directory)]
            self.assertEqual(
                [
                    "autocfg_1.1.0.crate",
                    "base64_0.21.7.crate",
                    "bitflags_1.3.2.crate"
                ],
                actual
            )

    def test_logging(self) -> None:
        time.sleep(1)
        with TemporaryDirectory() as target_directory, TemporaryDirectory() as source_directory:
            cargo_lock = Path(source_directory) / "Cargo.lock"
            cargo_lock.write_text(EXAMPLE_CARGO_LOCK_FILE__ONE_PACKAGE_ONLY)

            result = subprocess.run(
                [
                    sys.executable, "-m", "license_tools", "--cargo-lock-download", "--cargo-lock", cargo_lock, "--target-directory", target_directory,
                    "--log-level", "INFO",
                ],
                capture_output=True, env=self.custom_env
            )
            self.assertEqual(0, result.returncode, result)
            self.assertEqual(
                (
                    f"INFO:license_tools.utils.download_utils:Downloading https://crates.io/api/v1/crates/autocfg/1.1.0/download to "
                    f"{target_directory}/autocfg_1.1.0.crate ...\n"
                ),
                result.stderr.decode("UTF-8")
            )
            self.assertEqual(b"", result.stdout)

            actual = [x[1] for x in retrieval.get_files_from_directory(target_directory)]
            self.assertEqual(["autocfg_1.1.0.crate"], actual)
