Name:		gnu.getopt
Version:	1.0.9
Release:	0.1
Summary:	Java getopt implementation
License:	LGPL
Group:		Development/Languages/Java
URL:            http://www.urbanophile.com/arenn/hacking/download.htm
Source0:	ftp://ftp.urbanophile.com/pub/arenn/software/sources/java-getopt-%{version}.tar.gz
# Source0-md5:	ffbba007bb517dc42085d706ef7c0792
BuildRequires:	jakarta-ant >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
The GNU Java getopt classes support short and long argument parsing in
a manner 100% compatible with the version of GNU getopt in glibc 2.0.6
with a mostly compatible programmer's interface as well. Note that this
is a port, not a new implementation. I am currently unaware of any bugs
in this software, but there certainly could be some lying about. I would
appreciate bug reports as well as hearing about positive experiences.

%prep
%setup -q -c
mv gnu/getopt/buildx.xml build.xml

%build
ant jar
ant javadoc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
cp build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf %{name}.jar $RPM_BUILD_ROOT%{_javalibdir}/%{name}-%{version}.jar


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc gnu/getopt/COPYING.LIB gnu/getopt/README build/api
%{_javalibdir}/*.jar
