import os
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing -s compiler.libcxx=libstdc++11", remotes="https://api.bintray.com/a-alaa/public-conan/dlib")
    builder.add_common_builds(shared_option_name="dlib:shared", pure_c=False)
    builder.run()