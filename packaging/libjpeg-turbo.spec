Name:           libjpeg-turbo
License:        BSD3c(or similar)
Group:          Productivity/Graphics/Convertors
AutoReqProv:    on
Version:        1.1.90
Release:        7.2
Summary:        A MMX/SSE2 accelerated library for manipulating JPEG image files
Url:            http://sourceforge.net/projects/libjpeg-turbo
Source0:        %{name}-%{version}.tar.gz
Source1001: packaging/libjpeg-turbo.manifest 

%description
The libjpeg-turbo package contains a library of functions for manipulating
JPEG images.

%package devel

License:        BSD3c(or similar)
Summary:        Developement files for libjpeg-turbo contains a wrapper library (TurboJPEG/OSS) that emulates the TurboJPEG API using libjpeg-turbo
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description devel
The libjpeg-turbo shared libraries can be used as drop-in replacements for libjpeg on most systems




%prep
%setup -q 

%build
cp %{SOURCE1001} .
%ifarch %{arm}
%reconfigure --disable-static
%else
%reconfigure --disable-static --without-simd
%endif
make %{?_smp_mflags}

%check
make test libdir=%{_libdir}

%install
%make_install
# Fix perms

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%manifest libjpeg-turbo.manifest
%defattr(-,root,root)
%{_libdir}/libturbojpeg.so
%exclude %{_datadir}/man/man1/*
%exclude %{_bindir}/cjpeg
%exclude %{_bindir}/djpeg
%exclude %{_bindir}/jpegtran
%exclude %{_bindir}/rdjpgcom
%exclude %{_bindir}/tjbench
%exclude %{_bindir}/wrjpgcom
%exclude %{_libdir}/libjpeg.so.*


%files devel
%manifest libjpeg-turbo.manifest
%defattr(-,root,root)
%{_includedir}/turbojpeg.h
%exclude %{_libdir}/libjpeg.so
%exclude %{_includedir}/jconfig.h
%exclude %{_includedir}/jerror.h
%exclude %{_includedir}/jmorecfg.h
%exclude %{_includedir}/jpeglib.h


