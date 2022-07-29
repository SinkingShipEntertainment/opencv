name = "opencv"

authors = [
    "OpenCV"
]

version = "4.5.5"

description = \
    """
    Open Computing Vision
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

    #c.build_thread_count = "physical_cores"

requires = [
    "libjpeg",
    "libtiff",
    "libpng",
    "openexr",
    "tbb",
    "eigen",
    "numpy",
    "qt",
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-2.7.5"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.7.7"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.9.7"],
]

uuid = "repository.opencv"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():

    env.OPENCV_ROOT.append("{root}")
    env.OPENCV_LOCATION.append("{root}")

    # -----------------------------------------------------
    # Append to PYTHONPATH depending on the variant being used
    version_dir = None
    # NOTE: It should always be
    if "python" in resolve:
        ver = resolve["python"].version

        if ver.major == 2:
            version_dir = "python2.7"
        elif ver.major == 3:
            version_dir = "python3.7"

    if version_dir:
        env.PYTHONPATH.append("{root}/lib/" + version_dir + "/site-packages")
    # -----------------------------------------------------
