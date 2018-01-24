import os
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing", remotes="https://api.bintray.com/conan/bincrafters/public-conan")
    #builder.password = os.getenv("CONAN_PASSWORD")
    builder.add_common_builds(shared_option_name="dlib:shared", pure_c=False)
    builder.run()