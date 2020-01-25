%bcond_without javadoc		# don't build apidocs

%define		srcname	gnu-getopt
Summary:	Java getopt implementation
Summary(pl.UTF-8):	Implementacja getopt w Javie
Name:		java-gnu-getopt
Version:	1.0.13
Release:	4
License:	LGPL
Group:		Libraries/Java
Source0:	ftp://ftp.urbanophile.com/pub/arenn/software/sources/java-getopt-%{version}.tar.gz
# Source0-md5:	46336d9bc055900f0320e5c378d7bfb2
URL:		http://www.urbanophile.com/arenn/hacking/download.html
BuildRequires:	ant >= 1.5
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Obsoletes:	gnu.getopt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU Java getopt classes support short and long argument parsing in
a manner 100% compatible with the version of GNU getopt in glibc 2.0.6
with a mostly compatible programmer's interface as well. Note that
this is a port, not a new implementation. I am currently unaware of
any bugs in this software, but there certainly could be some lying
about. I would appreciate bug reports as well as hearing about
positive experiences.

%description -l pl.UTF-8
Klasy GNU Java getopt potrafią analizować krótkie i długie argumenty w
sposób w 100% kompatybilny z wersją GNU getopt z glibc 2.0.6 przy w
większości kompatybilnym interfejsie programistycznym. Ten pakiet jest
portem, a nie nową implementacją. Autor nie zna żadnych błędów w tym
oprogramowaniu, ale na pewno jakieś istnieją, więc będzie uznawał
raporty o błędach, a także pozytywnych doświadczeniach.

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	gnu.getopt-javadoc

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name}.

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%prep
%setup -q -c
mv gnu/getopt/buildx.xml build.xml

%build
%ant jar %{?with_javadoc:javadoc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a build/lib/gnu.getopt.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc gnu/getopt/README
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
