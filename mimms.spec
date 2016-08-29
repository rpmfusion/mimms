Summary: MMS stream downloader
Name:    mimms
Version: 3.2.1
Release: 10%{?dist}
License: GPLv3+
Group:   Applications/Multimedia
URL:     http://savannah.nongnu.org/projects/mimms/
Source:  http://download.savannah.gnu.org/releases/mimms/mimms-%{version}.tar.bz2
BuildRequires: python2-devel
Requires:  libmms >= 0.4
BuildArch: noarch

%description
mimms is a program designed to allow you to download streams using the MMS
protocol and save them to your computer, as opposed to watching them live.

%prep
%setup -q

%build
%py2_build

%install
%py2_install

%files
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/mimms
%{python2_sitelib}/mimms-*.egg-info
%{python2_sitelib}/libmimms/
%{_mandir}/man1/mimms.1*

%changelog
* Mon Aug 29 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.2.1-10
- Use python macros
- Clean spec file

* Mon Aug 01 2016 Sérgio Basto <sergio@serjux.com> - 3.2.1-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.2.1-7
- Mass rebuilt for Fedora 19 Features

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 24 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.2.1-5
- Rebuilt for python

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3.2.1-4
- rebuild for new F11 features

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 3.2.1-3
- Rebuild for new python.

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 3.2.1-2
- rebuild for RPM Fusion

* Tue Mar 18 2008 Matthias Saou <http://freshrpms.net/> 3.2.1-1
- Initial RPM release.

