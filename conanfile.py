from conans import ConanFile, CMake, tools


class NetSnmpConan(ConanFile):
    name = "net-snmp"
    version = "5.8"
    license = "BSD"
    url = "https://github.com/weatherhead99/conan-net-snmp"
    description = "Net-SNMP is a suite of applications used to implement SNMP v1, SNMP v2c and SNMP v3 using both IPv4 and IPv6."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "net-snmp-5.8.tar.gz"

    def source(self):
        tools.untargz("net-snmp-%s.tar.gz" % self.version)

    def build(self):
        pass
    
    def package(self):
        pass