import os
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.password = os.getenv("CONAN_PASSWORD")
    builder.add_common_builds(shared_option_name="dlib:shared")
    builder.run()