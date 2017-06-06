Name:           ros-lunar-cpp-common
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS cpp_common package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/cpp_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       console-bridge-devel
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  ros-lunar-catkin

%description
cpp_common contains C++ code for doing things that are not necessarily ROS
related, but are useful for multiple packages. This includes things like the
ROS_DEPRECATED and ROS_FORCE_INLINE macros, as well as code for getting
backtraces. This package is a component of roscpp.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Jun 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.4-0
- Autogenerated by Bloom

* Mon May 15 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.3-0
- Autogenerated by Bloom

* Tue Feb 21 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.2-0
- Autogenerated by Bloom
