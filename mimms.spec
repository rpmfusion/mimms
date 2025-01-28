Summary: MMS stream downloader
Name:    mimms
Version: 3.2.1
Release: 27%{?dist}
License: GPLv3+
Group:   Applications/Multimedia
URL:     http://savannah.nongnu.org/projects/mimms/
Source:  http://download.savannah.gnu.org/releases/mimms/mimms-%{version}.tar.bz2
Patch0:  convert_to_py3.patch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires:  libmms >= 0.4
BuildArch: noarch

%description
mimms is a program designed to allow you to download streams using the MMS
protocol and save them to your computer, as opposed to watching them live.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%files
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/mimms
%{python3_sitelib}/mimms-*.egg-info
%{python3_sitelib}/libmimms/
%{_mandir}/man1/mimms.1*

%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 01 2024 Leigh Scott <leigh123linux@gmail.com> - 3.2.1-26
- Patch to use python3

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

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

