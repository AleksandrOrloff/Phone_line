INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_CONTROL_RNG control_rng)

FIND_PATH(
    CONTROL_RNG_INCLUDE_DIRS
    NAMES control_rng/api.h
    HINTS $ENV{CONTROL_RNG_DIR}/include
        ${PC_CONTROL_RNG_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    CONTROL_RNG_LIBRARIES
    NAMES gnuradio-control_rng
    HINTS $ENV{CONTROL_RNG_DIR}/lib
        ${PC_CONTROL_RNG_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(CONTROL_RNG DEFAULT_MSG CONTROL_RNG_LIBRARIES CONTROL_RNG_INCLUDE_DIRS)
MARK_AS_ADVANCED(CONTROL_RNG_LIBRARIES CONTROL_RNG_INCLUDE_DIRS)

