Summary:	Java getopt implementation
Summary(pl):	Implementacja getopt w Javie
Name:		gnu.getopt
Version:	1.0.9
Release:	0.1
License:	LGPL
Group:		Development/Languages/Java
Source0:	ftp://ftp.urbanophile.com/pub/arenn/software/sources/java-getopt-%{version}.tar.gz
# Source0-md5:	ffbba007bb517dc42085d706ef7c0792
URL:		http://www.urbanophile.com/arenn/hacking/download.htm
BuildRequires:	jakarta-ant >= 1.5
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
The GNU Java getopt classes support short and long argument parsing in
a manner 100% compatible with the version of GNU getopt in glibc 2.0.6
with a mostly compatible programmer's interface as well. Note that
this is a port, not a new implementation. I am currently unaware of
any bugs in this software, but there certainly could be some lying
about. I would appreciate bug reports as well as hearing about
positive experiences.

%description -l pl
Klasy GNU Java getopt potrafi± analizowaæ krótkie i d³ugie argumenty w
sposób w 100% kompatybilny z wersj± GNU getopt z glibc 2.0.6 przy w
wiêkszo¶ci kompatybilnym interfejsie programistycznym. Ten pakiet jest
portem, a nie now± implementacj±. Autor nie zna ¿adnych b³êdów w tym
oprogramowaniu, ale na pewno jakie¶ istniej±, wiêc bêdzie uznawa³
raporty o b³êdach, a tak¿e pozytywnych do¶wiadczeniach.

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
%doc gnu/getopt/README build/api
%{_javalibdir}/*.jar
