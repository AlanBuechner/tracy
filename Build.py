# tracy build script

import scripts.BuildUtils as BuildUtils
from scripts.Utils.Utils import *
from Config import *
import time

import inspect
projDir = os.path.dirname(inspect.getfile(lambda: None))
projName = os.path.basename(projDir)

sources = [
	"public/TracyClient.cpp"
]

headers = [
	"public/**.h"
]

includes = [
	"public",
]

sysIncludes = []
sysIncludes.extend(GetSysIncludes())

defines = [
	configuration.upper(),
	"_UNICODE",
	"UNICODE",
	"_CRT_SECURE_NO_WARNINGS",
	"TRACY_ENABLE",
]

def GetProject():
	proj = BuildUtils.ProjectEnviernment()
	proj.projectDirectory = projDir
	proj.pchSource = ""
	proj.pchHeader = ""
	proj.sources = sources
	proj.resources = []
	proj.headers = headers
	proj.includes = includes
	proj.sysIncludes = sysIncludes
	proj.defines = defines
	proj.links = []
	proj.buildType = BuildUtils.BuildType.STATICLIBRARY
	proj.intDir = GetIntDir(projName)
	proj.binDir = GetBinDir(projName)
	return proj
