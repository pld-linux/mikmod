%define		ver	3.1.6
%define		rel	a
Summary:	XM, MOD, MTM, S3M, STM, ULT, IT and UNI module player
Summary(pl):	Odtwarzacz modu��w d�wi�kowych XM, MOD, MTM, S3M, STM, ULT, IT e UNI
Summary(pt_BR):	Reprodutor de arquivos de som XM, MOD, MTM, S3M, STM, ULT, IT e UNI
Summary(es):	Reproductor de archivos de sonido XM, MOD, MTM, S3M, STM, ULT, IT e UNI
Name:		mikmod
Version:	%{ver}%{rel}
Release:	6
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(es):	Aplicaciones/Sonido
Group(pl):	Aplikacje/D�wi�k
Group(pt_BR):	Aplica��es/Som
Source0:	http://www.mikmod.org/files/mikmod/%{name}-%{ver}-%{rel}.tar.gz
URL:		http://www.mikmod.org/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	libmikmod-devel >= 3.1.7
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MikMod is one of the best and most well known MOD music file players
for UNIX-like systems. This particular distribution is intended to
compile fairly painlessly in a Linux environment. MikMod uses the OSS
/dev/dsp driver including all recent kernels for output, and will also
write .wav files. Supported file formats include MOD, STM, S3M, MTM,
XM, ULT, and IT. The player uses ncurses for console output and
supports transparent loading from gzip/pkzip/zoo archives and the
loading/saving of playlists.

Install the mikmod package if you need a MOD music file player.

%description -l pl
mikmod jest odtwarzaczem modu��w obs�uguj�cym formaty: 669, DSM, FAR,
IT, MOD, MED, MTM, S3M, ULT, XM i MOD-15.

Zainstaluj mikmod, je�eli potrzebujesz odtwarzacza plik�w MOD.

%description -l pt_BR
Um dos melhores e mais conhecido reprodutor de MOD para Unix. Reproduz
m�sicas em formato MOD.

O MikMod � um reprodutor port�vel de m�dulos originalmente escrito por
Jean-Paul Mikkers (MikMak) para o DOS. Ele foi subseq�entemente
modificado por muitas m�os e agora roda em muitas plataformas, com
esta distribui��o projetada para compilar sem problemas em um ambiente
Unix (Linux). Ele usa o driver /dev/dsp OSS incluso em todos os kernel
recentes para sa�da e tamb�m escreve arquivos wav. Os formatos de
arquivos suportados incluem: mod, stm, s3m, mtm, xm e it. O reprodutor
usa ncurses para sa�da no console e suporta carga transparente de
arquivos gzip/pkzip/zoo e carga/grava��o de listas de m�sicas para
reprodu��o.

%description -l es
Uno de los mejores y m�s conocido reproductor de MOD para Unix.
Reproduce m�sicas en formato MOD. MikMod es un reproductor port�til de
m�dulos originalmente escrito por Jean-Paul Mikkers (MikMak) para el
DOS. Fue sucesivamente modificado por muchas manos y ahora se ejecuta
en muchas plataformas, con esta distribuci�n proyectada para compilar
sin problemas en un ambiente Unix (Linux). Usa el driver /dev/dsp OSS
incluso en todos los kernel recientes para salida y tambi�n escribe
archivos wav. Los formatos de archivos soportados incluyen: mod, stm,
s3m, mtm, xm y it. El reproductor usa ncurses para salida en la
pantalla y soporta carga transparente de archivos gzip/pkzip/zoo y
carga/grabaci�n de listas de m�sicas para reproducci�n.


%prep
%setup -q -n %{name}-%{ver}-%{rel}

%build
aclocal
autoconf
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/mikmod
%{_mandir}/man1/*
