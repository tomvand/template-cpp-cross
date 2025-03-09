"""
    Builder for WASM platform
"""

from SCons.Script import AlwaysBuild, Default, DefaultEnvironment

env = DefaultEnvironment()

progname = env['PROGNAME']

env.Replace(
    AR="emar",
    CC="emcc",
    CXX="em++",
    RANLIB="emranlib",
    SIZETOOL="emsize",

    PROGNAME=progname + ".html",

    SIZEPRINTCMD='$SIZETOOL $SOURCES'
)

#
# Target: Build executable program
#

target_bin = env.BuildProgram()

#
# Target: Execute binary
#

exec_action = env.VerboseAction(
    "$SOURCE $PROGRAM_ARGS", "Executing $SOURCE")

AlwaysBuild(env.Alias("exec", target_bin, exec_action))
AlwaysBuild(env.Alias("upload", target_bin, exec_action))

#
# Target: Print binary size
#

target_size = env.Alias("size", target_bin, env.VerboseAction(
    "$SIZEPRINTCMD", "Calculating size $SOURCE"))
AlwaysBuild(target_size)

#
# Default targets
#

Default([target_bin])