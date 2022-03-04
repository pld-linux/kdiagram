%define		qtver		5.9.0
Summary:	KDiagram
Name:		kdiagram
Version:	2.8.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/kdiagram/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	a63593335d382d4c6518e1a98a9e013f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	qt5-build >= %{qtver}
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
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKChart.so.2
%attr(755,root,root) %{_libdir}/libKChart.so.2.*.*
%ghost %{_libdir}/libKGantt.so.2
%attr(755,root,root) %{_libdir}/libKGantt.so.2.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KChart
%{_includedir}/KGantt
%{_includedir}/kchart_version.h
%{_includedir}/kgantt_version.h
%{_libdir}/cmake/KChart
%{_libdir}/cmake/KGantt
%{_libdir}/libKChart.so
%{_libdir}/libKGantt.so
%{_libdir}/qt5/mkspecs/modules/qt_KChart.pri
%{_libdir}/qt5/mkspecs/modules/qt_KGantt.pri
