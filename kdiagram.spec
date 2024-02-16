%define		qtver		5.9.0
Summary:	KDiagram
Name:		kdiagram
Version:	3.0.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/kdiagram/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	06d2462d04e7826b347edc5baac85e10
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kdiagram

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{name}.

%prep
%setup -q

%build
%cmake -B build \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKChart6.so.3
%attr(755,root,root) %{_libdir}/libKChart6.so.*.*
%ghost %{_libdir}/libKGantt6.so.3
%attr(755,root,root) %{_libdir}/libKGantt6.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KChart6
%{_includedir}/KGantt6
%{_libdir}/cmake/KChart6
%{_libdir}/cmake/KGantt6
%{_libdir}/libKChart6.so
%{_libdir}/libKGantt6.so
%{_libdir}/qt6/mkspecs/modules/qt_KChart6.pri
%{_libdir}/qt6/mkspecs/modules/qt_KGantt6.pri
