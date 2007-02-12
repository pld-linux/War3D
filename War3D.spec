Summary:	War3D - strategy game
Summary(pl.UTF-8):	War3D - gra strategiczna
Name:		War3D
Version:	0.08.90
%define	_snap	20050909
Release:	0.1
License:	GPL
Group:		Applications/Games
Source0:	http://sparky.homelinux.org/snaps/war3d/%{name}Source-%{_snap}.tar.gz
# Source0-md5:	cc5441a384e64dd0a8412403170477d0
Source1:	%{name}.sh
Source2:	%{name}.desktop
Patch0:		%{name}-homeconfig.patch
URL:		http://war3d.solar-opensource.com/
BuildRequires:	OpenAL-devel
BuildRequires:	SolarSockets-devel
BuildRequires:	glut-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
# only because of SolarSockets:
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A 3D strategy game.

Warning: this game is not internationalized, everything is in Spanish.

%description -l pl.UTF-8
Gra strategiczna 3D.

Uwaga: nie jest umiędzynarodowiona, wszystko jest po hiszpańsku.

%prep
%setup -q -n %{name}Source
%patch0 -p1
sed -i 's/IRCClienteSocket.getIP()/MiIP/' IRCcomunicaciones.h

%build
%{__make} \
	CC="%{__cxx}" \
	CFLAGS="%{rpmcflags} -funsigned-char -c -ansi -I. -Wall" \
	LFLAGS="%{rpmldflags} -lglut -lsolarsockets -lopenal -lpng"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir},%{_desktopdir}}

install war3d $RPM_BUILD_ROOT%{_bindir}/war3d.bin
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/war3d
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

cp -r	Armys Edificios Efectos Esenarios Hud Interface	\
	Mapas Musica Objetos UnidadesDeCombate \
	War3D.conf \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/war3d*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
