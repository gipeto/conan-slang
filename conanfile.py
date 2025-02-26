from conan import ConanFile
import os
from conan.tools.files import get, copy


class slangRecipe(ConanFile):
    name = "slang"
    version = "2025.5.3"

    # Optional metadata
    license = "https://github.com/shader-slang/slang/blob/master/LICENSE"
    url = "https://github.com/shader-slang/slang.git"
    description = "slang shader language"
    topics = ("slang", "shaders")

    # Binary configuration
    settings = "os", "arch"

    def build(self):
        base_url = "https://github.com/shader-slang/slang/releases/download"

        _os = {"Windows": "windows", "Linux": "linux", "Macos": "macos"}.get(
            str(self.settings.os)
        )
        _arch = str(self.settings.arch).lower()

        if _arch == "armv8":
            _arch = "aarch64"

        _ext = "zip" if self.settings.os == "Windows" else "tar.gz"
        url = "{}/v{}/slang-{}-{}-{}.{}".format(
            base_url, self.version, self.version, _os, _arch, _ext
        )
        get(self, url)

    def package(self):
        copy(self, "*", self.build_folder, os.path.join(self.package_folder))

    def package_info(self):
        self.cpp_info.libs = ["slang"]
