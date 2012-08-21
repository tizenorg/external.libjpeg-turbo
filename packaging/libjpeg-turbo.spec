Name:           libjpeg-turbo
License:        BSD3c(or similar)
Group:          Productivity/Graphics/Convertors
AutoReqProv:    on
Version: 	1.2.0
Release:        2
Summary:        A MMX/SSE2 accelerated library for manipulating JPEG image files
Url:            http://sourceforge.net/projects/libjpeg-turbo
Source0:        %{name}-%{version}.tar.gz

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
autoreconf -fiv
%ifarch %{arm}
%configure --disable-static --with-jpeg8
%else
%configure --disable-static --with-jpeg8 --without-simd
%endif
make %{?_smp_mflags}

#%check
#make test libdir=%{_libdir}

%install
%makeinstall
# Fix perms
chmod -x README-turbo.txt release/copyright

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libturbojpeg.so
%exclude %{_datadir}/man/man1/*
%exclude %{_datadir}/doc/
%exclude %{_bindir}/cjpeg
%exclude %{_bindir}/djpeg
%exclude %{_bindir}/jpegtran
%exclude %{_bindir}/rdjpgcom
%exclude %{_bindir}/tjbench
%exclude %{_bindir}/wrjpgcom
%exclude %{_libdir}/libjpeg.so.*


%files devel
%defattr(-,root,root)
%{_includedir}/turbojpeg.h
%exclude %{_libdir}/libjpeg.so
%{_includedir}/turbojpeg/jpeglib.h
%{_includedir}/turbojpeg/jerror.h
%{_includedir}/turbojpeg/jmorecfg.h
%{_includedir}/turbojpeg/jconfig.h
%{_libdir}/pkgconfig/turbojpeg.pc
%exclude %{_libdir}/libjpeg.la
%exclude %{_libdir}/libturbojpeg.la
%exclude %{_datadir}/doc/README
%exclude %{_datadir}/doc/README-turbo.txt
%exclude %{_datadir}/doc/example.c
%exclude %{_datadir}/doc/libjpeg.txt
%exclude %{_datadir}/doc/structure.txt
%exclude %{_datadir}/doc/usage.txt
%exclude %{_datadir}/doc/wizard.txt
